# Required libraries
import splitfolders as sf
import os
import json
import time
from PIL import Image
import os
import numpy as np
import pandas as pd

# Global variables
TRAIN_SIZE = 0.8
TEST_SIZE = 1 - TRAIN_SIZE
SEED_VALUE = 42
SCALING_SIZE = (224, 224)

RELATIVE_PATH = '../data'
ANNOTATION_PATH = '../data/train/annotation.json'

TRAIN_PATH = "../data/train/images"
TEST_PATH = "../data/test/images"
VAL_PATH = '../data/valid/images'

TRAIN_ANNOTATION_PATH = '../data/train/annotation.json'
TEST_ANNOTATION_PATH = '../data/test/annotation.json'
VAL_ANNOTATION_PATH = '../data/valid/annotation.json'

TRAIN_DATA = json.load(open(TRAIN_ANNOTATION_PATH))
VAL_DATA = json.load(open(VAL_ANNOTATION_PATH))
TEST_DATA = None

# Strip names to conform to annotations.json
def strip_names(path):
    for fileName in os.listdir(path):
        modified_fileName = ""
        for index, char in enumerate(fileName):
            if char != '0':
                break
            else:
                modified_fileName = fileName[index + 1:]
        os.system('mv ' + path + '/' + fileName + ' ' + path + '/' + modified_fileName)
    
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
    test_json = {}
    train_json = {}
    
    with open(annotation_path) as json_file:
        data = json.load(json_file)

    # populate training set json
    for fileName in os.listdir(os.path.join(RELATIVE_PATH, 'train/images')):
        image_id = fileName.strip('.jpg')
        train_json[image_id] = data.get(image_id)
    
    # populate test set json
    for fileName in os.listdir(os.path.join(RELATIVE_PATH, 'test/images')):
        image_id = fileName.strip('.jpg')
        test_json[image_id] = data.get(image_id)
    
    # save to the respective locations
    train_object = json.dumps(train_json)
    test_object = json.dumps(test_json)

    # save train object
    with open('../data/train/annotation.json', 'w') as outfile:
        outfile.write(train_object)
    
    # save test object
    with open('../data/test/annotation.json', 'w') as outfile:
        outfile.write(test_object)

def resize_images(path, scaling_size, annotation_path, data):

    # Load and resize images
    for index, fileName in enumerate(os.listdir(path)):
        if index % 4000 == 0: # Give progress update after every 4000 images
            print('Processed', index, 'images')

        image_id = fileName.strip('.jpg')
        _image = Image.open(path + '/' + fileName)
        image_np = np.asarray(_image)

        # find the new scaling factor after the image resize
        row_scaling_factor = scaling_size[0] / image_np.shape[1]
        col_scaling_factor = scaling_size[1] / image_np.shape[0]

        # fetch keypoints, bbox and segmentation
        keypoints = np.array(data.get(image_id).get('keypoints'))
        bbox = np.array(data.get(image_id).get('bbox'))

        # resize keypoints
        keypoints[:, 0] = keypoints[:, 0] * row_scaling_factor
        keypoints[:, 1] = keypoints[:, 1] * col_scaling_factor

        # resize bbox
        bbox[0] = int(bbox[0] * row_scaling_factor)
        bbox[1] = int(bbox[1] * col_scaling_factor)
        bbox[2] = int(bbox[2] * row_scaling_factor)
        bbox[3] = int(bbox[3] * col_scaling_factor)

        # save it to the json
        data.get(image_id)['keypoints'] = keypoints.tolist()
        data.get(image_id)['bbox'] = bbox.tolist()

        _image = _image.resize(scaling_size)
        os.system("rm -rf " + os.path.join(path, fileName))
        _image.save(os.path.join(path, fileName))

    # save json to file
    serialized_object = json.dumps(data)
    with open(annotation_path, 'w') as outfile:
        outfile.write(serialized_object)
    
def get_keypoints(path, data, store_file):

    df_columns = [
        'joint1x', 'joint1y', 
        'joint2x', 'joint2y', 
        'joint3x', 'joint3y', 
        'joint4x', 'joint4y', 
        'joint5x', 'joint5y', 
        'joint6x', 'joint6y', 
        'joint7x', 'joint7y', 
        'joint8x', 'joint8y', 
        'joint9x', 'joint9y',
        'joint10x', 'joint10y', 
        'joint11x', 'joint11y', 
        'joint12x', 'joint12y', 
        'joint13x', 'joint13y', 
        'joint14x', 'joint14y', 
        'joint15x', 'joint15y', 
        'joint16x', 'joint16y', 
        'joint17x', 'joint17y'
    ]

    temp_df = pd.DataFrame(columns = df_columns)

    for fileName in os.listdir(path):
        img_id = fileName.strip(".jpg")
        img_data = data.get(img_id)
        keypoints = img_data['keypoints']
        temp_arr = []

        for arr in keypoints:
            temp_arr.append(arr[0])
            temp_arr.append(arr[1])
        
        temp_df.loc[len(temp_df.index)] = temp_arr
    
    temp_df.to_csv(store_file, header=True, index = False)

def main():
    print('Cleaning names of training dataset....')
    strip_names(TRAIN_PATH)

    print('\nCleaning names of validation dataset')
    strip_names(VAL_PATH)

    print('\nSplitting images into train and test dataset')
    split_images()
    organize()
    generate_test_annotation(ANNOTATION_PATH)

    TEST_DATA = json.load(open(TEST_ANNOTATION_PATH))

    print('\nResizing Training Images....')
    resize_images(TRAIN_PATH, SCALING_SIZE, TRAIN_ANNOTATION_PATH, TRAIN_DATA)
    
    print('\nResizing Validation Images....')
    resize_images(VAL_PATH, SCALING_SIZE, VAL_ANNOTATION_PATH, VAL_DATA)

    print('\nResizing Test Images....')
    resize_images(TEST_PATH, SCALING_SIZE, TEST_ANNOTATION_PATH, TEST_DATA)

    print("\nFetching keypoints for Training Images....")
    get_keypoints(TRAIN_PATH, TRAIN_DATA, os.path.join(RELATIVE_PATH, 'train/keypoints.csv'))

    print("\nFetching keypoints for Validation Images....")
    get_keypoints(VAL_PATH, VAL_DATA, os.path.join(RELATIVE_PATH, 'valid/keypoints.csv'))

    print("\nFetching keypoints for Test Images....")
    get_keypoints(TEST_PATH, TEST_DATA, os.path.join(RELATIVE_PATH, 'test/keypoints.csv'))

start = time.time()
main()
end = time.time()
print('Total Time Taken to prepare datasets:', round((end - start), 2), 'seconds')