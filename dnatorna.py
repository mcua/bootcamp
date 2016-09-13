"""
Convert DNA sequences to RNA
"""

def rna(seq):
    """Convert a DNA sequence to RNA"""
    # Convert to upper case
    seq = seq.upper()

    return seq.replace('T','U')
