from loading import load_directory
from kmers import echantillonage
import numpy as np
import pandas as pd

def jaccard_echantillon(fileA, fileB, k,s):

    i = j = U = I = 0

    l1 = sorted([-x for x in  echantillonage(fileA,k,s)])
    l2 = sorted([-x for x in  echantillonage(fileB,k,s)])

    while i<len(l1) and j<len(l2):
        if l1[i] == l2[j]: 
            i+=1
            j+=1
            U+=1
            I+=1
        else :
            U+=1
            if l1[i] < l2[j]:
                i+=1    
            else :
                j+=1
    
    return I/U

if __name__ == "__main__":
    # Load all the files in a dictionary
    files = load_directory("data")
    k = 21

    filenames = list(files.keys())
    
    jac = np.ones((5,5))

    for i in range(len(files)):
        for j in range(i+1, len(files)):
        
            jac_val = jaccard_echantillon(files[filenames[i]], files[filenames[j]], k,10000)
            jac[i,j]  = jac_val
            jac[j,i] = jac_val

            print(filenames[i], filenames[j], jac)

    jac_df = pd.DataFrame(jac, index = filenames, columns = filenames)
    jac_df.to_csv("jaccard.csv")
