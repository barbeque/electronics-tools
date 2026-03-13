import os, sys

if len(sys.argv) < 2:
    print(f'Usage: {sys.argv[0]} [rom]')
    sys.exit(1)

with open(sys.argv[1], 'rb') as f:
    rom = bytes(f.read())

def decode_mapper(mapper):
    match mapper:
        case 0:
            return "Nintendo NROM"
        case 1:
            return "Nintendo MMC1"
        case 2:
            return "Nintendo UxROM"
        case 4:
            return "Nintendo MMC3"
        case 10:
            return "Nintendo MMC4"
        case 25:
            return "Konami VRC4"
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
