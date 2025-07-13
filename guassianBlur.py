import numpy as np
from PIL import Image 
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

def optimized_gaussian_blur(image_path, kernel_size=7, sigma=5.0):

    img = Image.open(image_path)
    img_gray = img.convert("L")
    
    img_array = np.array(img_gray, dtype=np.float32)
    height, width = img_array.shape
    
    kernel = blur1D(sigma, kernel_size)
    kernel = np.array(kernel, dtype=np.float32)
    
    kernel = kernel / np.sum(kernel)
    
    k_mid = kernel_size // 2
    
    padded_img = np.pad(img_array, k_mid, mode='edge')
    
    h_blurred = np.zeros_like(img_array)
    for i in range(kernel_size):
        weight = kernel[i]
        h_blurred += weight * padded_img[k_mid:k_mid+height, i:i+width]
    
    padded_h_blurred = np.pad(h_blurred, k_mid, mode='edge')
    
    v_blurred = np.zeros_like(img_array)
    for i in range(kernel_size):
        weight = kernel[i]
        v_blurred += weight * padded_h_blurred[i:i+height, k_mid:k_mid+width]
    
    result = np.clip(v_blurred, 0, 255).astype(np.uint8)
    
    return result

def difference_Of_Guassians(imagePath, kernelSize, sigma, sigma_k, threshHold):

    smaller_G = optimized_gaussian_blur(imagePath, kernelSize, sigma)
    larger_G = optimized_gaussian_blur(imagePath, kernelSize, sigma * sigma_k)

    result = smaller_G - larger_G
    output_Image = Image.fromarray(threshHolded(result, threshHold))
    return output_Image

def threshHolded(imageArry, cutoff):
    result = imageArry.copy()
    
    result[result > cutoff] = 255
    result[result <= cutoff] = 0
    
    return result

def extended_diff_of_Gaussians(imagePath, kernelSize, sigma, sigma_k, threshHold, tau, phi):
    smaller_G = (1 + tau) * optimized_gaussian_blur(imagePath, kernelSize, sigma)
    larger_G = tau * optimized_gaussian_blur(imagePath, kernelSize, sigma * sigma_k)

    result = smaller_G - larger_G
    output_Image = Image.fromarray(advancedThreshHold_v2(result, threshHold, phi))
    return output_Image
    

def advancedThreshHold_v2(imageArray, cutoff, phi):

    result = imageArray.copy().astype(np.float32)
    threshold_response = np.where(
        result > cutoff,
        255.0, 
        255 * (1 + np.tanh(phi * (result - cutoff))) 
    )
    
    return np.clip(threshold_response, 0, 255).astype(np.uint8)
