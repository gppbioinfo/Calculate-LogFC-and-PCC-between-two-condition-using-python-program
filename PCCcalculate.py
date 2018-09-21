'''This program calculate the logFC and Pearson correlation coefficient (PCC) 
'  using normalized expression score of mRNAs/miRNAs between two conditions.
'''

import numpy as np
import sys
import csv
import math as mt


with open(sys.argv[1], 'r') as f:
    lines = list(csv.reader(f, delimiter='\t'))
    #print(wines[2])

    for j in lines:
      col = len(j)
      if col > 2 and col != 6:

        G1=np.array([j[5],j[6]]).astype(np.float)
        G2=np.array([j[8],j[9]]).astype(np.float)
        #print (aa[6])
        cor=np.corrcoef([G1,G2])[0,1]
        m1=np.mean(G1)
        m2=np.mean(G2)
        div=m1/m2
        lfc=np.log2(div)
        #print ("%s\t%s" % (G1,G2))
        #print ("%s\t%f\t%f" % (j,lfc,cor))
        #print (j[7])
        #if cor <= -0.05 and float(j[7]) <= lfc:
        if cor <= -0.05 and float(j[7]) >= lfc:
          j.append(np.array2string(lfc, precision=3, separator='\t', suppress_small=True))
          j.append(np.array2string(cor,formatter={'float_kind':lambda cor: "%.2f" % cor}))
          print('\t'.join(j))
      
      
