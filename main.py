from loading import load_directory
from kmers import stream_kmers, kmer2str
import numpy as np
import pandas as pd

def jaccard(fileA, fileB, k):

    dico = {}
    Taille_U = 0
    Taille_I = 0

    for kmer in stream_kmers(fileA,k):
        dico[kmer] = 1 if kmer not in dico else dico[kmer] + 1
        Taille_U +=1

    for kmer in stream_kmers(fileB,k):
        
        if kmer in dico :

            Taille_I += 1
            dico[kmer]-=1
            if dico[kmer] == 0:
                del dico[kmer]
		
        else:
            Taille_U += 1
          
    return Taille_I/Taille_U


if __name__ == "__main__":
    # Load all the files in a dictionary
    files = load_directory("data")
    k = 21

    filenames = list(files.keys())
    
    jac = np.zeros((5,5))

    for i in range(len(files)):
        for j in range(i+1, len(files)):
        
            jac_val = jaccard(files[filenames[i]], files[filenames[j]], k)
            jac[i,j]  = jac_val
            jac[j,i] = jac_val

            print(filenames[i], filenames[j], jac)

    jac_df = pd.DataFrame(jac, index = filenames, columns = filenames)
    jac_df.to_csv("jaccard.csv")
