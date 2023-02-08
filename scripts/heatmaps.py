import numpy as np
import pandas as pd
import os
import json
import time

# Global Variables
TRAIN_ANNOTATION_PATH = "../data/train/annotation.json"
TEST_ANNOTATION_PATH = "../data/test/annotation.json"
VAL_ANNOTATION_PATH = "../data/val/annotation.json"
TRAIN_DATA = json.load(open(TRAIN_ANNOTATION_PATH))
TEST_DATA = json.load(open(TEST_ANNOTATION_PATH))
VAL_DATA = json.load(open(VAL_ANNOTATION_PATH))
IMAGE_SHAPE = (224, 224, 3)
STDDEV = 8

start = time.time()

# function that returns gaussian value
def gaussian(X, x, Y, y, stddev=STDDEV):
    exp_num = -((X - x)**2 + (Y - y)**2)
    exp_den = 2*(stddev**2)
    exp = np.exp((exp_num/exp_den))
    den = 1/2*np.pi*(stddev**2)

    return exp / den

# function that returns heatmap for a particular image
def heatmap(keypoints, X, Y, sd=STDDEV):
    heatmap_arr = np.zeros(IMAGE_SHAPE)
    for index, x, y, _ in enumerate(keypoints):
        gaussian_value = gaussian(X, x, Y, y, sd)
        heatmap_arr[index] = gaussian_value
    return heatmap_arr

def plot_heatmap(image, heatmap):
    pass

def main():
    test_keypoints = VAL_DATA[0].get("keypoints")
    _heatmap = heatmap(test_keypoints, )

end = time.time()
print('Total time taken to generate heatmaps:', round((end - start), 2), "seconds")