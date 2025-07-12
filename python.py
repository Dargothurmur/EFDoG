from PIL import Image
import guassianBlur as GB

img = Image.open("Images/Thelighthouse.jpg")
img_gray = img.convert("L")  # ensure grayscale
pixels = img_gray.load()

width, height = img_gray.size

# Prepare output image
output_img = Image.new("L", (width, height))
output_pixels = output_img.load()

output = "D:/FDoG/EFDoG/FilteredImage/DoG"
fileName = "Test.jpg"
outputImage = output + "/" + fileName

kernelSize = 7
sigma = 5.0
kernel = GB.blur1D(sigma, kernelSize)

width, height = img.size
kMid = kernelSize // 2

#Blur in x direction
for pixelY in range(height):
    for pixelX in range(width):
        accumulation = 0.0
        normal = 0.0
        kernelRange = range(-kMid, kMid + 1)
        for dx in kernelRange:
            nx = pixelX + dx
            if 0 <= nx < width:
                weight = kernel[dx + kMid]
                accumulation += weight * pixels[nx, pixelY]
        output_pixels[pixelX, pixelY] = int(accumulation)

#Blur in y direction
for pixelX in range(width):
    for pixelY in range(height):
        accumulation = 0.0
        normal = 0.0
        kernelRange = range(-kMid, kMid + 1)
        for dy in kernelRange:
            ny = pixelY + dy
            if 0 <= ny < height:
                weight = kernel[dy + kMid]
                accumulation += weight * output_pixels[pixelX, ny]
        output_pixels[pixelX, pixelY] = int(accumulation)
        

output_img.save(outputImage)
