import numpy as np 

# implement your function to combine two numpy arrays 

def combination(arr1, arr2, axis=0):
    # Remove unnecessary dimensions of input arrays
    arr1 = np.squeeze(arr1)
    arr2 = np.squeeze(arr2)

    # Check if arrays can be combined along the given axis
    if arr1.shape[:axis] != arr2.shape[:axis] or arr1.shape[axis + 1:] != arr2.shape[axis + 1:]:
        raise ValueError("Cannot combine arrays along the specified axis.")

    # Combine arrays along the given axis
    combined = np.concatenate((arr1, arr2), axis=axis)

    return combined


if __name__ == "__main__":
    # use this for your own testing!

    pass
