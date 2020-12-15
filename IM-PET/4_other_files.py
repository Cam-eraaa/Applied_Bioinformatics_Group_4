CDS=open("input/counts.CDS.txt","r")
CDS=open(CDS.readline(),"r")
gene_expr=open("output/gene_expr.txt","r")

next(CDS)
next(CDS)
next(gene_expr)

i=1
l_CDS=[]
d={}

transcript_Gd7_3h=open("output/transcript_Gd7_3h.gtf","w")
transcript_Gd7_5h=open("output/transcript_Gd7_5h.gtf","w")
transcript_Toll9_3h=open("output/transcript_Toll9_3h.gtf","w")
transcript_Toll9_5h=open("output/transcript_Toll9_5h.gtf","w")
transcript_Toll10b_3h=open("output/transcript_Toll10b_3h.gtf","w")
transcript_Toll10b_5h=open("output/transcript_Toll10b_5h.gtf","w")
hash_txt=open("output/hash.txt","w")
gene=open("output/genes.txt","w")

for line in CDS.readlines():
	line=line.strip("\n").split("\t")
	l_CDS.append([line[0], line[1].split(';')[0], line[2].split(';')[0]])

for lone in gene_expr.readlines():
	lone=lone.strip("\n").split(" ")
	lone[0]=lone[0].replace('"', '')
	for j in l_CDS:
		if j[0]==lone[0]:
			transcript_Gd7_3h.write(f"{i}\tchr{j[1]}\t{j[2]}\t{lone[1]}\t{lone[2]}\t{lone[3]}\t{lone[4]}\t{lone[5]}\t{lone[6]}\n")
			transcript_Gd7_5h.write(f"{i}\tchr{j[1]}\t{j[2]}\t{lone[2]}\t{lone[1]}\t{lone[3]}\t{lone[4]}\t{lone[5]}\t{lone[6]}\n")
			transcript_Toll9_3h.write(f"{i}\tchr{j[1]}\t{j[2]}\t{lone[5]}\t{lone[6]}\t{lone[1]}\t{lone[2]}\t{lone[3]}\t{lone[4]}\n")
			transcript_Toll9_5h.write(f"{i}\tchr{j[1]}\t{j[2]}\t{lone[6]}\t{lone[5]}\t{lone[1]}\t{lone[2]}\t{lone[3]}\t{lone[4]}\n")
			transcript_Toll10b_3h.write(f"{i}\tchr{j[1]}\t{j[2]}\t{lone[3]}\t{lone[4]}\t{lone[1]}\t{lone[2]}\t{lone[5]}\t{lone[6]}\n")
			transcript_Toll10b_5h.write(f"{i}\tchr{j[1]}\t{j[2]}\t{lone[4]}\t{lone[3]}\t{lone[1]}\t{lone[2]}\t{lone[5]}\t{lone[6]}\n")
			gene.write(f'{lone[0]}\n')
			if f'chr{j[1]}' not in d.keys():
				d[f'chr{j[1]}']=[i]
			else:
				d[f'chr{j[1]}'].append(i)
			i+=1

for chrom in d.keys():
	s=' '.join([str(elem) for elem in d[chrom]])
	hash_txt.write(f'{chrom}\n')
	hash_txt.write(f'{s}\n')