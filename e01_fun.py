def reverse_complement(seq):
    """Compute reverse complement of a sequence."""

    # Initialize reverse complement
    rev_seq = ''

    # Loop through and populate list with reverse complement
    # for base in reversed(seq):
    #     rev_seq += complement_base(base)
    # E1-1.3a
    # seq1    = seq[::-1]
    # for base in seq1:
    #     rev_seq += complement_base(base)

    # E1-1.3b
    seq = seq.replace('C','X')
    seq = seq.replace('T','Y')

    seq = seq.replace('G','C')
    seq = seq.replace('X','G')
    seq = seq.replace('A','T')
    seq = seq.replace('Y','A')

    rev_seq = seq[::-1]

    return rev_seq

def complement_base(base):
    """Returns the Watson-Crick complement of a base."""

    if base in 'Aa':
        return 'T'
    elif base in 'Tt':
        return 'A'
    elif base in 'Gg':
        return 'C'
    elif base in 'Cc':
        return 'G'
    else:
        return '_'

# E1 - 1.4
def longest_substring(str1,str2):
    if len(str1)>=len(str2):
        longStr = str1;
        shrtStr = str2;
    else:
        longStr = str2;
        shrtStr = str1;

    val  = -1;

    # Start finding from longest substring
    for strLen in range(len(shrtStr),0,-1):
         print('Searching substrings ',strLen)
         stInd = 0
         while stInd <= (len(shrtStr)-strLen):
            val = longStr.find(shrtStr[stInd:strLen])
            print('   Starting from Index ',stInd,': ',shrtStr[stInd:strLen])
            if val != -1:
                break
            stInd +=1
         if val != -1:
            break;


    if val != -1:
        print('Shortest Substring is ',shrtStr[stInd:strLen])
        return shrtStr[stInd:strLen]
    else:
        return 0
