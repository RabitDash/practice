import sys
import os
import _os
from collections import namedtuple
from PIL import Image


class Nude(object):
	Skin = namedtuple("Skin", "id skin region x y")
	def __init__(self, path_or_image):
		if isinstance(path_or_image. Image.Image):
			self.image = path_or_image
		elif isinstance(path_or_image, str):
			self.image = Image.open(path_or_image)
		bands = self.image.getbands()

		if len(bands) == 1:
			new_img = Image.new("RGB", self.image.size)
			new_img.paste(self.image)
			f=self.image.filename
			self.image = new_img
			self.image.filename = f
		self.skin_map = []
		self.detected_regions = []
		self.merge_regions = []
		self.skin_regions = []
		self.last_from, self.last_to = -1, -1
		self.result = None
		self.message = None
		self.width, self.height = self.image.size
		self.total_pixels = self.width * self.height

	def resize(self, maxwidth=1000, maxheight=1000):
		ret = 0
		if maxwidth:
			if self.width > maxwidth:
				wpercent = (maxwidth / self.width)
				hsize = int((self.height * wpercent))
				fname = self.image.filename
				self.image = self.image.resize((maxwidth,hsize),Image.LANCZOS)
				self.image.filename = fname
				self.width, self.height = self.image.size
				self.total_pixels = self.width * self.height
				ret += 1
		if maxheight:
			if self.height > maxheight:
			hpercent = (
