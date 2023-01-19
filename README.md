# Project Description
The project aims at implementing the state-of-the-art (SOTA) human pose estimation (a computer vision task that involves detecting the position and oritentation of a person's body in an image or video). The application of this project includes a myriad number of things spanning from ADAS to Action recognition.

The purpose of this project is to identify and locate key points, such as the joints and body parts, of a person in an image or video.

# Prerequisites
* The project is build on Python version 3.8.10. Please ensure that you have Python version 3.8.10 or later installed on your device.
* Even though this project was run on Ubuntu 20.04, it should run fine with any distro of linux.
* There are two options of dataset. One is entire COCO 2017 keypoints dataset which requires a total of 45GB of disk space after unzipping and the other contains a subset of the dataset which requires around 4GB of the storage.

# Installation and Running


* Clone the repository using the below command
```bash
git clone https://github.com/sameepv21/Human_Pose_Estimation.git
```
* Install the python dependencies that are required.
```bash
pip install -r requirements.txt
```
* Create a directory named "data"
```bash
mkdir data
```
* Now there are two options, either you want to download the 
* Download and extract the subset of data
```bash
cd scripts/
python small.py
```
* Check once in the "data" folder whether you have a directory named "small".
* Download and extract the entire dataset
```bash
cd scripts/
python large.py
```