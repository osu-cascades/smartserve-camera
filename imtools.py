#Taylor Mallory

from PIL import Image
from numpy import *

def imresize(im,sz):
	""" Resize an image array using PIL. """
	pil_im = Image.fromarray(uint8(im))
	return array(pil_im.resize(sz))

