def html_colour_ratio(code, ratio=0.66):
    code = code.strip('# ').strip()
    assert(len(code) == 6), f'Not an HTML code "{code}"?'
    c = [ 0, 0, 0 ]
    c[0] = int(code[0:2], 16)
    c[1] = int(code[2:4], 16)
    c[2] = int(code[4:6], 16)

    c = list(map(lambda i: int(i * ratio), c))

    return f'#{c[0]:02x}{c[1]:02x}{c[2]:02x}'
