# Required libraries
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

def main():
    split_images()
    organize()
    generate_test_annotation(ANNOTATION_PATH)

main()