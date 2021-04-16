import sys

#run like this:
#python filter_vcf.py input.vcf > output.vcf
# 
#sys.argv[1] (i.e the first argument) is now input.vcf (the vcf you want to filter)
input_vcf=sys.argv[1] 

#minimum phredd score
min_qual=10

#minimum coverage
min_dp=10

#maximium_coverage
max_dp=200



#minimum fraction of reads supporting the event
min_fraction=0.1

#minimum reads supporting the event
min_support=4

for line in open(input_vcf):

	if line[0] == "#":
		#print header, then continue to next line
		print(line.strip())
		continue

	content=line.split("\t")

	#if poor quality, continue to next line
	quality=float(content[5])
	if quality < min_qual:
		continue

	DP=int(content[-1].split(":")[1])

	#continue if abnormal coverage
	if DP < min_dp:
		continue
	if DP > max_dp:
		continue
	
	#this is only printed if it passed the quality checked
	print(line.strip())
