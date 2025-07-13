from PIL import Image
import guassianBlur as GB
import numpy as np

img = Image.open("Images/Thelighthouse.jpg")
img_gray = img.convert("L")
pixels = img_gray.load()

width, height = img_gray.size

image_path = "Images/Thelighthouse.jpg"
output = "D:/FDoG/EFDoG/FilteredImage/DoG"
fileName = "DifferenceOfGaussians.jpg"
outputImageDoG = output + "/" + fileName
outputImageEDoG = output + "/" + "ExtendedDifferenceOfGaussians.jpg"

kernelSize = 7
sigma = 2.4
sigma_k = 1.6
tau = 3
phi = .1
threshHold = 56

GB.difference_Of_Guassians(image_path, kernelSize, sigma, sigma_k, threshHold).save(outputImageDoG)
GB.extended_diff_of_Gaussians(image_path, kernelSize, sigma, sigma_k, threshHold, tau, phi).save(outputImageEDoG)

