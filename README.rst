===============================
py-gfe
===============================


.. image:: https://img.shields.io/pypi/v/pygfe.svg
        :target: https://pypi.python.org/pypi/pygfe

.. image:: https://img.shields.io/travis/mhalagan-nmdp/pygfe.svg
        :target: https://travis-ci.org/mhalagan-nmdp/pygfe

.. image:: https://readthedocs.org/projects/pygfe/badge/?version=latest
        :target: https://pygfe.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/mhalagan-nmdp/pygfe/shield.svg
     :target: https://pyup.io/repos/github/mhalagan-nmdp/pygfe/
     :alt: Updates


Overview
--------

**py-gfe** is a Python package for converting sequence annotations to **Gene Feature Enumerations (GFE)**, particularly for HLA (Human Leukocyte Antigen) loci. It's developed by the NMDP (National Marrow Donor Program) Bioinformatics team.

Core Features
~~~~~~~~~~~~~

* **GFE Generation**: Converts biological sequence annotations into standardized GFE identifiers (e.g., ``HLA-DQB1w0-4-0-141-0-12-0-4-0-0-0-0-0``)
* **Sequence Annotation**: Works with both genomic and protein sequences
* **Multiple HLA Loci Support**: Handles HLA-A, HLA-B, HLA-C, HLA-DRB1, HLA-DQB1, HLA-DRB4, HLA-DRB5, HLA-DPB1, HLA-DPA1, HLA-DQA1, HLA-DRB3, and KIR loci
* **Feature Extraction**: Identifies genomic features like exons, introns, and UTRs
* **Multiple Annotation Sources**: Supports seqann for local annotation

Key Components
~~~~~~~~~~~~~~

* **pygfe module**: Core GFE conversion logic with Neo4j graph database integration
* **feature_client**: REST API client for feature service queries
* **seq2gfe**: Command-line tool for converting FASTA sequences to GFE

* Free software: LGPL 3.0
* Documentation: https://pygfe.readthedocs.io.

Docker
--------

.. code-block:: shell

  docker pull nmdpbioinformatics/py-gfe

.. code-block:: 

	docker run -it --rm -v $PWD:/opt nmdpbioinformatics/py-gfe seq2gfe \
		-f /opt/your_fastafile.fasta -l HLA-A


Example
--------

.. code-block:: python3

    >>> from Bio import SeqIO
    >>> from BioSQL import BioSeqDatabase
    >>> from seqann.sequence_annotation import BioSeqAnn
    >>> import pygfe
    >>> seq_file = 'test_dq.fasta'
    >>> gfe = pygfe.pyGFE()
    >>> server = BioSeqDatabase.open_database(driver="pymysql", user="root",
    ...                                       passwd="", host="localhost",
    ...                                      db="bioseqdb")
    >>> seqann = BioSeqAnn(server=server)
    >>> seq_rec = list(SeqIO.parse(seq_file, 'fasta'))[0]
    >>> annotation = seqann.annotate(seq_rec, "HLA-DQB1")
    >>> gfe = gfe.get_gfe(annotation, "HLA-DQB1")
    >>> print(gfe)
    HLA-DQB1w0-4-0-141-0-12-0-4-0-0-0-0-0

