#! /usr/bin/env python
from setuptools import setup

setup(
    name="facemaskdetect",
    version='1.0.0',
    description='Face masks detector with Tensorflow Keras and MobileNet V2',
    packages=["facemaskdetect"],
    install_requires=['numpy',
        'tensorflow==2.5.0',
        'opencv-python',
        'imutils'],
    entry_points = {
        "console_scripts": [
            "facemaskdetect = facemaskdetect.detector:main",
        ]
    },
    package_data={'facemaskdetect': ['face_detector/*', '*.model']},
    include_package_data=True
)