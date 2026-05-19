# py-gfe

[![PyPI](https://img.shields.io/pypi/v/py-gfe.svg)](https://pypi.python.org/pypi/py-gfe)
[![Build Status](https://github.com/nmdp-bioinformatics/py-gfe/actions/workflows/build.yml/badge.svg)](https://github.com/nmdp-bioinformatics/py-gfe/actions)
[![Documentation Status](https://readthedocs.org/projects/py-gfe/badge/?version=latest)](https://py-gfe.readthedocs.io/en/latest/?badge=latest)
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)

## Overview

**py-gfe** is a Python package for converting sequence annotations to **Gene Feature Enumerations (GFE)**, particularly for HLA (Human Leukocyte Antigen) loci. It's developed by the NMDP (National Marrow Donor Program) Bioinformatics team.

### Core Features

- **GFE Generation**: Converts biological sequence annotations into standardized GFE identifiers (e.g., `HLA-DQB1w0-4-0-141-0-12-0-4-0-0-0-0-0`)
- **Sequence Annotation**: Works with both genomic and protein sequences
- **Multiple HLA Loci Support**: Handles HLA-A, HLA-B, HLA-C, HLA-DRB1, HLA-DQB1, HLA-DRB4, HLA-DRB5, HLA-DPB1, HLA-DPA1, HLA-DQA1, HLA-DRB3, and KIR loci
- **Feature Extraction**: Identifies genomic features like exons, introns, and UTRs
- **Multiple Annotation Sources**: Supports seqann for local annotation

### Key Components

- **pygfe module**: Core GFE conversion logic with Neo4j graph database integration
- **feature_client**: REST API client for feature service queries
- **seq2gfe**: Command-line tool for converting FASTA sequences to GFE

**Free software:** LGPL 3.0  
**Documentation:** https://pygfe.readthedocs.io

## Docker

Build the image locally:

```bash
docker build -t py-gfe .
```

Run the container:

```bash
docker run -it --rm -v $PWD:/opt py-gfe seq2gfe \
    -f /opt/your_fastafile.fasta -l HLA-A
```

## Example

```python
from Bio import SeqIO
from BioSQL import BioSeqDatabase
from seqann.sequence_annotation import BioSeqAnn
import pygfe

seq_file = 'test_dq.fasta'
gfe = pygfe.pyGFE()
server = BioSeqDatabase.open_database(driver="pymysql", user="root",
                                      passwd="", host="localhost",
                                      db="bioseqdb")
seqann = BioSeqAnn(server=server)
seq_rec = list(SeqIO.parse(seq_file, 'fasta'))[0]
annotation = seqann.annotate(seq_rec, "HLA-DQB1")
gfe = gfe.get_gfe(annotation, "HLA-DQB1")
print(gfe)
# Output: HLA-DQB1w0-4-0-141-0-12-0-4-0-0-0-0-0
```
