from PIL import Image
import numpy as np
import math
from collections import Counter

ASCII_CHARS = " .:-=+*|#@" # Inspo Credit: https://paulbourke.net/dataformats/asciiart/


def rgbToGrayScale(r,g,b):
	try:
		return 0.299 * r + 0.587 * g + 0.114 * b
	except:
		print(r,g,b)
		raise Exception("Error in converting RGB to Grayscale")

# ASCII art will always be 100 characters wide
def imageToAscii(input_image_path, width=100, invert=False):
	ascii_image = ""
 
 	# open the image
	image = Image.open(input_image_path)
	type =  image.format
	print(type)
	w,h = image.size
	
	if(w <= width or h <= width):
		raise Exception("Image is too small. Image must be atleast 100px x 100px")

	if(type.upper() != 'JPEG' and type.upper() != 'JPG'):
		raise Exception("Image must be in JPEG format")
	
 	# Resize the image
	image.resize((width, math.ceil(width * h / w))).save("resized.%s" % type)
	
	# open resized image
	img = Image.open("resized.%s" % type)
 	
  	# convert to rgb
	img = img.convert('RGB')
 
	pixels = img.load()
	
 	# redefine width and height
	w,h = img.size	
 
	for y in range(h):
		for x in range(w):
			# Get grayscale value of pixel
			px = pixels[x,y]
			gScale = rgbToGrayScale(px[0], px[1], px[2])
			# Get the ascii character
			if invert:
				ascii_image += ASCII_CHARS[math.floor((255 - gScale) * ((len(ASCII_CHARS) - 1) / 255))]
			else:
				ascii_image += ASCII_CHARS[math.floor(gScale * ((len(ASCII_CHARS) - 1) / 255))]
		ascii_image += "\n"
	
	return ascii_image


if __name__ == '__main__':
	# Ask for image path
	image_path = input("Enter the path of the image: ")
	width = int(input("Width of the image: ").strip() or "100")
	output_ascii_path = "ascii.txt"
 	
	# Convert the image to ascii
	ascii_image = imageToAscii(image_path, width, True)
	print(ascii_image)
 	# Save the ascii image
	with open(output_ascii_path, "w") as f:
		f.write(ascii_image)
	