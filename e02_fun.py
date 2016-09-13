# import modules
import os

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

def proc_fasta_gc(fname_in,fname_out,block_size,gc_thresh):

    # Load sequence from fasta file
    seq = load_fasta(fname_in)

    # Load description from fasta
    with open(fname_in,'r') as f:
        f_desc = f.read()

    # Process sequence
    seqmap = gc_map(seq,block_size,gc_thresh)

    # Add \n every 60 characters
    nAdd = len(seqmap//60)

    for i in range(nAdd,0,-1):
        seqmap = seqmap.insert(i*60,'\n')

    # Write Mapped sequences
    with open(fname_out,'w') as f:
        f.write(f_desc)
        f.write(seqmap)

    return 0

def orf_detect(seq):
    """Detects ORF sequences in DNA sequences"""
    ORF_start = 'ATG'
    ORG_end   = ['TGA','TAG','TAA']

    
