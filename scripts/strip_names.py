import os

def strip_till_first_nonzero(fileName):
    for index, char in enumerate(fileName):
        if char != '0':
            break
        else:
            modified_fileName = fileName[index + 1:]
    
    return modified_fileName

def clean_names(path):
    for fileName in os.listdir(path):
        modified_filename = strip_till_first_nonzero(fileName)
        os.system('mv ' + path + '/' + fileName + ' ' + path + '/' + modified_filename)

clean_names('../data/train/images')
clean_names('../data/valid/images')