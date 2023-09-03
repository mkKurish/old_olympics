def is_self_compliment(pSeq, maxNucNum):
    pSeq = pSeq.lower()
    if maxNucNum <= len(pSeq):
        cutSeq = pSeq[len(pSeq)-maxNucNum:]
    else:
        cutSeq = pSeq
    cutSeq = cutSeq.replace('a', 'T')
    cutSeq = cutSeq.replace('t', 'A')
    cutSeq = cutSeq.replace('g', 'C')
    cutSeq = cutSeq.replace('c', 'G')
    cutSeq = cutSeq.lower()
    cutSeq = cutSeq[::-1]
    return cutSeq in pSeq

print(is_self_compliment('ATGGCAGCCCACACGATACAGGG', 3))
print(is_self_compliment('ACACTAACGACCGTATCGA', 4))
print(is_self_compliment('GATTTGTAACTTCCTTTTTTCGC', 4))
