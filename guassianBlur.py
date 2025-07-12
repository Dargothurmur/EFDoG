import numpy as np
def blur1D(sigma, size):
    middleIndex = size // 2

    m = range(-middleIndex, middleIndex+1)
    cursor = 0

    kernel1D = []

    for index in m:
        value = 1/(np.sqrt(2 * np.pi) * sigma) * (np.e ** (-(index ** 2)/(2*(sigma ** 2))))
        kernel1D.append(value)
    
    kernel1D = np.array(kernel1D)
    kernel1D /= kernel1D.sum()

    return kernel1D