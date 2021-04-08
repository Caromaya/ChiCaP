import sys

#run like this:
#python filter_second_hit.py merged_file.vcf

#sys.argv[1] (i.e the first argument) is now input.vcf 
input_vcf=sys.argv[1] 

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

	if "./.:." in content[-2]:
		in_germline=False
	else :
		in_germline=True

	if "./.:." in content[-1]:
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

	

print (len(germline))
print ("\n")
print (len(somatic))
print ("\n")
print (len(somatic.intersection(germline)))

print (sorted(germline))

