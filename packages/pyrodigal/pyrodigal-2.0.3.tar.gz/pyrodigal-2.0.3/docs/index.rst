Pyrodigal |Stars|
=================

.. |Stars| image:: https://img.shields.io/github/stars/althonos/pyrodigal.svg?style=social&maxAge=3600&label=Star
   :target: https://github.com/althonos/pyrodigal/stargazers

*Cython bindings and Python interface to* `Prodigal <https://github.com/hyattpd/Prodigal/>`_,
*an ORF finder for genomes and metagenomes*. **Now with SIMD!**

|Actions| |Coverage| |PyPI| |Bioconda| |AUR| |Wheel| |Versions| |Implementations| |License| |Source| |Mirror| |Issues| |Docs| |Changelog| |Downloads| |Paper|

.. |Actions| image:: https://img.shields.io/github/actions/workflow/status/althonos/pyrodigal/test.yml?branch=main&logo=github&style=flat-square&maxAge=300
   :target: https://github.com/althonos/pyrodigal/actions

.. |GitLabCI| image:: https://img.shields.io/gitlab/pipeline/larralde/pyrodigal/main?gitlab_url=https%3A%2F%2Fgit.embl.de&logo=gitlab&style=flat-square&maxAge=600
   :target: https://git.embl.de/larralde/pyrodigal/-/pipelines

.. |Coverage| image:: https://img.shields.io/codecov/c/gh/althonos/pyrodigal?style=flat-square&maxAge=600
   :target: https://codecov.io/gh/althonos/pyrodigal/

.. |PyPI| image:: https://img.shields.io/pypi/v/pyrodigal.svg?style=flat-square&maxAge=3600
   :target: https://pypi.python.org/pypi/pyrodigal

.. |Bioconda| image:: https://img.shields.io/conda/vn/bioconda/pyrodigal?style=flat-square&maxAge=3600
   :target: https://anaconda.org/bioconda/pyrodigal

.. |AUR| image:: https://img.shields.io/aur/version/python-pyrodigal?logo=archlinux&style=flat-square&maxAge=3600
   :target: https://aur.archlinux.org/packages/python-pyrodigal

.. |Wheel| image:: https://img.shields.io/pypi/wheel/pyrodigal?style=flat-square&maxAge=3600
   :target: https://pypi.org/project/pyrodigal/#files

.. |Versions| image:: https://img.shields.io/pypi/pyversions/pyrodigal.svg?style=flat-square&maxAge=3600
   :target: https://pypi.org/project/pyrodigal/#files

.. |Implementations| image:: https://img.shields.io/pypi/implementation/pyrodigal.svg?style=flat-square&maxAge=3600&label=impl
   :target: https://pypi.org/project/pyrodigal/#files

.. |License| image:: https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square&maxAge=3600
   :target: https://choosealicense.com/licenses/mit/

.. |Source| image:: https://img.shields.io/badge/source-GitHub-303030.svg?maxAge=2678400&style=flat-square
   :target: https://github.com/althonos/pyrodigal/

.. |Mirror| image:: https://img.shields.io/badge/mirror-EMBL-009f4d?style=flat-square&maxAge=2678400
   :target: https://git.embl.de/larralde/pyrodigal/

.. |Issues| image:: https://img.shields.io/github/issues/althonos/pyrodigal.svg?style=flat-square&maxAge=600
   :target: https://github.com/althonos/pyrodigal/issues

.. |Docs| image:: https://img.shields.io/readthedocs/pyrodigal?style=flat-square&maxAge=3600
   :target: http://pyrodigal.readthedocs.io/en/stable/?badge=stable

.. |Changelog| image:: https://img.shields.io/badge/keep%20a-changelog-8A0707.svg?maxAge=2678400&style=flat-square
   :target: https://github.com/althonos/pyrodigal/blob/main/CHANGELOG.md

.. |Downloads| image:: https://img.shields.io/badge/dynamic/json?style=flat-square&color=303f9f&maxAge=86400&label=downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2Fpyrodigal
   :target: https://pepy.tech/project/pyrodigal

.. |Paper| image:: https://img.shields.io/badge/paper-JOSS-9400ff?style=flat-square&maxAge=86400
   :target: https://doi.org/10.21105/joss.04296


Overview
--------

Pyrodigal is a Python module that provides bindings to Prodigal using
`Cython <https://cython.org/>`_. It directly interacts with the Prodigal
internals, which has the following advantages:

- **single dependency**: Pyrodigal is distributed as a Python package, so you
  can add it as a dependency to your project, and stop worrying about the
  Prodigal binary being present on the end-user machine.
- **no intermediate files**: Everything happens in memory, in a Python object
  you fully control, so you don't have to invoke the Prodigal CLI using a
  sub-process and temporary files. Sequences can be passed directly as
  strings or bytes, which avoids the overhead of formatting your input to
  FASTA for Prodigal.
