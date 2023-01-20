import numpy as np
import json

# Function to display menu to the user
def menu():
    _input = 0
    while(_input not in [1, 2, 3, 4]):
        print("============= Select One of the following ==============")
        print('1. Train Set Annotations')
        print('2. Validation Set Annotations')
        print('3. Testing Set Annotations')
        print('4. Exit')
        try:
            _input = int(input("Select process: "))
            if(_input not in [1, 2, 3, 4]):
                print("Invalid Selection")
            else:
                return _input
        except:
            print("Invalid Selection")

# Function to process the json file and fetch only the required records
def annotate(path):
    # open the json file
    with open(path) as json_file:
        data = json.load(json_file)

    arr_json = [] # final array for storing records for all the images
    len_flag = 0 # assertion flag for checking if the number of images in the JSON file and array are same or not
    for img_data in data.get('annotations'):
        cleaned_data = {} # temp dict for individual image
        len_flag += 1
        cleaned_data['image_id'] = img_data.get('image_id')
        cleaned_data['bbox'] = img_data.get('bbox')
        
        # create a 17x3 matrix instead of 51,1
        keypoints_arr = img_data.get('keypoints')
        processed_keypoints = np.empty(shape = (17, 3)) # 17x3 matrix
        count = 0
        for index in range(0, 52, 3):
            temp_arr = keypoints_arr[index:index + 3]
            if(len(temp_arr) > 0):
                processed_keypoints[count] = temp_arr
                count += 1
        cleaned_data['keypoints'] = processed_keypoints.tolist()

        cleaned_data['category_id'] = img_data.get('category_id')
        cleaned_data['segmentation'] = img_data.get('segmentation')
        arr_json.append(cleaned_data)

    # assertion
    if(len(arr_json) == len_flag):
        return arr_json
    else:
        print("Something went wrong!")

# function to save the output of into the json file
def save(final_json, path):
    path = path[:-5]
    path += "_processed.json"
    # serialize the json
    json_object = json.dumps(final_json)

    # save to file
    with open(path, 'w') as outfile:
        outfile.write(json_object)

# wrapper function that calls and coordinates others
def main():
    task = 0
    while(task != 4):
        task = menu()
        path = ""
        if task == 1:
            path = input("Enter the complete path for training json file: ")
        elif task == 2:
            path = input('Enter the complete path for validation json file: ')
        elif task == 3:
            path = input('Enter the complete path for test json file: ')
        
        if(task != 4):
            print('Processing...')
            processed_json = annotate(path)
            save(processed_json, path)
            print('Processing Completed')

main()