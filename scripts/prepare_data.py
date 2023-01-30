# Required libraries
import numpy as np
import splitfolders as sf
import os
import json

# Global variables
TRAIN_SIZE = 0.8
TEST_SIZE = 1 - TRAIN_SIZE
RELATIVE_PATH = '../data'
ANNOTATION_PATH = '../data/train/annotation.json'
SEED_VALUE = 42

# Split folders
def split_images():
    sf.ratio(
        os.path.join(RELATIVE_PATH, "train"),
        os.path.join(RELATIVE_PATH, "preprocessed"),
        seed = SEED_VALUE,
        ratio = (TRAIN_SIZE, TEST_SIZE),
        group_prefix = None
    )

# Copy and organize file
def organize():
    print("Organizing...")
    os.system("cp " + ANNOTATION_PATH + " ../data/preprocessed/train/annotation.json")
    os.system("rm -rf ../data/train")
    os.system('cp ../data/preprocessed/train ../data/train -r')
    os.system('cp ../data/preprocessed/val ../data/test -r')
    os.system('rm -rf ../data/preprocessed')

# Create annotation.json for test dataset
def generate_test_annotation(annotation_path = ANNOTATION_PATH):
    print("Generating Annotations File...")
    with open(annotation_path) as json_file:
        data = json.load(json_file)


def main():
    split_images()
    organize()
    generate_test_annotation(ANNOTATION_PATH)

main()