from PIL import Image
import guassianBlur as GB
import numpy as np

img = Image.open("Images/Thelighthouse.jpg")
img_gray = img.convert("L")
pixels = img_gray.load()

width, height = img_gray.size


def optimized_gaussian_blur(image_path, kernel_size=7, sigma=5.0):

    img = Image.open(image_path)
    img_gray = img.convert("L")
    
    img_array = np.array(img_gray, dtype=np.float32)
    height, width = img_array.shape
    
    kernel = GB.blur1D(sigma, kernel_size)
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
    output_img = Image.fromarray(result, mode='L')
    
    return output_img

output = "D:/FDoG/EFDoG/FilteredImage/DoG"
fileName = "Test.jpg"
outputImage = output + "/" + fileName

kernelSize = 3
sigma = 1.0
kernel = GB.blur1D(sigma, kernelSize)

width, height = img.size

optimized_gaussian_blur("Images/Thelighthouse.jpg", kernelSize, sigma).save(outputImage)
