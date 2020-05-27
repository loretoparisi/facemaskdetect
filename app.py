# -*- coding: utf-8 -*-
#
# source code Adrian Rosebrock
# https://www.pyimagesearch.com/2020/05/04/covid-19-face-mask-detector-with-opencv-keras-tensorflow-and-deep-learning/
# adapted by Loreto Parisi (loretoparisi at gmail dot com)
#

import datetime

from facemaskdetect.detector import detect

initial_time = datetime.datetime.now()
res = detect(image_path='examples/example_01.png',
        confidence=0.5,
        output='out.png')
execute_time = (datetime.datetime.now() - initial_time).total_seconds()
print("detect time:", execute_time)

initial_time = datetime.datetime.now()
res = detect(image_path='examples/example_01.png',
        confidence=0.5,
        output='json')
execute_time = (datetime.datetime.now() - initial_time).total_seconds()
print("detect time:", execute_time)
print(res)
    
