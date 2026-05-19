import pathlib

p = pathlib.Path('/usr/local/lib/python3.7/site-packages/seqann/models/reference_data.py')
src = p.read_text()

# Fix 1: Update feature service URL
src2 = pathlib.Path('/usr/local/lib/python3.7/site-packages/seqann/gfe.py').read_text()
old2 = 'def __init__(self, url="http://feature.nmdp-bioinformatics.org"'
new2 = 'def __init__(self, url="https://feature.b12x.org"'
assert old2 in src2, "gfe.py URL pattern not found"
pathlib.Path('/usr/local/lib/python3.7/site-packages/seqann/gfe.py').write_text(src2.replace(old2, new2))
print("Patched gfe.py URL successfully")

# Fix 2: TypeError in gfe.py error logging
src3 = pathlib.Path('/usr/local/lib/python3.7/site-packages/seqann/gfe.py').read_text()
old3 = 'self.logger.error(self.logname + "Exception when calling DefaultApi->create_feature %e" + e)'
new3 = 'self.logger.error(self.logname + "Exception when calling DefaultApi->create_feature %s" % str(e))'
assert old3 in src3, "gfe.py logging pattern not found"
pathlib.Path('/usr/local/lib/python3.7/site-packages/seqann/gfe.py').write_text(src3.replace(old3, new3))
print("Patched gfe.py logging successfully")

# Fix 3: hla.dat zip fallback in reference_data.py
old = "def download_dat(url, dat):\n    urllib.request.urlretrieve(url, dat)"
new = """def download_dat(url, dat):
    import io, zipfile
    try:
        urllib.request.urlretrieve(url, dat)
    except Exception:
        zip_url = url.rsplit('.dat', 1)[0] + '.dat.zip'
        with urllib.request.urlopen(zip_url) as r:
            zf = zipfile.ZipFile(io.BytesIO(r.read()))
            name = next(n for n in zf.namelist() if n.endswith('.dat'))
            with open(dat, 'wb') as f:
                f.write(zf.read(name))"""

assert old in src, "Pattern not found - seqann may have changed"
p.write_text(src.replace(old, new))
print("Patched successfully")
