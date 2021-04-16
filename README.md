# ChiCaP
Pipeline takes bam files from matched germline and somatic cancer patient samples, performs annotation, filtering and merging. 
Further, it flags variants within the merged vcf file into "Germline" or "Somatic". 
The program will be used to improve analysis of germline variants leading to Childhood Cancer Predisposition (ChiCaP), by including information from somatic tumor analyses.

# run_chicap.sh
Script that uses as input a bam file from blood (Germline) and one from the tumor (Somatic) from a patient for variant calling, merging and analysis of germline variants
Run with $1 as germline and $2 as somatic (sbatch run_chicap.sh $1 $2 where $1 and $2 are bam files from illumina WGS results)
