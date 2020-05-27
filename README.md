# facemaskdetect
Face masks detector with Tensorflow Keras and MobileNet V2. It supports still image or camera detection. The output is to image with bounding box and label (Mask, NoMask), image viewer or to JSON.

## Disclaimer
Source code adpted from Adrian Rosebrock article available here:
https://www.pyimagesearch.com/2020/05/04/covid-19-face-mask-detector-with-opencv-keras-tensorflow-and-deep-learning/

## How to build
To build the docker image please do:

```bash
docker build . -t facemaskdetect
```

### How to install
We provide a python setup to install a command line script `facemaskdetect`:

```bash
python setup.py install
```

## How to run
To run the installed script to get `JSON` output:

```
facemaskdetect -i examples/example_01.png -o json
```

for image output with bounding boxes:
```
facemaskdetect -i examples/test.jpeg -o out.png
```

### How to run the container on linux
To run on a `linux` host without X server support:
```bash
docker run --rm -it -v $(pwd):/app facemaskdetect bash
```

to enable X server support:

```bash
docker run --rm -it --net=host --ipc=host -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --env="QT_X11_NO_MITSHM=1" -v $(pwd):/app facemaskdetect bash
```

### How to run the container on macOS
To run on `macOS` with X server support enabled, first be sure to have xquartz and socat installed:

```bash
brew install socat
brew cask install xquartz
```
NOTE. In case of errors, please do `brew reinstall`.

then open XQuartz server and bind to the port:
```bash
open -a XQuartz
socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\"
```

then in another window (important!) run docker with display forwarding:

```bash
docker run  -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --rm -it -v $(pwd):/app facemaskdetect bash
```

## Mask detection from still image
To detect from a still image with camera output
```bash
python facemaskdetect/detector.py -i ../examples/example_01.png -o cam
```

To detect from a still image with file output
```bash
python facemaskdetect/detector.py -i ../examples/example_02.png -o output.png
```

To detect from a still image with `JSON` output
```bash
python facemaskdetect/detector.py -i ../examples/example_01.png -o json
```

To JSON output format looks like:

```json
[
    {
        "label": "Mask",
        "accuracy": "0.93",
        "box": {
            "start_x": 173,
            "start_y": 161,
            "end_x": 565,
            "end_y": 750
        }
    },
    {
        "label": "Mask",
        "accuracy": "0.99",
        "box": {
            "start_x": 394,
            "start_y": 411,
            "end_x": 685,
            "end_y": 775
        }
    }
]
```

## Mask detection from video
To continuosuly detect from a video stream of a camera (like web cam):
```bash
python facemaskdetect/camera.py 
```

## Sample application
A example application is available in `app.py`. To run it

```bash
python app.py
```
