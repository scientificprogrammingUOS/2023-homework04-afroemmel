import numpy as np

# implement the function strange pattern

def strange_pattern(nm):
    n, m = nm
    pattern = np.empty((n, m), dtype=str)
    
    for i in range(n):
        for j in range(m):
            if (i % 3 == 0 or i % 3 == 2) and (j % 3 == 0 or j % 3 == 2):
                pattern[i, j] = 'x'
            else:
                pattern[i, j] = ' '
    
    return pattern


if __name__ == "__main__":
    # use this for your own testing!

    pass
