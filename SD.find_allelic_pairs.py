#!/usr/bin/env python
import re
import string
import sys



with open('/path/to/mapped.filtered1.sorted.95.gtf', 'r') as gene_models: #We take the filtered annotation
    with open('/path/to/diplo_pairs.txt','r') as diplo_pairs:  #And the allelic pairs
    # We make two dictionaries from the list of allelic pairs, so that we can query it with either allele
    allele1=[]
    allele2=[]
    for line in diplo_pairs:
        fields=string.split(string.strip(line))
        allele1.append(fields[0])
        allele2.append(fields[1])
    pairs1=dict(zip(allele1,allele2))
    pairs2=dict(zip(allele2,allele1))
    
    # We make look at the number of transcripts in the PacBio assembly and create a database that is easier to search
    transcripts=[]
    transcript_names=[]
    for line in gene_models:
        fields=string.split(string.strip(line))
        if fields[2]=="transcript":
            transcripts.append(fields)
            transcript_names.append(fields[9].split('|')[2])
    print 'total genes in PacBio', len(transcripts) #output the number of transcripts gound
    
    both_names=[]
    both_in_pacbio_1=0
    both_in_pacbio_2=0
    not_in_pacbio=0
    for tr in transcript_names:
        if tr  in allele1:
            if pairs1[tr] in transcript_names:
                both_in_pacbio_1+=1
        if tr  in allele2:
            if pairs2[tr] in transcript_names:
                both_in_pacbio_2+=1
                both_names.append([tr,pairs2[tr]])
    print 'of the Sanger alleles in pacbio', both_in_pacbio_1, both_in_pacbio_2
    
    # Find the names of the transcripts that are on the alternate haplotypes and create a list of names
    haplotype_gene_names=[]      
    haplotypes=[]   
    for trans in transcripts:
        if len(trans[0])==21:
            haplotypes.append(trans)
            haplotype_gene_names.append(trans[9].split('|')[2])
    print 'haplotype genes total', len(haplotypes) #Find how many transcripts are found in alternate haplotypes
    
    # Divide the transcripts on the haplotypes to those that were found as allelic pairs in the Sanger assembly and to those that were not
    new_hap_genes=[]
    old_hap_genes=[]
    for hap_gene in haplotype_gene_names:
        if hap_gene not in allele1 and hap_gene not in allele2:
            new_hap_genes.append(hap_gene)
        else:
            old_hap_genes.append(hap_gene)
            
    print 'new alternate alleles',len(new_hap_genes)
    print 'old hap genes', len(old_hap_genes)
    
    #Create a list of the allelic pairs found in both the Sanger and PacBio assemblies
    for old in old_hap_genes:
        if old in pairs1:
            print old,pairs1[old]
        if old in pairs2:
            print old, pairs2[old]
    #Create a list of the new alleles found in the PacBio assembly not classified as allelic pairs in the Sanger assembly
    for new in new_hap_genes:
        print new 
        
            
    
            