counts=open("input/CBP.CBP.counts.QC.tab.txt","r")
counts=open(counts.readline(),"r")
positions=open("input/CBP-CBP_dm6.featureCount.count.tab.txt","r")
positions=open(positions.readline(),"r")
next(counts)
next(positions)
next(positions)

# First we create 2 lists containing the information we want

## This list is going to contain the information about the region and the sum of the read counts
l_counts10b=[]
l_counts9=[]
l_counts7=[]
# l_countstotal=[]
for line in counts.readlines():
	line=line.strip("\n").split("\t")
	### For Toll10b
	l_counts10b.append([line[0],int(line[1])+int(line[6])])
	### For Toll9
	l_counts9.append([line[0],int(line[2])+int(line[5])])
	### For Gd7
	l_counts7.append([line[0],int(line[3])+int(line[4])])
	### For total
	# l_countstotal.append([line[0],int(line[1])+int(line[2])+int(line[3])+int(line[4])+int(line[5])+int(line[6])])

# This list is going to contain the regions and their positions in the genome
l_positions=[]
for line in positions.readlines():
	line=line.strip("\n").split("\t")
	l_positions.append([line[0],line[1],line[2],line[3]])

# Now we create a file that will summarize both lists that we just created
CBP_Toll10b=open("output/CBP_Toll10b.bedGraph","w")
CBP_Toll10b.write('track type=bedGraph name="CBP_Toll10b" description="CBP_Toll10b"\n')
CBP_Toll9=open("output/CBP_Toll9.bedGraph","w")
CBP_Toll9.write('track type=bedGraph name="CBP_Toll9" description="CBP_Toll9"\n')
CBP_Gd7=open("output/CBP_Gd7.bedGraph","w")
CBP_Gd7.write('track type=bedGraph name="CBP_Gd7" description="CBP_Gd7"\n')
# CBP=open("output/CBP.bedGraph","w")
# CBP.write('track type=bedGraph name="CBP" description="CBP"\n')
for i in l_positions:
	## For Toll10b
	for j in l_counts10b:
		if i[0]==j[0]:
			CBP_Toll10b.write(f'{i[1]}\t{i[2]}\t{i[3]}\t{j[1]}\n')
	## For Toll9
	for k in l_counts9:
		if i[0]==k[0]:
			CBP_Toll9.write(f'{i[1]}\t{i[2]}\t{i[3]}\t{k[1]}\n')
	## For Gd7
	for l in l_counts7:
		if i[0]==l[0]:
			CBP_Gd7.write(f'{i[1]}\t{i[2]}\t{i[3]}\t{l[1]}\n')
	# for m in l_countstotal:
	# 	if i[0]==m[0]:
	# 		CBP.write(f'{i[1]}\t{i[2]}\t{i[3]}\t{m[1]}\n')