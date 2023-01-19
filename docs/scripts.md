# Purpose
The purpose of the script folder is to contain the python script for download the datasets based on the user's choice of whether he or she wants to donwload the entire dataset or just a small subset of the dataset.

# Working
For smaller subset of the dataset, the dataset is downloaded from google drive. Once the dataset is downloaded, there is a small script to extract and place it in the proper folder to get used by the rest of the project.

For the entire dataset, the process has been parallelized so that simultaneously all the three datasets get downloaded, extracted and saved in the required folder to get used by the rest of the project.

# Libraries Used
* os - For runnning system level commands
* multiprocessing - For parallelizing the extraction of the entire dataset.
* gdown - For downloading the subset of data from google drive.