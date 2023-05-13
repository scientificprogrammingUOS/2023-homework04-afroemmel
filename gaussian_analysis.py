import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, low, high):
    meaningfulError = "much meaningful so wow"
    if type(loc) is not int and type(loc) is not float:
        return meaningfulError
    if type(scale) is not int and type(scale) is not float:
        return meaningfulError
    if type(low) is not int and type(low) is not float:
        return meaningfulError
    if type(high) is not int and type(high) is not float:
        return meaningfulError
    if low > high:
        return meaningfulError

    arr = np.random.normal(loc, scale, 100)
    arr = arr[arr >= low]
    arr = arr[arr <= high]
    return np.mean(arr), np.std(arr)


if __name__ == "__main__":
    # use this for your own testing!

    pass
