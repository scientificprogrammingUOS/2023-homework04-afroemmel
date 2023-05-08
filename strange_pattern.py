import numpy as np

def strange_pattern(shape):
    n, m = shape
    pattern = np.zeros((n, m), dtype=bool)
    
    for i in range(n):
        for j in range(m):
            if (i % 6 < 3 and j % 6 < 3) or (i % 6 >= 3 and j % 6 >= 3):
                pattern[i, j] = True
    
    return pattern
if __name__ == "__main__":
    # use this for your own testing!

    pass
