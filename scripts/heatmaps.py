import numpy as np
import cv2
import json
import matplotlib
import matplotlib.pyplot as plt
import time

# Global Variables
TRAIN_ANNOTATION_PATH = "../data/train/annotation.json"
TEST_ANNOTATION_PATH = "../data/test/annotation.json"
VAL_ANNOTATION_PATH = "../data/valid/annotation.json"
TRAIN_DATA = json.load(open(TRAIN_ANNOTATION_PATH))
TEST_DATA = json.load(open(TEST_ANNOTATION_PATH))
VAL_DATA = json.load(open(VAL_ANNOTATION_PATH))
IMAGE_SHAPE = (224, 224, 3)
STDDEV = 8

start = time.time()

# function that returns gaussian value
def gaussian(x, y, stddev=STDDEV):
    exp_num = -((np.arange(224) - x)**2 + (np.arange(224) - y)**2)
    exp_den = 2*(stddev**2)
    exp = np.exp((exp_num/exp_den))
    den = 1/2*np.pi*(stddev**2)
    normal_arr = exp / den
    round_arr = np.round((exp / den), 3)
    return round_arr

# function that returns heatmap for a particular image
def heatmap(keypoints, sd=STDDEV):
    heatmap_arr = np.zeros(IMAGE_SHAPE[:2])
    for index, kp in enumerate(keypoints):
        x, y, _ = kp
        gaussian_value = gaussian(x, y, sd)
        heatmap_arr[index] = gaussian_value
    return heatmap_arr

def plot_heatmap(image, heatmap):
    cv2.imshow("Image", image)
    cv2.imshow("Heatmap", heatmap)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    test_keypoints = VAL_DATA.get('18519').get("keypoints")
    image = cv2.imread("../data/valid/images/18519.jpg")
    _heatmap = heatmap(test_keypoints)
    print(_heatmap)
    # plot_heatmap(image, _heatmap)
    
main()

end = time.time()
print('Total time taken to generate heatmaps:', round((end - start), 2), "seconds")