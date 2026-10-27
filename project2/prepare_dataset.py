"""Restore the exact original sampled CSV stored as three compressed Git blobs.

The archive is intentionally split into transport-friendly parts. No network,
API key, or separate QIAIP installation is needed. Standard library only.
"""
from pathlib import Path
import hashlib
import lzma

ROOT = Path(__file__).resolve().parent
DEST = ROOT / 'metropt3_compressor_sample.csv'
PARTS = sorted((ROOT / 'data_parts').glob('metropt3.csv.xz.part*'))
EXPECTED_PARTS = 3
EXPECTED_COMPRESSED = '6542028b7ce3880b3bcfc5985448de360689de47a6d58afc1f6117aeb12b4a0d'
EXPECTED_CSV = '2281e4ad5b677a233c1246ad418e63795ee33d0d2772543ec46455e043de7167'

if len(PARTS) != EXPECTED_PARTS:
    raise SystemExit(f'Expected {EXPECTED_PARTS} compressed source pieces; found {len(PARTS)}.')
compressed = b''.join(p.read_bytes() for p in PARTS)
assert hashlib.sha256(compressed).hexdigest() == EXPECTED_COMPRESSED, 'Compressed source checksum mismatch'
data = lzma.decompress(compressed)
assert hashlib.sha256(data).hexdigest() == EXPECTED_CSV, 'Restored CSV checksum mismatch'
DEST.write_bytes(data)
print(f'Restored {DEST} ({len(data)} bytes); SHA256 verified')
