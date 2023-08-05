import re
import shlex
import random
import shutil
import typing
import pathlib
import subprocess

import cldfbench
from cldfbench.datadir import DataDir
import nexus
from nexus.handlers.tree import Tree
from nexus.tools import delete_trees, sample_trees, strip_comments_in_trees
from pyglottolog.languoids import Glottocode
from clldutils.path import TemporaryDirectory, ensure_cmd
from pycldf.trees import TreeTable
from cldfviz.tree import render

from .metadata import Metadata
from .cldfwriter import CLDFWriter


class PhlorestDir(DataDir):
    """
    Enhanced `DataDir`, adding methods to access phylogenetic data.
    """
    def read_nexus(self,
                   path: typing.Optional[typing.Union[str, pathlib.Path]] = None,
                   text: typing.Optional[str] = None,
                   remove_rate: bool = False,
                   encoding: str = 'utf-8-sig',
                   preprocessor: typing.Callable[[str], str] = lambda s: s) -> nexus.NexusReader:
        """
        :param path: path to nexus file (or `None`).
        :param text: text content of a nexus file.
        :param remove_rate: Some trees have annotations before *and* after the colon, separating \
        the branch length. The newick package can't handle these. So we can remove the simpler \
        annotation after the ":".
        :return: Initialized `NexusReader` object.
        """
        assert (path or text) and not (path and text), 'Must pass either path or text'
        if not text:
            text = self.read(path, encoding=encoding)
        if remove_rate:
            text = self.remove_rate(text)
        return nexus.NexusReader.from_string(preprocessor(text))

    def read_trees(self,
                   path: typing.Union[str, pathlib.Path] = None,
                   text: str = None,
                   detranslate: bool = False,
                   burnin: int = 0,
                   sample: int = 0,
                   remove_rate: bool = False,
                   strip_annotation: bool = False,
                   preprocessor: typing.Callable[[str], str] = lambda s: s) -> typing.List[Tree]:
        """
        Reads trees from `path` and transforms them as required.

        Processing order:
            burnin -> sample -> strip_annotation -> remove_rate -> detranslate

        :param path: path to nexus file.
        :param text: nexus content in text.
        :param detranslate: return trees with translate blocks removed (default=False).
        :param burnin: number of trees to remove as burn-in (default=none).
        :param sample: number of trees to sample (default=all).
        :param remove_rate: remove extra rate information.
        :param strip_annotation: remove comments and annotations in trees (default=False).
        :param preprocessor: function to preprocess nexus text.
        :return:
        """
        nex = self.read_nexus(path=path, text=text, preprocessor=preprocessor)
        # remove burn-in first
        if burnin:
            nex = delete_trees(nex, list(range(burnin + 1)))
        # ..then sample if needed
        if sample and len(nex.trees.trees) > sample:
            nex = sample_trees(nex, sample)
        # remove comments if asked
        if strip_annotation:
            nex = strip_comments_in_trees(nex)
        # remove rates if asked
        if remove_rate:
            nex.trees.trees = [self.remove_rate(t) for t in nex.trees.trees]
        # ...then detranslate.
        if detranslate:
            nex.trees.detranslate()
        return nex.trees.trees

    def read_tree(self,
                  path: typing.Union[str, pathlib.Path] = None,
                  text: str = None,
                  detranslate: bool = False,
                  burnin: int = 0,
                  sample: int = 0,
                  remove_rate: bool = False,
                  strip_annotation: bool = False,
                  preprocessor=lambda s: s) -> Tree:
        return self.read_trees(
            path=path,
            text=text,
            detranslate=detranslate,
            burnin=burnin,
            sample=sample,
            remove_rate=remove_rate,
            strip_annotation=strip_annotation,
            preprocessor=preprocessor)[0]

    def remove_rate(self, text: str) -> Tree:
        """
        Some trees have annotations before *and* after the colon (i.e. on the
        node), separating the branch length. The newick package can't handle
        these. This method removes the simpler annotation after the ":", keeping
        the branch annotations.

        :param text: nexus content in text.
        :return: str
        """
        return Tree(re.sub(r':\[&rate=[0-9]*\.?[0-9]*]', ':', text))


