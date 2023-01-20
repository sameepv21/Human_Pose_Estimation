import os
from multiprocessing import Process

# global variables
TRAIN_URL = 'http://images.cocodataset.org/zips/train2017.zip'
TEST_URL = 'http://images.cocodataset.org/zips/test2017.zip'
VAL_URL = 'http://images.cocodataset.org/zips/val2017.zip'

def download_train():
    os.system('curl -L -o "train2017.zip" ' + TRAIN_URL)
    print("EXTRACTING TRAINING SET.....")
    os.system('unzip train2017.zip >/dev/null 2')
    os.system('rm -rf train2017.zip')
    os.system('cp train2017 ../data/train2017 -r')
    os.system('rm -rf train2017/')
    os.system("clear")
    print("TRAINING SET EXTRACTED")

def download_test():
    os.system('curl -L -o "test2017.zip" ' + TEST_URL)
    print("EXTRACTING TEST SET.....")
    os.system('unzip test2017.zip >/dev/null 2')
    os.system('rm -rf test2017.zip')
    os.system('cp test2017 ../data/test2017 -r')
    os.system('rm -rf test2017/')
    os.system('clear')
    print('TESTING SET EXTRACTED')

def download_val():
    os.system('curl -L -o "val2017.zip" ' + VAL_URL)
    print("EXTRACTING VALIDATION SET.....")
    os.system('unzip val2017.zip >/dev/null 2')
    os.system('rm -rf val2017.zip')
    os.system('cp val2017 ../data/val2017 -r')
    os.system('rm -rf val2017/')
    os.system('clear')
    print('VALIDATION SET EXTRACTED')


########### Execute in main thread #############
if __name__ == '__main__':
    process_arr = []
    p = Process(target = download_train)
    process_arr.append(p)
    p.start()

    p = Process(target = download_val)
    process_arr.append(p)
    p.start()

    p = Process(target = download_test)
    process_arr.append(p)
    p.start()

    for p in process_arr:
        p.join()