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
	from detect_mask_video import detect_from_video
except:
	from .detect_mask_video import detect_from_video

def detect(confidence=0.5):

	args = {}
	args['face'] = os.path.join(BASE_PATH, 'face_detector')
	args['model'] = os.path.join(BASE_PATH, 'mask_detector.model')
	args['confidence'] = confidence
    
	return detect_from_video(args)

def main():
	# construct the argument parser and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-f", "--face", type=str,
		default="face_detector",
		help="path to face detector model directory")
	ap.add_argument("-m", "--model", type=str,
		default="mask_detector.model",
		help="path to trained face mask detector model")
	ap.add_argument("-c", "--confidence", type=float, default=0.5,
		help="minimum probability to filter weak detections")
	args = vars(ap.parse_args())

	# specify absolute path
	if args['face'] == 'face_detector':
		args['face'] = os.path.join(BASE_PATH, 'face_detector')

	if args['model'] == 'mask_detector.model':
		args['model'] = os.path.join(BASE_PATH, 'mask_detector.model')
	
	detect_from_video(args)

if __name__ == "__main__":
	main()