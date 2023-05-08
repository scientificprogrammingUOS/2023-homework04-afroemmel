import numpy as np

# implement the function strange pattern

def strange_pattern():
    n, m = shape
    pattern = np.zeros((n, m), dtype=bool)
    
    for i in range(n):
        for j in range(m):
            if (i % 3 == 0 or i % 3 == 2) and (j % 3 == 0 or j % 3 == 2):
                pattern[i, j] = True
    
    return pattern


if __name__ == "__main__":
    # use this for your own testing!

    pass
