import os,sys

# LP: append local modules path
BASE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, os.path.join(BASE_PATH, 'modules'))
