def ratio(x,y):
    """The ratio of 'x' to 'y'."""
    return x/y

def add(x,y):
    """Adds x and y"""
    return x+y

def complement_base(base,material='DNA'):
    """Return the Watson-Crick complement of a base"""
    if base in 'Aa':
        if material == 'DNA':
            return 'T'
        elif material == 'RNA':
            return 'U'
        else:
            raise RunTimeError('Invalid Material')
    elif base in 'TtUu':
        return 'A'
    elif base in 'Gg':
        return 'C'
    else:
        return 'G'

def reverse_complement(seq,material='DNA'):
    """Compute reverse complement of a sequence."""

    rev_seq = ''

    for base in reversed(seq):
        rev_seq += complement_base(base,material)

    return rev_seq

def add_three(a,b,c):
    return(a+b+c)
