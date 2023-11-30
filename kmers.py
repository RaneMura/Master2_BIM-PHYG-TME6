
def kmer2str(val, k):
    """ Transform a kmer integer into a its string representation
    :param int val: An integer representation of a kmer
    :param int k: The number of nucleotides involved into the kmer.
    :return str: The kmer string formatted
    """
    letters = ['A', 'C', 'T', 'G']
    str_val = []
    for i in range(k):
        str_val.append(letters[val & 0b11])
        val >>= 2

    str_val.reverse()
    return "".join(str_val)


def stream_kmers(text, k):
    mask = (1 << (2*k)) - 1

    kmer1 = 0
    kmer2 = 0
    encodage = {'A' : 0, 'C' : 1, 'T' : 2, 'G' : 3}
    lst=[]

	#Parcours pour la seq [0:k-1]    
    for letter in text[:k-1]:
        nucl = encodage[letter]
        comp=(nucl+2)&0b11
        
        kmer1 <<= 2
        kmer1+=nucl
        kmer1&=mask

        kmer2 <<= 2
        kmer2+=comp
        kmer2&=mask

	#Parcours pour la seq [k-1:] décalage à jour
    for letter in text[k-1:]:
        
        nucl = encodage[letter]
        comp=(nucl+2)&0b11
        comp <<= (2*k-2)
        
        kmer1 <<= 2
        kmer1+=nucl
        
        kmer2 >>= 2
        kmer2+=comp
        
        kmer1&=mask
        kmer2&=mask

        yield min(kmer1,kmer2)
        
#l = stream_kmers("AATCTGT",3)
#for i in l :
#	print(kmer2str(i,3))    



