import re
import heapq

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


def stream_kmers(file, k):
    mask = (1 << (2*k)) - 1

    kmer1 = 0
    kmer2 = 0
    encodage = {'A' : 0, 'C' : 1, 'T' : 2, 'G' : 3}

    for text in file: 
        text  = re.sub(r'[^ACTG]','',text)
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

def xorshift(seed):
    seed ^= (seed << 21)
    seed ^= (seed >> 35)
    seed ^= (seed << 4)
    return seed & 0xFFFFFFFFFFFFFFFF


def echantillonage(f,k,s): 
    sketch=[-2**63]*s
    heapq.heapify(sketch) 
    for kmer in stream_kmers(f,k):
        elem=-sketch[0]
        if kmer<elem:
            heapq.heappop(sketch) 
            heapq.heappush(sketch,-kmer)
    return sketch
