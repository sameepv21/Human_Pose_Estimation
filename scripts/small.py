# Import libraries
import gdown
import os

# Required variables
URL = "https://drive.google.com/file/d/1lwt3smqdJ2-ZuVCzgImEp8gw-RHuG-YR/view"
OUTPUT_FILE_NAME = "dataset.zip"
gdown.download(URL, OUTPUT_FILE_NAME, quiet = False, fuzzy = True)

# Extract the zip folder and place it in the data folder
print("EXTRACTING.....")
os.system("unzip dataset.zip >/dev/null 2")
os.system('rm -rf dataset.zip')
os.system('cp coco_single_person_only ../data  -r')
os.system('rm -rf coco_single_person_only/')
print("COMPLETED EXTRACTION")