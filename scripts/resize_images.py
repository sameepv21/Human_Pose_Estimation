# Required libraries
import time
from PIL import Image
import os
import numpy as np
import json

start = time.time()

# Global variables
TRAIN_PATH = "../data/train/images"
TEST_PATH = "../data/test/images"
VAL_PATH = '../data/valid/images'

TRAIN_ANNOTATION_PATH = '../data/train/annotation.json'
TEST_ANNOTATION_PATH = '../data/test/annotation.json'
VAL_ANNOTATION_PATH = '../data/valid/annotation.json'

TRAIN_DATA = json.load(open(TRAIN_ANNOTATION_PATH))
VAL_DATA = json.load(open(VAL_ANNOTATION_PATH))
TEST_DATA = json.load(open(TEST_ANNOTATION_PATH))

SCALING_SIZE = (224, 224)


print('Processing Train images.....')
# Load and resize train image
for index, fileName in enumerate(os.listdir(TRAIN_PATH)):
    if index % 4000 == 0: # Give progress update after every 4000 images
        print('Processed', index, 'images')

    image_id = fileName.strip('.jpg')
    _image = Image.open(TRAIN_PATH + '/' + fileName)
    image_np = np.asarray(_image)

    # find the new scaling factor after the image resize
    row_scaling_factor = SCALING_SIZE[0] / image_np.shape[1]
    col_scaling_factor = SCALING_SIZE[1] / image_np.shape[0]

    # fetch keypoints, bbox and segmentation
    keypoints = np.array(TRAIN_DATA.get(image_id).get('keypoints'))
    bbox = np.array(TRAIN_DATA.get(image_id).get('bbox'))

    # resize keypoints
    keypoints[:, 0] = keypoints[:, 0] * row_scaling_factor
    keypoints[:, 1] = keypoints[:, 1] * col_scaling_factor
    
    # print("\nImage shape", image_np.shape)
    # print("Row Scaling Factor", row_scaling_factor)
    # print("Col Scaling Factor", col_scaling_factor)

    # resize bbox
    bbox[0] = int(bbox[0] * row_scaling_factor)
    bbox[1] = int(bbox[1] * col_scaling_factor)
    bbox[2] = int(bbox[2] * row_scaling_factor)
    bbox[3] = int(bbox[3] * col_scaling_factor)

    # save it to the json
    TRAIN_DATA.get(image_id)['keypoints'] = keypoints.tolist()
    TRAIN_DATA.get(image_id)['bbox'] = bbox.tolist()

    _image = _image.resize(SCALING_SIZE)
    os.system("rm -rf " + os.path.join(TRAIN_PATH, fileName))
    _image.save(os.path.join(TRAIN_PATH, fileName))

# save json to file
train_object = json.dumps(TRAIN_DATA)
with open(TRAIN_ANNOTATION_PATH, 'w') as outfile:
    outfile.write(train_object)
print('Completed Train images.')


print('\nProcessing Test images.....')
# Load and resize test image
for index, fileName in enumerate(os.listdir(TEST_PATH)):
    if index % 4000 == 0: # Give progress update after every 4000 images
        print('Processed', index, 'images')

    image_id = fileName.strip('.jpg')
    _image = Image.open(TEST_PATH + '/' + fileName)
    image_np = np.asarray(_image)

    # find the new scaling factor after the image resize
    row_scaling_factor = SCALING_SIZE[0] / image_np.shape[1]
    col_scaling_factor = SCALING_SIZE[1] / image_np.shape[0]

    # fetch keypoints, bbox and segmentation
    keypoints = np.array(TEST_DATA.get(image_id).get('keypoints'))
    bbox = np.array(TEST_DATA.get(image_id).get('bbox'))

    # resize keypoints
    keypoints[:, 0] = keypoints[:, 0] * row_scaling_factor
    keypoints[:, 1] = keypoints[:, 1] * col_scaling_factor
    
    # print("\nImage shape", image_np.shape)
    # print("Row Scaling Factor", row_scaling_factor)
    # print("Col Scaling Factor", col_scaling_factor)

    # resize bbox
    bbox[0] = int(bbox[0] * row_scaling_factor)
    bbox[1] = int(bbox[1] * col_scaling_factor)
    bbox[2] = int(bbox[2] * row_scaling_factor)
    bbox[3] = int(bbox[3] * col_scaling_factor)

    # save it to the json
    TEST_DATA.get(image_id)['keypoints'] = keypoints.tolist()
    TEST_DATA.get(image_id)['bbox'] = bbox.tolist()

    _image = _image.resize(SCALING_SIZE)
    os.system("rm -rf " + os.path.join(TEST_PATH, fileName))
    _image.save(os.path.join(TEST_PATH, fileName))

# save json to file
test_object = json.dumps(TEST_DATA)
with open(TEST_ANNOTATION_PATH, 'w') as outfile:
    outfile.write(test_object)
print('Completed Test images.')


print('\nProcessing Validation images.....')
# Load and resize validation image
for index, fileName in enumerate(os.listdir(VAL_PATH)):
    if index % 4000 == 0: # Give progress update after every 4000 images
        print('Processed', index, 'images')

    image_id = fileName.strip('.jpg')
    _image = Image.open(VAL_PATH + '/' + fileName)
    image_np = np.asarray(_image)

    # find the new scaling factor after the image resize
    row_scaling_factor = SCALING_SIZE[0] / image_np.shape[1]
    col_scaling_factor = SCALING_SIZE[1] / image_np.shape[0]

    # fetch keypoints, bbox and segmentation
    keypoints = np.array(VAL_DATA.get(image_id).get('keypoints'))
    bbox = np.array(VAL_DATA.get(image_id).get('bbox'))

    # resize keypoints
    keypoints[:, 0] = keypoints[:, 0] * row_scaling_factor
    keypoints[:, 1] = keypoints[:, 1] * col_scaling_factor
    
    # print("\nImage shape", image_np.shape)
    # print("Row Scaling Factor", row_scaling_factor)
    # print("Col Scaling Factor", col_scaling_factor)

    # resize bbox
    bbox[0] = int(bbox[0] * row_scaling_factor)
    bbox[1] = int(bbox[1] * col_scaling_factor)
    bbox[2] = int(bbox[2] * row_scaling_factor)
    bbox[3] = int(bbox[3] * col_scaling_factor)

    # save it to the json
    VAL_DATA.get(image_id)['keypoints'] = keypoints.tolist()
    VAL_DATA.get(image_id)['bbox'] = bbox.tolist()

    _image = _image.convert('RGB').resize(SCALING_SIZE)
    os.system("rm -rf " + os.path.join(VAL_PATH, fileName))
    _image.save(os.path.join(VAL_PATH, fileName))

# save json to file
val_object = json.dumps(VAL_DATA)
with open(VAL_ANNOTATION_PATH, 'w') as outfile:
    outfile.write(val_object)
print('Completed Validation images.')

end = time.time()
print("Time taken to resize:", round((end - start), 2),"seconds")