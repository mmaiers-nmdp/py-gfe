FROM python:3.7
MAINTAINER NMDP Bioinformatics

RUN apt-get update -q \
    && apt-get install clustalo -y \
	  && apt-get install ncbi-blast+ -y \
    && apt-get autoremove \
    && apt-get clean

COPY seq-ann /opt/seq-ann
RUN pip install --no-cache-dir /opt/seq-ann
COPY py-gfe/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
COPY py-gfe /opt/py-gfe
RUN pip install --no-cache-dir /opt/py-gfe


ENV BIOSQLHOST=imgt_biosqldb
ENV BIOSQLPORT=3306
ENV BIOSQLDB=bioseqdb
ENV BIOSQLUSER=root
ENV BIOSQLPASS=my-secret-pw
