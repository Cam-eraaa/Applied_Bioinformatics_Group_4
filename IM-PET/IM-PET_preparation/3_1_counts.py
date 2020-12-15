CDS=open("input/counts.CDS.txt","r")
CDS=open(CDS.readline(),"r")
QC=open("input/counts.QC.tab.txt","r")
QC=open(QC.readline(),"r")
next(CDS)
next(CDS)

l_CDS=[]
for line in CDS.readlines():
	line=line.strip("\n").split("\t")
	l_CDS.append([line[0],line[5]])

counts=open("output/counts.txt","w")
counts.write("length	gd7_3h	gd7_5h	toll10b_3h_rep	toll10b_5h_rep	toll9_3h_r	toll9_5h_r\n")
for line in QC.readlines():
	line=line.strip("\n").split("\t")
	for i in l_CDS:
		if i[0]==line[0]:
			# counts.write(f'{line[0]}\t{i[1]}\t{line[1]}\t{line[2]}\t{line[3]}\t{line[4]}\t{line[5]}\t{line[6]}\t{line[7]}\t{line[8]}\t{line[9]}\t{line[10]}\t{line[11]}\t{line[12]}\n')
			counts.write(f'{line[0]}\t{i[1]}\t{int(line[1])+int(line[2])}\t{int(line[3])+int(line[4])}\t{int(line[5])+int(line[6])}\t{int(line[7])+int(line[8])}\t{int(line[9])+int(line[10])}\t{int(line[11])+int(line[12])}\n')