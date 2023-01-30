# Purpose
The following file contains already exisitng pre-trained architectures. It mentions about their performance, their approach used (eg. regression based or heatmap based etc.), their limitations etc. Finally, based on their individual performance and limitations, a combination of model and approach would be selected to be the baseline before fine-tuning and would serve as a comparision model.

# Single-Person HPE

## Regression Based

### DeepPose
* Approach - AlexNet and a cascaded deep neural network regressor.

### Iterative Error Feedback
* Approach - GoogleNet and a feedback mechanism for self-correcting model

### Compositional Pose Regression
* Approach - ResNet and a bone based structure instead of joints based images

### HPE using softargmax function
* Approach - SoftArgMax function to directly convert feature maps into joint coordinates.

### PRTR
* Approach - Cascaded transformer-based model.

### Multi-Task Learning
* Approach 1 - Two tasks i.e predicting joints coordinates from full images by a regressor and detecting body parts from image patches using a sliding window. 
* Approach 2 - Two sources i.e joint detection (determines whether a pathc contains a body joint) and joint localization (find exact location of the joint in the patch)

## Heatmap Based

### Spatial model
* Approach - CNN with body part detector incorporating keypoints votes and join probablities.

### Convolutional Pose Machines (CPM)
* Approach - CNN-based sequential framework to predict the locations of key joints with multi-stage processing.

### Stacked Hourglass and Variations
* Main Approach - Consists of consecutive steps of pooling and upsampling layers to capture information.
* Variant 1 - Hourglass residual units
* Variant 2 - Multibranch pyramid residual module
* Variant 3 - Structure-aware conditional GAN and passed through an hourglass network-based pose generator and two discriminators
* Variant 4 - Two stacked hourglass with shared GAN