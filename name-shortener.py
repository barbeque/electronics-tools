"""
Name shortener
Copy files into another directory, truncating their names
if the filename (and extension) are too long.

Used for PiColeco but probably useful for lots of other stuff too
"""

import sys
import os
import glob
import shutil
from pathlib import Path

EXTENSION = '*.col' # colecovision
MAX_LENGTH = 32 # includes extension

if len(sys.argv) < 3:
    print(f'Usage: {sys.argv[0]} [indir] [outdir]')
    sys.exit(1)

in_dir = sys.argv[1]

if not Path(in_dir).is_dir():
    print(f'In-dir is not actually a directory, try again')
    sys.exit(2)

out_dir = sys.argv[2]
if os.path.exists(out_dir):
    print(f'Out-dir "{out_dir}" already exists, aborting')
    sys.exit(3)

def shortened(long_filename):
    (root, ext) = os.path.splitext(long_filename)
    max_length = MAX_LENGTH - len(ext)
    short_root = root[:max_length]
    return short_root + ext

# make the directory
os.mkdir(out_dir)

col_files = glob.glob(os.path.join(glob.escape(in_dir), EXTENSION))
for rom in sorted(col_files):
    filename = os.path.basename(rom)
    if len(filename) > MAX_LENGTH:
        filename = shortened(filename)
        assert(len(filename) <= MAX_LENGTH)
    shutil.copyfile(rom, os.path.join(out_dir, filename))
