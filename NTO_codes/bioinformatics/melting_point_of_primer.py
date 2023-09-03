def calculate_tm(pSeq):
    pSeq = pSeq.lower()
    w = pSeq.count('a')
    x = pSeq.count('t')
    y = pSeq.count('g')
    z = pSeq.count('c')
    return round(64.9 + 41 * (y + z - 16.4) / (w + x + y + z))

print(calculate_tm('ATGGCAGGCACACGATACAGG'))
print(calculate_tm('ATGCCAATGGGTCCAGCTTTA'))
