# import modules
import os
import bioinfo_dicts as bd
import numpy as np

# E02.1 - read fasta file
def load_fasta(filename):
    """Loads fasta files"""

    # Read information in file
    with open(filename,'r') as f:
        f_lines = f.readlines()

    seq = ''

    # Remove all description lines
    for i,lines in enumerate(f_lines):
        if f_lines[i][0] == '>':
            f_lines.pop(i)

        f_lines[i] = f_lines[i].replace('\n','')
        seq += f_lines[i]

    return seq

# E02.2a - compute GC content in each block
def gc_content(seq,block_size):
    """Computes GC content in each block"""

    seq     = seq.upper()
    gc_cont = []

    # Split sequence into list of blocks and compute GC content
    for i in range(0,len(seq),block_size):
        tmp = seq[i:(block_size+i)]
        print(tmp)
        gc_cont.append((tmp.count('G')+tmp.count('C'))/block_size)

    return gc_cont

# E02.2b - Map sequence based on threshold gc content
def gc_map(seq, block_size, gc_thresh):
    """Maps sequences, where all blocks with gc content < thresh are undercased"""

    #Compute GC content
    seq     = seq.upper()
    gc_cont = gc_content(seq,block_size)
    seq1    = ''

    for i,num in enumerate(gc_cont):
        st = i*block_size
        en = st+block_size
        if num < gc_thresh:
            seq1 += seq[st:en].lower()
        else:
            seq1 += seq[st:en]

    return seq1

# E02.3 - Load in sequence from fasta file, process, and save
def proc_fasta_gc(fname_in,fname_out,block_size,gc_thresh):

    # Load sequence from fasta file
    seq = load_fasta(fname_in)

    # Load description from fasta
    with open(fname_in,'r') as f:
        f_desc = f.readline()

    # Process sequence
    seqmap = gc_map(seq,block_size,gc_thresh)

    # Add \n every 60 characters
    nAdd    = len(seqmap)//60
    seqlist = list(seqmap)

    for i in range(0,nAdd+1,1):
        ind = (nAdd - i)*60
        seqlist.insert(ind,'\n')

    seqmapOut = ''.join(seqlist)
    # Write Mapped sequences
    with open(fname_out,'w') as f:
        f.write(f_desc)
        f.write(seqmapOut)

    # Print and add every 60 characters
    # with open(fname_out,'w') as f2:
    #     f2.write(f_desc)
    #     for i in range(0,len(seqmap),60):
    #         f2.write(seqmap[i:i+60] + ['\n'])

    return seqmapOut

# E02.4a Detect ORF sequence
def orf_detect(seq):
    """Detects ORF sequences in DNA sequences"""
    ORF_start = ['ATG']
    ORF_ends  = ['TGA','TAG','TAA']

    # Find all indices corresponding to start and end sequences
    stInds    = subseq_detect(seq,ORF_start)
    endInds   = subseq_detect(seq,ORF_ends)

    print('Detected ',len(stInds),' instances of start seq')
    print('Detected ',sum(endInds), ' instances of end seq')

    endInds   = endInds[::-1]
    indDiff   = []
    maxDiff   = 0

    for i in range(0,len(stInds)):
        for j in range(0,len(endInds)):
            diff = endInds[j]-stInds[i]
            # If start and end pair form possible ORF sequence, then record
            if diff%3 == 0 and diff > maxDiff:
                maxDiff = max(diff,maxDiff)
                indDiff = [stInds[i],endInds[j]]

    print('Longest Detected Sequences is',maxDiff+3,' long')
    return seq[indDiff[0]:(indDiff[1]+3)]

# E02.4b Convert DNA to Protein sequence
def dna_to_protein(seq,fname=''):
    """Converts DNA sequence to Protein"""
    proteinList = ''

    for i in range(0,len(seq),3):
        proteinList += bd.codons[seq[i:i+3]]

    # if specified, write protein into specified file
    if fname != '':
        with out(fname) as f:
            f.write(proteinList)

    return proteinList;

# E02.4e Detect ORF sequence -multiple
def orf_detect_multi(seq,n=1):
    """Detects ORF sequences in DNA sequences"""
    ORF_start = ['ATG']
    ORF_ends  = ['TGA','TAG','TAA']

    # Find all indices corresponding to start and end sequences
    stInds    = subseq_detect(seq,ORF_start)
    endInds   = subseq_detect(seq,ORF_ends)

    print('Detected ',len(stInds),' instances of start seq')
    print('Detected ',sum(endInds), ' instances of end seq')

    indDiffs = []
    numDiffs = []

    for i in range(0,len(stInds)):
        for j in range(0,len(endInds)):
            diff = endInds[j]-stInds[i]
            # If start and end pair form possible ORF sequence, then record
            if diff%3 == 0:
                numDiffs.append(diff)
                indDiffs.append([stInds[i], endInds[j]])

    # get indices to n largest diffs
    indOrd    = np.argsort(numDiffs)
    lenOrd    = len(indOrd)
    indOrdMax = indOrd[lenOrd-n:lenOrd]
    ords      = []
    maxDiff   = []

    for ind in indOrdMax:
        ords.append(seq[indDiffs[ind][0]:indDiffs[ind][1]+3])
        maxDiff.append(numDiffs[ind]+3)

    print(n,' largest ords are lengths ', maxDiff)
    return ords

# E02.4e - v2 Detect multiple orfs - no numpy
# E02.4e Detect ORF sequence -multiple
def orf_detect_multi_b(seq,n=1):
    """Detects ORF sequences in DNA sequences"""
    ORF_start = ['ATG']
    ORF_ends  = ['TGA','TAG','TAA']

    # Find all indices corresponding to start and end sequences
    stInds    = subseq_detect(seq,ORF_start)
    endInds   = subseq_detect(seq,ORF_ends)

    print('Detected ',len(stInds),' instances of start seq')
    print('Detected ',sum(endInds), ' instances of end seq')

    indDiffs = []
    numDiffs = []
    numDiffsA = []

    for i in range(0,len(stInds)):
        for j in range(0,len(endInds)):
            diff = endInds[j]-stInds[i]
            # If start and end pair form possible ORF sequence, then record
            if diff%3 == 0:
                numDiffs.append(diff)
                numDiffsA.append(diff)
                indDiffs.append([stInds[i], endInds[j]])

    # get indices to n largest diffs
    numDiffs.sort()
    lenOrd  = len(numDiffs)
    maxDiff = numDiffs[lenOrd-n:lenOrd]
    ords    = []

    print(n,' largest ords are lengths (-3) is', maxDiff)

    for ind,dif in enumerate(numDiffsA):
        if ind in maxDiff:
            ords.append(seq[indDiffs[ind][0]:indDiffs[ind][1]+3])
        if len(ords) == n:
            break

    return ords

# E02.4a - i Detect codons in sequence
def subseq_detect(seq,codon):
    """Detects 3 letter codon in seq"""

    # Count the number of codons
    numCount = []
    for i in range(0,len(codon)):
        numCount.append(seq.count(codon[i]))

    # print(numCount)
    # Find all indices
    indices = []
    for i in range(0,len(numCount)):
        j  = 0
        nC = 0
        while j < len(seq)-3 and nC < numCount[i]:
            tmp = seq[j::].find(codon[i])
            if tmp == -1 : # no more left
                j = len(seq)
                break;
            else: #found sequence - add to list
                indices.append(tmp+j)
                j = tmp + j + 3
                nC += 1

    indices.sort()

    return indices