class Dataset(cldfbench.Dataset):
    """
    An augmented `cldfbench.Dataset`

    - swapping in `PhlorestDir` as `DataDir` implementation for `raw`
    - swapping in a custom CLDFWriter implementation `phorest.cldfwriter.CLDFWriter`
    - adding methods to be called in implementations of `cmd_makecldf` for simpler manipulation of \
      phylogenetic data,
    - enhancing README.md by adding an SVG plot of the summary tree.
    """
    metadata_cls = Metadata
    datadir_cls = PhlorestDir

    def __init__(self):
        cldfbench.Dataset.__init__(self)
        self._lids = set()

    def cldf_specs(self):  # A dataset must declare all CLDF sets it creates.
        return cldfbench.CLDFSpec(dir=self.cldf_dir, writer_cls=CLDFWriter)

    def cmd_download(self, args):  # pragma: no cover
        pass

    def _cmd_makecldf(self, args):
        if self.metadata.family and Glottocode.pattern.match(self.metadata.family):
            glang = args.glottolog.api.languoid(self.metadata.family)
            self.metadata.family = '{} [{}]'.format(glang.name, glang.id)
        cldfbench.Dataset._cmd_makecldf(self, args)

        cldf = self.cldf_reader()
        for tree in TreeTable(cldf):
            if tree.tree_type == 'summary':
                legend = "Summary tree"
                if cldf.properties.get('dc:subject', {}).get('analysis'):
                    title = cldf.properties['dc:subject']['analysis'].title()
                    legend += ' of a {} analysis'.format(title)
                if cldf.properties.get('dc:subject', {}).get('family'):
                    family = cldf.properties['dc:subject']['family']
                    legend += ' of the {} family'.format(family)
                if tree.tree_branch_length_unit:
                    legend += ' with branches in {}'.format(tree.tree_branch_length_unit)

                return render(
                    tree,
                    self.dir / 'summary_tree.svg',
                    glottolog_mapping={
                        r['ID']: (r['Glottocode'], r.get('Glottolog_Name'))
                        for r in cldf['LanguageTable'] if r['Glottocode']},
                    legend=legend,
                    width=1000,
                    with_glottolog_links=True
                )

    def init(self, args):
        """
        Create rows in LanguageTable according to `etc/taxa.csv` and add sources from
        `raw/source.bib`.
        """
        args.writer.add_taxa(self.taxa, args.glottolog.api, args.log)
        if self.raw_dir.joinpath('source.bib').exists():
            args.writer.cldf.sources.add(
                self.raw_dir.joinpath('source.bib').read_text(encoding='utf8'))

    def _cmd_readme(self, args):
        cldfbench.Dataset._cmd_readme(self, args)
        if self.dir.joinpath('summary_tree.svg').exists():
            text = self.dir.joinpath('README.md').read_text(encoding='utf8')
            text += '\n\n## Summary Tree\n\n![summary](./summary_tree.svg)'
            self.dir.joinpath('README.md').write_text(text, encoding='utf8')

    def _read_from_etc(self, name):
        if (self.etc_dir / name).exists():
            return list(self.etc_dir.read_csv(name, dicts=True))
        return []

    @property
    def taxa(self) -> typing.List[dict]:
        return self._read_from_etc('taxa.csv')

    @property
    def characters(self) -> typing.List[dict]:
        return self._read_from_etc('characters.csv')

    def run_treeannotator(self, cmd, input):
        with TemporaryDirectory() as d:
            in_ = d / 'in.nex'
            if isinstance(input, str):
                in_.write_text(input, encoding='utf8')
            else:
                shutil.copy(input, in_)
            out = d / 'out.nex'
            subprocess.check_call(
                [ensure_cmd('treeannotator')] + shlex.split(cmd) + [str(in_), str(out)],
                stderr=subprocess.DEVNULL,
            )
            return nexus.NexusReader.from_string(out.read_text(encoding='utf8'))

    def run_rscript(self, script, output_fname):
        with TemporaryDirectory() as d:
            d.joinpath('script.r').write_text(script, encoding='utf8')
            subprocess.check_call([ensure_cmd('Rscript'), str(d / 'script.r')], cwd=d)
            return d.joinpath(output_fname).read_text(encoding='utf8')

    def remove_burnin(self, input, amount, as_nexus=False):
        res = delete_trees(input, list(range(amount + 1)))
        return res if as_nexus else res.write()

    def sample(self,
               input,
               seed=12345,
               detranslate=False,
               as_nexus=False,
               n=1000,
               strip_annotation=False):
        random.seed(seed)
        res = sample_trees(input, n)
        if strip_annotation:
            res = strip_comments_in_trees(res)
        if detranslate:
            res.trees.detranslate()
        return res if as_nexus else res.write()
