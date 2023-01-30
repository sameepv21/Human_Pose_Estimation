# Required libraries
import time
from PIL import Image
import os

start = time.time()

# Global variables
TRAIN_PATH = "../data/train/images"
TEST_PATH = "../data/test/images"
VAL_PATH = '../data/valid/images'
SCALING_SIZE = (224, 224)

print('Processing Train images.....')
# Load and resize train image
for index, fileName in enumerate(os.listdir(TRAIN_PATH)):
    if index % 4000 == 0:
        print('Processed', index, 'images')
    _image = Image.open(TRAIN_PATH + '/' + fileName)
    _image = _image.resize(SCALING_SIZE)
    os.system("rm -rf " + os.path.join(TRAIN_PATH, fileName))
    _image.save(os.path.join(TRAIN_PATH, fileName))
print('Completed Train images.....')


print('\nProcessing Test images.....')
# Load and resize test image
for index, fileName in enumerate(os.listdir(TEST_PATH)):
    if index % 4000 == 0:
        print('Processed', index, 'images')
    _image = Image.open(TEST_PATH + '/' + fileName)
    _image = _image.resize(SCALING_SIZE)
    os.system("rm -rf " + os.path.join(TEST_PATH, fileName))
    _image.save(os.path.join(TEST_PATH, fileName))
print('Completed Test images.....')


print('\nProcessing Validation images.....')
# Load and resize validation image
for index, fileName in enumerate(os.listdir(VAL_PATH)):
    if index % 4000 == 0:
        print('Processed', index, 'images')
    _image = Image.open(VAL_PATH + '/' + fileName)
    _image = _image.resize(SCALING_SIZE)
    os.system("rm -rf " + os.path.join(VAL_PATH, fileName))
    _image.save(os.path.join(VAL_PATH, fileName))
print('Completed Validation images.....')

end = time.time()
print("Time taken to resize:", round((end - start), 2),"seconds")