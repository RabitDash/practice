import sys
import copy
import cv2
import getopt
import math

def detectEdges(image):
	edges = cv2.Canny(image, 100, 100)
	cv2.imwrite("edges.jpg", edges)
	return edges

def isolateUnique(image, edges):
	blocksize = 64
	varianceThreshold = 95
	cellPx = image.shape[1] // blocksize
	rows = image.shape[0] // cellPx
	cols = blocksize
	blockPx = cellPx * cellPx
	cellValues = [0] * (rows)
	imgR = 0
	imgG = 0
	imgB = 0
	imgCells = (blockPx) * (rows * cols)
	
	for i in range(rows):
		cellValues[i] = [0] * blocksize
		for j in range(cols):
			rbeg = cellPx * i
			rend = rbeg + cellPx

			cbeg = cellPx * j
			cend = cbeg + cellPx

			r = 0
			g = 0
			b = 0

			hasEdge = False

			for ii in range(rbeg, rend):
				for jj in range(cbeg, cend):
					if edges[ii][jj] > 0:
						hasEdge = True
					r = r + image[ii][jj][0]
					g = g + image[ii][jj][1]
					b = b + image[ii][jj][2]
			imgR = imgR + r
			imgG = imgG + g
			imgB = imgB + b
			rv = int(r / blockPx)
			gv = int(g / blockPx)
			bv = int(b / blockPx)
			value = [rv, gv, bv] if hasEdge is True else [0,0,0]
			cellValues[i][j] = value
			cv2.rectangle(image, (cbeg, rbeg), (cend, rend), (rv, gv, bv), -1)
	avgR = imgR // imgCells
	avgG = imgG // imgCells
	avgB = imgB // imgCells
		
	cv2.rectangle(image, (0, 0), (image.shape[1], image.shape[0]), (0, 0, 0),
		-1)
	for i in range(len(cellValues)):
		for j in range(len(cellValues[i])):
			rdiff = abs(cellValues[i][j][0] - avgR)
			gdiff = abs(cellValues[i][j][1] - avgG)
			bdiff = abs(cellValues[i][j][2] - avgB)

			rbeg = cellPx * i
			rend = rbeg + cellPx

			cbeg = cellPx * j
			cend = cbeg + cellPx

			pxDiff = True if (rdiff > varianceThreshold or gdiff > varianceThreshold or bdiff > varianceThreshold) else False
			isBlack = True if (cellValues[i][j][0] < 30 and cellValues[i][j][1] < 30 and cellValues[i][j][2] < 30) else False
			if pxDiff and isBlack is False:
				cv2.rectangle(image, (cbeg, rbeg), (cend, rend), (255,255,255), -1)
			else:
				cv2.rectangle(image, (cbeg, rbeg), (cend, rend), (0, 0, 0), -1)
	cv2.imwrite("blocks.png", image)

def main(argv):
	face_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml')
	eye_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_eye.xml')
	inputFile = ''
	outputFile = ''
	width = 300
	height = 300
	blocksize = 64

	opts, args = getopt.getopt(argv, "hi:o:x:y:b:", ["ifile=", "ofile="])
	for opt, arg in opts:
		if opt == "-i":
			inputFile = arg
		if opt == "-o":
			outputFile = arg
		if opt == "-y":
			height = arg
		if opt == "-x":
			width = arg
		if opt == "-b":
			blocksize = arg

	if outputFile == '':
		outputFile = inputFile
	orgHeight = height
	orgWidth = width
	img = cv2.imread(inputFile)
	assert img is not None
	original = copy.copy(img)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(
		gray,
		scaleFactor = 1.1,
		minNeighbors = 5,
		minSize = (30, 30),
		flags = cv2.CASCADE_SCALE_IMAGE)
	edgeRef = detectEdges(img)
	isolateUnique(img, edgeRef)
	maxFaceRight = 0
	print("Found {0} faces!".format(len(faces)))

	imgHeight, imWidth = img.shape[:2]
	cropBias = imWidth
	for(x, y, w, h) in faces:
		cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), -1)
		cropBias = cropBias - x

		if (x + w) > maxFaceRight:
			maxFaceCenter = (x + w) - (w // 2)
			maxFaceRight = x + w

		roi_gray = gray[y:y + h, x: x + w]
		roi_color= img[y:y + h, x: x + w]

		eyes = eye_cascade.detectMultiScale(roi_gray)

		for (ex, ey, ew, eh) in eyes:
			cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
	cropBiasPerc = cropBias / imWidth

	ratio = int(height) / img.shape[0]
	height = img.shape[0]

	middleY = 0
	newRatio = height / int(orgHeight)
	width = round(int(width) * newRatio)
	rawCols = math.ceil(img.shape[1] / width)
	mostPosIndex = 0
	bestPosValue = 0
	
	for i in range(rawCols):
		positiveCount = 0
		startx = i * width
		endx = startx + width
		endx = img.shape[1] if endx > img.shape[1] else endx
		for col in range(startx, endx):
			for row in range(img.shape[0]):
				pxval = img[row][col][0] + img[row][col][1] + img[row][col][2]
			if pxval > 0:
				positiveCount = positiveCount + 1
		if positiveCount > bestPosValue:
			mostPosIndex = i
			bestPosValue = positiveCount
		print(i, positiveCount)
	print("Best Index: ", str(mostPosIndex))
	middleX = mostPosIndex * width

	if middleX + width  > img.shape[1]:
		middleX = img.shape[1] - width
	
	cv2.rectangle(img, (middleX, middleY),
			(middleX + width, middleY + height),
			(0, 255, 0),
			2)

	cropped = copy.copy(original)
	copyName = "ref_" + outputFile
	croppedName = "cropped_" + outputFile
	cropX1 = middleX + width
	cropY1 = middleY + height
	croppedData = original[middleY:cropY1, middleX:cropX1]

	cv2.imwrite(copyName, original)
	cv2.imwrite(croppedName, croppedData)
	cv2.imwrite(outputFile, img)

if __name__ == "__main__":
	main(sys.argv[1:])
