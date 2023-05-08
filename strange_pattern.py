import numpy as np

def strange_pattern(pattern):
    n, m = pattern
    win = np.zeros((n, m), dtype=bool)

    for i in range(n):
        for j in range(m):
            if (i + j) % 3 == 0:
                win[i, j] = True

    return win
if __name__ == "__main__":
    pattern = (10, 10)
    print(strange_pattern(pattern))
