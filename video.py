import cv2
import imutils
from PIL import Image, ImageTk


def videoLoop(self):
	# DISCLAIMER:
	# I'm not a GUI developer, nor do I even pretend to be. This
	# try/except statement is a pretty ugly hack to get around
	# a RunTime error that Tkinter throws due to threading
	try:
		# keep looping over frames until we are instructed to stop
		while not self.stopEvent.is_set():
			# grab the frame from the video stream and resize it to
			# have a maximum width of 300 pixels
			self.frame = self.vs.read()
			self.frame = imutils.resize(self.frame, width=300)
		
			# OpenCV represents images in BGR order; however PIL
			# represents images in RGB order, so we need to swap
			# the channels, then convert to PIL and ImageTk format
			image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
			image = Image.fromarray(image)
			image = ImageTk.PhotoImage(image)
		
			# if the panel is not None, we need to initialize it
			if self.panel is None:
				self.panel = tki.Label(image=image)
				self.panel.image = image
				self.panel.pack(side="left", padx=10, pady=10)
		
			# otherwise, simply update the panel
			else:
				self.panel.configure(image=image)
				self.panel.image = image
	except RuntimeError as e:
		print("[INFO] caught a RuntimeError")