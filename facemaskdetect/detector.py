# -*- coding: utf-8 -*-
#
# source code Adrian Rosebrock
# https://www.pyimagesearch.com/2020/05/04/covid-19-face-mask-detector-with-opencv-keras-tensorflow-and-deep-learning/
# adapted by Loreto Parisi (loretoparisi at gmail dot com)
#

import os,sys,argparse

# LP: append local modules path
BASE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, os.path.join(BASE_PATH, 'modules'))

try:
	from detect_mask_image import detect_from_image
except:
	from .detect_mask_image import detect_from_image

def detect(image_path, 
	confidence=0.5, 
	output='json'):

	args = {}
	args['image'] = image_path
	args['face'] = os.path.join(BASE_PATH, 'face_detector')
	args['model'] = os.path.join(BASE_PATH, 'mask_detector.model')
	args['confidence'] = confidence
	args['output'] = output
    
	return detect_from_image(args)

def main():
	# construct the argument parser and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--image", required=True,
		help="path to input image")
	ap.add_argument("-f", "--face", type=str,
		default="face_detector",
		help="path to face detector model directory")
	ap.add_argument("-m", "--model", type=str,
		default="mask_detector.model",
		help="path to trained face mask detector model")
	ap.add_argument("-c", "--confidence", type=float, default=0.5,
		help="minimum probability to filter weak detections")
	ap.add_argument("-o", "--output", type=str,
		default="cam",
		help="specify a camera (cam) | png | json")
	args = vars(ap.parse_args())
	
	res = detect_from_image(args)
	if res:
		print(res)

if __name__ == "__main__":
    main()


