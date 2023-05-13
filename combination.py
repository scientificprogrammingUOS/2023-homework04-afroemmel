import numpy as np 

# implement your function to combine two numpy arrays 

def combination(arr1, arr2, axis=0):
    arr1, arr2 = np.squeeze(arr1), np.squeeze(arr2)
    if arr1.shape[:axis] != arr2.shape[:axis] or arr1.shape[axis + 1:] != arr2.shape[axis + 1:]:
        raise ValueError("meaningful error")
    return np.concatenate((arr1, arr2), axis=axis)

if __name__ == "__main__":
    arr1 = np.array([["x","x","x"], ["y","y","y"]])
    arr2 = np.array([["z","z","z"], ["a","a","a"]])
    combined0 = combination(arr1, arr2, axis=0)
    combined1 = combination(arr1, arr2, axis=1)
    k = "k"
    pass

