gd7=open("input/ANNoutput_Gd7","r")
gd7=open(gd7.readline(),"r")
toll9=open("input/ANNoutput_Toll9","r")
toll9=open(toll9.readline(),"r")
toll10b=open("input/ANNoutput_Toll10b","r")
toll10b=open(toll10b.readline(),"r")

d={}

chr2L=open("output/chr2L.txt","w")
chr2R=open("output/chr2R.txt","w")
chr3L=open("output/chr3L.txt","w")
chr3R=open("output/chr3R.txt","w")
chr4=open("output/chr4.txt","w")
chrX=open("output/chrX.txt","w")
chrY=open("output/chrY.txt","w")

def convert_list_to_string(org_list, seperator=' '):
    """ Convert list to string, by joining all item in list with given separator.
        Returns the concatenated string """
    return seperator.join(org_list)


for line in gd7.readlines():
	line=line.strip("\n").split("\t")
	d[convert_list_to_string([line[0],line[1]], ' ')]=[line[1]]
	d[convert_list_to_string([line[0],line[1]], ' ')].append(line[2])

for lone in toll9.readlines():
	lone=lone.strip("\n").split("\t")
	d[convert_list_to_string([lone[0],lone[1]], ' ')].append(lone[2])

for lune in toll10b.readlines():
	lune=lune.strip("\n").split("\t")
	d[convert_list_to_string([lune[0],lune[1]], ' ')].append(lune[2])

for key in d.keys():
	chrom=key.split(" ")[0]
	if chrom == "chr2L":
		chr2L.write(f'{chrom}\t{convert_list_to_string(d[key],"	")}\n')
	if chrom == "chr2R":
		chr2R.write(f'{chrom}\t{convert_list_to_string(d[key],"	")}\n')
	if chrom == "chr3L":
		chr3L.write(f'{chrom}\t{convert_list_to_string(d[key],"	")}\n')
	if chrom == "chr3R":
		chr3R.write(f'{chrom}\t{convert_list_to_string(d[key],"	")}\n')
	if chrom == "chr4":
		chr4.write(f'{chrom}\t{convert_list_to_string(d[key],"	")}\n')
	if chrom == "chrX":
		chrX.write(f'{chrom}\t{convert_list_to_string(d[key],"	")}\n')
	if chrom == "chrY":
		chrY.write(f'{chrom}\t{convert_list_to_string(d[key],"	")}\n')