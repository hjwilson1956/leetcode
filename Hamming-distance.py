def hamming_distance(StringA,StringB):
    """Return the Hamming distance between equal-length sequences"""
    if len(StringA) != String(B):
        raise ValueError("The length of sequences are not equal!")
    return sum(x !=y for (x,y) in zip(StringA,StringB))
