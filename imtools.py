#Taylor Mallory
#tools working with openCV

from PIL import Image
from numpy import *

def imresize(im,sz):
	""" Resize an image array using PIL. """
	pil_im = Image.fromarray(uint8(im))

	return array(pil_im.resize(sz))

def histeq(im,nbr_bins=256):
	""" Histogram equalization of a grayscale image. """
	imhist,bins = histogram(im.flatten(),nbr_bins,normed=True)
	cdf = imhist.cumsum() # cumulative distribution function
	cdf = 255 * cdf / cdf[-1] # normalize

	# use linear interpolation of cdf to find new pixel values
	im2 = interp(im.flatten(),bins[:-1],cdf)

	return im2.reshape(im.shape), cdf


