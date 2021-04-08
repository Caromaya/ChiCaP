#!/bin/bash -l
#SBATCH -A sens2020021
#SBATCH -p core
#SBATCH -n 1
#SBATCH -t 1-00:00:00
#SBATCH -J TIDDIT

module load bionfo-tools freebayes vep bcftools

freebayes -f human_g1k_v37.fasta RMNISTHS_30xdownsample.nsort.bwa-mem.sorted.nonDupRead.rg.bam >RMNISTHS_30xdownsample.nsort.bwa-mem.sorted.nonDupRead.vcf

#bgzip $1
#tabix -p vcf $1.gz

#vcf-merge inbox/F0013698_sorted_md_brecal_haptc_vrecal_comb_BOTH.vcf.sort.vcf.kg_intersect.vcf.gz turkisk_bakgrund/TGP.integrated_callset.vcf.gz.sort.vcf.kg_intersect.vcf.gz > merge_background_F0013698.vcf

