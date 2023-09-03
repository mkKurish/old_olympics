def check_primer(primerSeq, minGC=50, maxGC=60, minPrimerLen=18, maxPrimerLen=25):
    primerSeq = primerSeq.lower()
    gc = (primerSeq.count('g') + primerSeq.count('c'))*100/len(primerSeq)
    lengthSeq = len(primerSeq)
    return (lengthSeq<=maxPrimerLen and lengthSeq>=minPrimerLen and
            gc<=maxGC and gc>=minGC)

print(check_primer('ATGGCAGGCACACGATACAGG'))
print(check_primer('CCAGCATATGACAGGCACAGTTGC', 55, 65, 20, 25))
print(check_primer('CGTATGCAGCAGTATAGGGCAGCCCAC', 52, 62, 20))
print(check_primer('cgtatgcatcagtataggcaatcc', 40, 60, 20, 30))
