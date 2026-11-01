"""Losslessly package local outputs; verify every byte before removing duplicate files.
Only operates inside this session's data/ and preflight_data/ directories.
Restore: python -m zipfile -e sessions/S115/LOCAL_EVIDENCE.zip sessions/S115
"""
import hashlib
import json
from pathlib import Path
import zipfile

HERE=Path(__file__).resolve().parent
roots=[(HERE/'data').resolve(),(HERE/'preflight_data').resolve()]
assert all(root.parent==HERE.resolve() for root in roots)
files=sorted(p for root in roots for p in root.rglob('*') if p.is_file())
assert files
for p in files:
    assert any(p.resolve().is_relative_to(root) for root in roots)
entries={str(p.relative_to(HERE)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
archive=HERE/'LOCAL_EVIDENCE.zip'
assert not archive.exists(), 'archive already exists; do not overwrite evidence'
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in files:z.write(p,str(p.relative_to(HERE)).replace('\\','/'))
with zipfile.ZipFile(archive) as z:
    assert set(z.namelist())==set(entries)
    for name,h in entries.items():assert hashlib.sha256(z.read(name)).hexdigest()==h
record={'archive':archive.name,'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'files':entries,
        'original_bytes':sum(p.stat().st_size for p in files),'archive_bytes':archive.stat().st_size,
        'verification':'every archived file byte digest equals original before duplicate removal',
        'restore':'python -m zipfile -e sessions/S115/LOCAL_EVIDENCE.zip sessions/S115'}
(HERE/'ARCHIVE_MANIFEST.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8',newline='\n')
# Each resolved file is checked against explicit session roots, not shell-expanded paths.
for p in files:
    assert any(p.resolve().is_relative_to(root) for root in roots)
    p.unlink()
for root in roots:
    for d in sorted((p for p in root.rglob('*') if p.is_dir()),key=lambda p:len(p.parts),reverse=True):
        assert d.resolve().is_relative_to(root)
        d.rmdir()
    root.rmdir()
print(json.dumps({k:v for k,v in record.items() if k!='files'},indent=2))
