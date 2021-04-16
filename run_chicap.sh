#!/bin/bash -l
#SBATCH -A sens2020021
#SBATCH -p core
#SBATCH -n 10
#SBATCH -t 4-00:00:00
#SBATCH -J ChiCaP_merge

##Script for variant calling from bam files, and merging of germline and somatic variants
##Run with $1 as germline bam file and $2 as somatic bam file (sbatch run_chicap.sh $1 $2)  

echo $1 $2

module load bioinfo-tools freebayes vep bcftools tabix

reference="/proj/sens2020021/nobackup/carolina/human_g1k_v37.fasta"
genelist="/proj/sens2020021/nobackup/carolina/20mar21_Somatic_matched_Germline/genelist.txt"
filter="/proj/sens2020021/nobackup/carolina/ChiCaP/filter_vcf.py"

freebayes -f $reference $1 >$1.vcf
freebayes -f $reference $2 >$2.vcf

vep --cache --dir_cache $VEP_CACHE -i $1.vcf --symbol --vcf --assembly GRCh37 --offline -o $1.vep.vcf
vep --cache --dir_cache $VEP_CACHE -i $2.vcf --symbol --vcf --assembly GRCh37 --offline -o $2.vep.vcf

filter_vep -i $1.vep.vcf --format vcf -o $1.chicap_filtered.vcf  --filter "(SYMBOL in $genelist) and (IMPACT is HIGH or IMPACT is MODERATE) and (AFR_AF < 0.1 or EUR_AF < 0.1)"

filter_vep -i $2.vep.vcf --format vcf -o $2.chicap_filtered.vcf  --filter "(SYMBOL in $genelist) and (IMPACT is HIGH or IMPACT is MODERATE) and (AFR_AF < 0.1 or EUR_AF < 0.1)"

python $filter $1.chicap_filtered.vcf >$1.filtered.vcf
python $filter $2.chicap_filtered.vcf >$2.filtered.vcf

bgzip $1.filtered.vcf
bgzip $2.filtered.vcf

tabix -p vcf $1.filtered.vcf.gz
tabix -p vcf $2.filtered.vcf.gz

bcftools merge $1.filtered.vcf.gz $2.filtered.vcf.gz > $1.merge.vcf


