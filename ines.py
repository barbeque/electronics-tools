import os, sys

if len(sys.argv) < 2:
    print(f'Usage: {sys.argv[0]} [rom]')
    sys.exit(1)

with open(sys.argv[1], 'rb') as f:
    rom = bytes(f.read())

def decode_mapper(mapper):
    match mapper:
        case 167:
            return "Subor Educational Computer"
        case _:
            return "???"

def dump_ines(rom):
    if rom[0:4] != b'NES\x1a':
       print(f'Invalid ROM header "{ rom[0:4] }", this is not iNES?')
       return

    # TODO: add some other stuff later, if i care
    byte6 = rom[6] # mapper: bits 7..4
    byte7 = rom[7] # mapper: bits 7..4
    mapper = (byte7) | (byte6 >> 4)

    print(f'Mapper: { hex(mapper) } / {mapper} / { decode_mapper(mapper) }')

dump_ines(rom)
