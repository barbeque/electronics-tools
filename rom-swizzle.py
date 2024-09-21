# ROM swizzle joins two 8-bit ROM files together (L) and (H) into a 16-bit ROM file that can be understood better

import sys

OUTFILE = '16bit.bin'

if len(sys.argv) < 3:
    print(f'Usage: {sys.argv[0]} [rom low] [rom high]')
    sys.exit(1)

with open(sys.argv[1], 'rb') as l:
    lo = bytes(l.read())

with open(sys.argv[2], 'rb') as h:
    hi = bytes(h.read())

if len(lo) != len(hi):
    print(f'Lengths of low ({len(lo)} bytes) and high ({len(hi)}) roms differ. Please recheck your dump.')
    sys.exit(2)

output = bytearray(b'\0' * (len(lo) + len(hi)))
assert(len(output) == len(lo) + len(hi))

for i in range(len(lo)):
    # TODO: make endian configurable
    output[i * 2] = lo[i]
    output[i * 2 + 1] = hi[i]

with open(OUTFILE, 'wb') as o:
    o.write(output)

print(f'Wrote {len(output)} bytes to {OUTFILE}')