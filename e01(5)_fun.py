def complement_base(base,material = 'DNA'):
    """Returns the Watson-Crick complement of a base."""

    if base in 'Aa':
        if material == 'DNA':
            return 'T'
        else:
            return 'U'
    elif base in 'TtUu':
        return 'A'
    elif base in 'Gg':
        return 'C'
    elif base in 'Cc':
        return 'G'
    else:
        return '_'

def complement_bases(base,material = 'DNA',wobble = True):
    """Returns the Watson-Crick complement of a base."""

    if base in 'Aa':
        if material == 'DNA':
            return 'T'
        else:
            return 'U'
    elif base in 'Tt':
        return 'A'
    elif base in 'Uu' and material == 'RNA':
        if wobble == True:
            return 'AG'
        else:
            return 'A'
    elif base in 'Gg':
        if material == 'RNA' and wobble == True:
            return 'CU'
        else:
            return 'C'
    elif base in 'Cc':
        return 'G'
    else:
        return '_'

def parentheses_balanced(seq):
    """Checks if #'(' is equal to #')'"""
    if seq.count('(') == seq.count(')'):
        res = True
    else:
        res = False

    return(res)

def check_basepair(seq):

    lenStr   = len(seq)
    numBP    = lenStr//2
    seq      = seq.upper();
    dotNum   = []

    for i in range(0,lenStr,1):
        dotNum.append(0)

    for i in range(0,numBP,1):
        if seq[i]==complement_base(seq[lenStr-i-1],'RNA'):
            dotNum[i] = 1
            dotNum[lenStr-i-1] = 2

    dotparen = '';
    for i in dotNum:
        dotparen += str(i)

    dotparen = dotparen.replace('1','(')
    dotparen = dotparen.replace('2',')')
    dotparen = dotparen.replace('0','.')

    return dotparen

def dotparen_to_bp(dotparen):
    """Converts dot-parens notation to 2-tuples representing the base pairs"""
    lenStr  = len(dotparen)
    good    = parentheses_balanced(dotparen)
    dotList = []

    if good == False:
        return 0

    numBP = dotparen.count('(')

    i = 0;
    while i <= lenStr//2:
        if dotparen[i] == '(':
            print('appending', i)
            dotList.append([i,lenStr-i-1])
        i += 1

    return tuple(dotList)

def ishairpin(dotparen):
    if type(dotparen) == str:
        val = dotparen.find('...')
        if val != -1:
            res = True
        else:
            res = False
    else: #tuple
        lenSeq = sum(dotparen[0])+1
        numBp  = lenSeq//2 - 1
        if len(dotTuple) > numBp:
            res = False
        else:
            res = True
    return(res)

def rna_ss_validator(seq,sec_struc,wobble=True):
    res = ishairpin(sec_struc)
    if res == False:
        return False

    # Check structure against seq
    lenSeq = len(seq)
    numBp  = lenSeq//2
    for i in range(0,numBp,1):
        if sec_struc[i] == '(':
            if sec_struc[lenSeq-i-1] !=')':
                return False
            elif seq[lenSeq-i-1] not in complement_bases(seq[i],'RNA',wobble):
                return False
        elif sec_struc[i] == '.':
            if sec_struc[lenSeq-i-1] != '.':
                return False

    return True
