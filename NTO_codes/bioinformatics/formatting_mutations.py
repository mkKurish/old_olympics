def formating(row):
    if row[0] != '#':
        row = row.split()
        return('chr'+row[0]+':'+row[1]+' '+row[3]+'/'+row[4])
    else:
        return('False')
    
print(formating('##fileformat=VCFv4.2'))
print(formating('#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	NA00001	NA00002	NA00003'))
print(formating('20	14370	rs6054257	G	A	29	PASS	NS=3;DP=14;AF=0.5;DB;H2	GT:GQ:DP:HQ	0|0:48:1:51,51	1|0:48:8:51,51	1/1:43:51:51'))
print(formating('5	112151205	-	G	.'))
