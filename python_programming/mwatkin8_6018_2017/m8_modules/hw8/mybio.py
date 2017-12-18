"""
A module for working with DNA data

Copyright Michael Watkins
"""

def get_kmer_locations(seq, kmer="A"):
    """
    Finds the starting locations of kmers if they are present in a DNA sequence
    
    seq: A DNA sequence provided in string format consisting of only valid nucleotides.
    kmer: a string representing a DNA subsequence of length k
    
    returns: All the start locations, if any, of `kmer` in `seq`."""
    index = 0
    locations = []
    while index < len(seq):
        i = seq.find(kmer,index,index+len(kmer))
        if i == -1:
            index += 1
            continue
        else:
            locations.append(index)
            index += 1
    return tuple(locations)


def get_kmer_locations_recursive(seq, kmer="A", start=0):
    """
    This function recursively goes through a DNA sequence and looks for the starting locations of a kmer if it is present.
    
    seq: a string containing a DNA sequence
    kmer: a string representing a DNA subsequence of length k
    start: the start of an index of 'seq' where we are looking for 'kmer'

    returns: a list of starting locations for kmer within seq"""
    
    loc = seq.find(kmer, start)
    if loc != -1:
        return [loc] + get_kmer_locations_recursive(seq, kmer=kmer, start=loc+1)
    else:
        return []

def count_kmers(sequences, kmers):
    """
    Counts the instances of kmers in a DNA sequence
    
    sequences: a dictionary of DNA sequences with the form {"seq1":sequence1, "seq2":sequence2, ..., "seqN": sequenceN}
    kmers: a string representing a DNA subsequence of length k
    
    returns:
    """
    rslts = {}
    if kmers == None:
        kmers = ('A')
    for seq in sequences:
        sequence = sequences[seq]
        "".join(sequence.split())
        entry = {}
        for kmer in kmers:
            entry[kmer] = 0
            l = len(kmer)
            for i in range(0, len(sequence)):
                test = sequence[i:i+l]
                if len(test) != l:
                    break
                if test == kmer:
                    entry[kmer] += 1
                    
        rslts[seq] = entry    
    return rslts
