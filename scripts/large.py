# parallalize this script on 3 cores for train, test and validation dataset
import os

# global variables
TRAIN_URL = 'http://images.cocodataset.org/zips/train2017.zip'
TEST_URL = 'http://images.cocodataset.org/zips/test2017.zip'
VAL_URL = 'http://images.cocodataset.org/zips/val2017.zip'

def download_train():
    os.system('curl -L -o "train2017.zip" ' + TRAIN_URL)
    os.system('unzip train2017.zip')
    os.system('rm -rf train2017.zip')
    os.system('cp train2017 ../data/train2017 -r')
    os.system('rm -rf train2017/')
    os.system("clear")
    print("TRAINING SET EXTRACTION COMPLETED")

def download_test():
    os.system('curl -L -o "test2017.zip" ' + TEST_URL)
    os.system('unzip test2017.zip')
    os.system('rm -rf test2017.zip')
    os.system('cp test2017 ../data/test2017 -r')
    os.system('rm -rf test2017/')
    os.system('clear')
    print('TESTING SET EXTRACTION COMPLETED')

def download_val():
    os.system('curl -L -o "val2017.zip" ' + VAL_URL)
    os.system('unzip val2017.zip')
    os.system('rm -rf val2017.zip')
    os.system('cp val2017 ../data/val2017 -r')
    os.system('rm -rf val2017/')
    os.system('clear')
    print('VALIDATION SET EXTRACTION COMPLETED')

download_train()
download_test()
download_val()