- **lower memory usage**: Pyrodigal is slightly more conservative when it comes
  to using memory, which can help process very large sequences. It also lets
  you save some more memory when running several *meta*-mode analyses
- **better performance**: Pyrodigal uses *SIMD* instructions to compute which
  dynamic programming nodes can be ignored when scoring connections. This can
  save from a third to half the runtime depending on the sequence. The 
  `Benchmarks <https://pyrodigal.readthedocs.io/en/stable/benchmarks.html>`_ 
  page of the documentation contains comprehensive comparisons. See the 
  `JOSS paper <https://doi.org/10.21105/joss.04296>`_ for details about how 
  this is achieved.
- **same results**: Pyrodigal is tested to make sure it produces 
  exactly the same results as Prodigal ``v2.6.3+31b300a``. This was verified 
  extensively by `Julian Hahnfeld <https://github.com/jhahnfeld>`_ and can be 
  checked with his `comparison repository <https://github.com/jhahnfeld/prodigal-pyrodigal-comparison>`_.


Features
--------

The library now features everything from the original Prodigal CLI:

- **run mode selection**: Choose between *single* mode, using a training
  sequence to count nucleotide hexamers, or *metagenomic* mode, using
  pre-trained data from different organisms (``prodigal -p``).
- **region masking**: Prevent genes from being predicted across regions
  containing unknown nucleotides  (``prodigal -m``).
- **closed ends**: Genes will be identified as running over edges if they
  are larger than a certain size, but this can be disabled (``prodigal -c``).
- **training configuration**: During the training process, a custom
  translation table can be given (``prodigal -g``), and the Shine-Dalgarno motif
  search can be forcefully bypassed (``prodigal -n``)
- **output files**: Output files can be written in a format mostly
  compatible with the Prodigal binary, including the protein translations
  in FASTA format (``prodigal -a``), the gene sequences in FASTA format
  (``prodigal -d``), or the potential gene scores in tabular format
  (``prodigal -s``).
- **training data persistence**: Getting training data from a sequence and
  using it for other sequences is supported; in addition, a training data
  file can be saved and loaded transparently (``prodigal -t``).

In addition, the **new** features are available:

- **custom gene size threshold**: While Prodigal uses a minimum gene size
  of 90 nucleotides (60 if on edge), Pyrodigal allows to customize this
  threshold, allowing for smaller ORFs to be identified if needed.

Several changes were done regarding **memory management**:

- **digitized sequences**: Sequences are stored as raw bytes instead of compressed 
  bitmaps. This means that the sequence itself takes 3/8th more space, but since 
  the memory used for storing the sequence is often negligible compared to the 
  memory used to store dynamic programming nodes, this is an acceptable 
  trade-off for better performance when extracting said nodes.
- **node buffer growth**: Node arrays are dynamically allocated and grow 
  exponentially instead of being pre-allocated with a large size. On small 
  sequences, this leads to Pyrodigal using about 30% less memory.
- **lightweight genes**: Genes are stored in a more compact data structure than in 
  Prodigal (which reserves a buffer to store string data), saving around 1KiB 
  per gene.


Setup
-----

Run ``pip install pyrodigal`` in a shell to download the latest release and all
its dependencies from PyPi, or have a look at the
:doc:`Installation page <install>` to find other ways to install ``pyrodigal``.


Citation
--------

Pyrodigal is scientific software, with a
`published paper <https://doi.org/10.21105/joss.04296>`_
in the `Journal of Open-Source Software <https://joss.theoj.org/>`_. Check the 
:doc:`Publications page <publications>` to see how to cite Pyrodigal properly.


Library
-------

.. toctree::
   :maxdepth: 2

   Installation <install>
   Output Formats <outputs>
   Contributing <contributing>
   Publications <publications>
   Benchmarks <benchmarks>
   API Reference <api/index>
   Changelog <changes>


License
-------

This library is provided under the `GNU General Public License v3.0 <https://choosealicense.com/licenses/gpl-3.0/>`_.
The Prodigal code was written by `Doug Hyatt <https://github.com/hyattpd>`_ and is distributed under the
terms of the GPLv3 as well. The ``cpu_features`` library was written by
`Guillaume Chatelet <https://github.com/gchatelet>`_ and is licensed under the terms of the
`Apache License 2.0 <https://choosealicense.com/licenses/apache-2.0/>`_.

*This project is in no way not affiliated, sponsored, or otherwise endorsed by
the original* `Prodigal`_ *authors. It was developed by* `Martin Larralde <https://github.com/althonos>`_ *during his
PhD project at the* `European Molecular Biology Laboratory <https://www.embl.de/>`_
*in the* `Zeller team <https://github.com/zellerlab>`_.
