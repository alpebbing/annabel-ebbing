import random

def get_counts(seq, base=3):
    counts = {}
    for i in range(0,len(seq),base):
        slice = seq[i:i+base]
        if slice in counts:
            counts[slice ] += 1
        else:
            counts[slice ] = 1
    return counts

def translate_dna(dna_seq): 
    bases = ["T","C","A","G"]
    codons = [a+b+c for a in bases for b in bases for c in bases]
    amino_acids = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
    codon_table = dict(zip(codons, amino_acids))
    protein_seq = []
    
    for i in range(0,len(dna_seq),3):
        codon = dna_seq[i:i+3]
        protein_seq +=codon_table[codon]
    return ''.join(protein_seq)

def get_di_counts(seq):
    coddic = {} # Make an empty dictionary to store codons
    for i in range(0,len(seq),2):
        codon = seq[i:i+2]     
        if codon in coddic:
            coddic[codon] += 1
        else:
            coddic[codon] = 1 
        # If the codon is already within your
        # dictionary then increase its count
        # otherwise add it to the dictionary with and assign it's count as 1
    return coddic

def get_mono_counts(seq):
    coddic = {} # Make an empty dictionary to store codons
    for i in range(0,len(seq),1):
        codon = seq[i:i+1]     
        if codon in coddic:
            coddic[codon] += 1
        else:
            coddic[codon] = 1 
        # If the codon is already within your
        # dictionary then increase its count
        # otherwise add it to the dictionary with and assign it's count as 1
    return coddic

def ran_more(seq):
    r_list = []
    for i in seq:
        if i == 0:
            r_list.append("A")
        elif i == 1:
            r_list.append("C")
        elif i == 2:
            r_list.append("G")
        elif i == 3:
            r_list.append("T")
    return "".join(r_list)

# function ran_xy(y, x), where y is amount of nucleotides of the string, 
#and x is the amount of strings 

def ran_xy(y, x):
    list_rxy = []
    for j in range(x):
        ry = [random.randint(0,3) for j in xrange(y)]
        #for i in range(1, x ):
        list_rxy.append(ran_more(ry))
    return list_rxy