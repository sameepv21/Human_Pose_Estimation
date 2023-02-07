import numpy as np
import pandas as pd
import os
import json
import time

# Global Variables
TRAIN_ANNOTATION_PATH = "../data/train/annotation.json"
TEST_ANNOTATION_PATH = "../data/test/annotation.json"
VAL_ANNOTATION_PATH = "../data/val/annotation.json"

# Load json data
TRAIN_DATA = json.load(open(TRAIN_ANNOTATION_PATH))
TEST_DATA = json.load(open(TEST_ANNOTATION_PATH))
VAL_DATA = json.load(open(VAL_ANNOTATION_PATH))

start = time.time()

# function that returns gaussian distribution
def gaussian(x, y, meanx, meany):
    pass

end = time.time()
print('Total time taken to generate heatmaps:', round((end - start), 2), "seconds")