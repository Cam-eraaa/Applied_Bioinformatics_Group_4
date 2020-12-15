peaks=open("input/H3K27ac.peak.QC.tab.txt","r")
peaks=open(peaks.readline(),"r")
counts=open("input/H3K27ac.counts.QC.tab.txt","r")
counts=open(counts.readline(),"r")
next(counts)
next(peaks)

# First we make lists with the information that we want from the three mutants
l_counts10b=[]
l_counts9=[]
l_counts7=[]
l_positions=[]
for line in counts.readlines():
	line=line.strip("\n").split("\t")
	# For Toll10b
	l_counts10b.append([line[0],int(line[1])+int(line[3])])
	# For Toll9
	l_counts9.append([line[0],int(line[2])+int(line[6])])
	# For Gd7
	l_counts7.append([line[0],int(line[4])+int(line[5])])
for line in peaks.readlines():
	line=line.strip("\n").split("\t")
	l_positions.append([line[0],line[1],line[2],line[3]])

# Now we will summarize both the lists in a bedgraph file for each mutant

H3K27ac_Toll10b=open("output/H3K27ac_Toll10b.bedGraph","w")
H3K27ac_Toll10b.write('track type=bedGraph name="H3K27ac_Toll10b" description="H3K27ac_Toll10b"\n')
H3K27ac_Toll9=open("output/H3K27ac_Toll9.bedGraph","w")
H3K27ac_Toll9.write('track type=bedGraph name="H3K27ac_Toll9" description="H3K27ac_Toll9"\n')
H3K27ac_Gd7=open("output/H3K27ac_Gd7.bedGraph","w")
H3K27ac_Gd7.write('track type=bedGraph name="H3K27ac_Gd7" description="H3K27ac_Gd7"\n')
for i in l_positions:
	# For Toll10b
	for j in l_counts10b:
		if i[0]==j[0]:
			H3K27ac_Toll10b.write(f'{i[1]}\t{i[2]}\t{i[3]}\t{j[1]}\n')
	# For Toll9
	for k in l_counts9:
		if i[0]==k[0]:
			H3K27ac_Toll9.write(f'{i[1]}\t{i[2]}\t{i[3]}\t{k[1]}\n')
	# For Gd7
	for l in l_counts7:
		if i[0]==l[0]:
			H3K27ac_Gd7.write(f'{i[1]}\t{i[2]}\t{i[3]}\t{l[1]}\n')

