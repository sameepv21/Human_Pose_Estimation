import argparse
import gdown
import os
from multiprocessing import Process
import time

parser = argparse.ArgumentParser()
parser.add_argument(
    "-f",
    '--full',
    action='store_true',
    required=False,
    help='download the entire coco2017 keypoints dataset'
)

args = vars(parser.parse_args())

start = time.time()

if(args['full']):
    # Download the entire dataset
    TRAIN_URL = 'http://images.cocodataset.org/zips/train2017.zip'
    TEST_URL = 'http://images.cocodataset.org/zips/test2017.zip'
    VAL_URL = 'http://images.cocodataset.org/zips/val2017.zip'

    def download_train():
        os.system('curl -L -o "train2017.zip" ' + TRAIN_URL)
        print("EXTRACTING TRAINING SET.....")
        os.system('unzip train2017.zip >/dev/null')
        os.system('rm -rf train2017.zip')
        os.system('cp train2017 ../data/train2017 -r')
        os.system('rm -rf train2017/')
        os.system("clear")
        print("TRAINING SET EXTRACTED")

    def download_test():
        os.system('curl -L -o "test2017.zip" ' + TEST_URL)
        print("EXTRACTING TEST SET.....")
        os.system('unzip test2017.zip >/dev/null')
        os.system('rm -rf test2017.zip')
        os.system('cp test2017 ../data/test2017 -r')
        os.system('rm -rf test2017/')
        os.system('clear')
        print('TESTING SET EXTRACTED')

    def download_val():
        os.system('curl -L -o "val2017.zip" ' + VAL_URL)
        print("EXTRACTING VALIDATION SET.....")
        os.system('unzip val2017.zip >/dev/null')
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

else:
    # Default download the subset of the dataset
    URL = "https://drive.google.com/file/d/1lwt3smqdJ2-ZuVCzgImEp8gw-RHuG-YR/view"
    OUTPUT_FILE_NAME = "dataset.zip"
    gdown.download(URL, OUTPUT_FILE_NAME, quiet = False, fuzzy = True)

    # Extract the zip folder and place it in the data folder
    print("EXTRACTING.....")
    os.system("unzip dataset.zip > /dev/null")
    os.system('rm -rf dataset.zip')
    os.system('cp coco_single_person_only/train ../data  -r')
    os.system('cp coco_single_person_only/valid ../data  -r')
    os.system('rm -rf coco_single_person_only/')
    print("COMPLETED EXTRACTION")

end = time.time()
print("Time taken to download:", round((end - start), 2), "seconds")