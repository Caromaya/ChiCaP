import sys

#run like this:
#python filter_second_hit.py merged_file.vcf

#sys.argv[1] (i.e the first argument) is now input.vcf 
input_vcf=sys.argv[1]
output_gene_list= input_vcf + ".genelist.txt"
output_vcf=input_vcf + ".flagged.vcf"

#You can add things only once into a set (Repeated elements become one)
germline=set([])
somatic=set([])

#We extract the gene names from the merged vcf file
gene=False

for line in open(input_vcf):

	if line[0] == "#":
		continue
	
	#Split by tabs
	content=line.split("\t")
	
	#We check if germline
	content[-2] 

	if ("./.:." in content[-2]) or ("0/0" in content[-2]):
		in_germline=False
	else :
		in_germline=True

	if ("./.:." in content[-1]) or ("0/0" in content[-1]):
		in_somatic=False
	else :
		in_somatic=True

	if in_germline and in_somatic:
		transcripts = line.split("CSQ=")[-1].split(";")[0].split()[0].split(",")
		
		for transcript in transcripts:
			germline.add(transcript.split("|")[3])

	if not in_germline and in_somatic:
                transcripts = line.split("CSQ=")[-1].split(";")[0].split()[0].split(",")

		for transcript in transcripts:
                        somatic.add(transcript.split("|")[3])

	if in_germline and not in_somatic:
                transcripts = line.split("CSQ=")[-1].split(";")[0].split()[0].split(",")
		
		for transcript in transcripts:
                        germline.add(transcript.split("|")[3])

#Gene List for Excel

genelist=""
secondhit = somatic.intersection(germline)
gene_list_file = open (output_gene_list,"w")

for ele in sorted(secondhit): 
        genelist += ele + "\n"

gene_list_file.write(genelist)
gene_list_file.close()


output_vcf_file = open (output_vcf,"w")
for line in open(input_vcf):

	if line[0] == "#":
		output_vcf_file.write(line)
		continue

        #Split by tabs
	content=line.split("\t")

        #We check if germline
        #content[-2]
	if ("./.:." in content[-2]) or ("0/0" in content[-2]):
		in_germline=False
	else :
		in_germline=True

	if ("./.:." in content[-1]) or ("0/0" in content[-1]):
		in_somatic=False
	else :
		in_somatic=True

	germline_flag=";GERMLINE=FALSE"
	somatic_flag=";SOMATIC=FALSE"

	if in_germline:
		germline_flag=";GERMLINE=TRUE"	
	elif in_somatic:
		somatic_flag=";SOMATIC=TRUE"	

		
	transcripts = line.split("CSQ=")[-1].split(";")[0].split()[0].split(",")
	secondhit_flag=";SECONDHIT=FALSE"
	
	for transcript in transcripts:
		gene=transcript.split("|")[3]
		if gene in secondhit:
			secondhit_flag=secondhit_flag.replace("FALSE","TRUE")
			#secondhit_flag+="|"+gene
			#secondhit_flag=gene + ":TRUE"
#		else :
#			secondhit_flag=gene + ":FALSE"

	content[7]+=germline_flag+somatic_flag+secondhit_flag
	output_vcf_file.write("\t".join(content))

output_vcf_file.close()
