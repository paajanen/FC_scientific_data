#!/usr/bin/env python
import re
import string
import sys


cov=int(sys.argv[1])
ident=int(sys.argv[2])

with open('/path/to/mapped.filtered1.sorted.gtf', 'r') as gene_models: #We take blast hits with filtering
    with open('/path/to/mapped.filtered1.sorted.95.gtf', 'w') as filtered: #We take blast hits with filtering
        coverage=[]
        coverage=[]
        identity=[]
        good_cov=0
        good_identity=0
        all_good=0
        for line in gene_models:
            fields=string.split(string.strip(line))
            if fields[2]=="transcript":
                if  fields[12]=='MD':
                    continue
                    print fields[13][1:-2]
                    print fields[27][1:-2]
                else:
                    coverage.append(fields[13])
                    identity.append(fields[27])
                    if float(fields[13][1:-2])<10:
                        good_cov+=1
                    if fields[27][1:-2]=='M' or fields[27][1:-2]=='UT':
                        continue
                    if float(fields[27][1:-2])<10:
                        good_identity+=1
                    if float(fields[13][1:-2])>cov and float(fields[27][1:-2])>ident:
                        all_good+=1
                        filtered.write(line)
                    
                    
        gene_quality=dict(zip(coverage,identity))
    
        print len(coverage)
        print good_cov
        print good_identity
        print all_good
        
 