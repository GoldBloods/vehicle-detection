# import the necessary packages
import imutils

def pyramid(image, scale, minSize=(30, 30)):
	# yield the original image
	yield image
	# keep looping over the pyramid
	while True:
		# compute the new dimensions of the image and resize it
		w = int(image.shape[1] / scale)
		image = imutils.resize(image, width=w)

		# if the resized image does not meet the supplied minimum
		# size, then stop constructing the pyramid
		if image.shape[0] < minSize[1] or image.shape[1] < minSize[0]:
			break

		# yield the next image in the pyramid
		yield image

def sliding_window(image, startingHeight, stepSize, windowSize):
	# slide a window across the image
	if image.shape[0] < startingHeight:
		print 'Starting height cannot be larger than actual height'
		exit()

	#for y in xrange(0, image.shape[0], stepSize):
	for y in xrange(startingHeight, image.shape[0], stepSize):
		for x in xrange(0, image.shape[1], stepSize):
			# yield the current window
			yield (x, y, image[y:y + windowSize[1], x:x + windowSize[0]])
