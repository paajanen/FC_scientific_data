#!/usr/bin/env python

import string
import sys
import re





infile=open('falcon_assembly.fasta','r')
outfile=open('falcon_assembly_renamed.fasta','w')


for aline in infile:
    if aline[0]=='>':
        b=string.split(aline)
        outfile.write('{0}\n'.format(b[0]))
    else:
        outfile.write(aline)
        
infile.close()
outfile.close()    
