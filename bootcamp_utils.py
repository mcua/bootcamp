# bootcamp_utils: a collection of statistical functions

def ecdf(data):
    """
    Computes ECDF of provided data
    """
    x = np.sort(data)
    y = np.arange(1,len(x)+1)/len(x)

    return x,y
