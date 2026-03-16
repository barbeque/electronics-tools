import os, sys

if len(sys.argv) < 2:
    print(f'Usage: {sys.argv[0]} [rom]')
    sys.exit(1)

with open(sys.argv[1], 'rb') as f:
    rom = bytes(f.read())

def decode_mapper(mapper):
    MAPPERS = {
        0: "Nintendo NROM",
        1: "Nintendo MMC1",
        2: "Nintendo UxROM",
        4: "Nintendo MMC3",
        10: "Nintendo MMC4",
        25: "Konami VRC4",
        167: "Subor Educational Computer"
    }
    if mapper in MAPPERS:
        return MAPPERS[mapper]
    else:
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
