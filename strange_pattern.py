import numpy as np

def strange_pattern(pattern):
    win = np.zeros((pattern), dtype=bool)
    for i in range(pattern[0]):
        for j in range(pattern[1]):
            if (i + j) % 3 == 0:
                win[i, j] = True

    return win
if __name__ == "__main__":
    pattern = (10, 10)
    print(strange_pattern(pattern))
