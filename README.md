# Brain Tumor Classification Application 

## **About**
This repository contains a Flask application that can be used to classify brain tumors from images submitted by the user. The flask application inherits a model
that was trained on a dataset of brain tumor images. The dataset classes are glioma, meningioma , no tumor, and pitutary. You can download the given dataset from [Here](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)

## **Dataset Information**
This dataset contains 7023 images of human brain MRI images which are classified into 4 classes: glioma, meningioma, no tumor, and pituitary.

## **Model Information**
The model followed a periodic sequence in terms of its implemented filters (notebook to the model can be found [Here](https://github.com/DouglasPrograms/Brain-Tumor-Classification-App/blob/main/Brain%20Tumor%20Recognition.ipynb))

The model was trained using the given dataset and achieved the following metrics:
* Categorical Accuracy: 96%
* F1 Score: 0.96

## **Requirements**
* Python v3.10.6
* Tensorflow v2.8.0
* Flask v2.3.2
* Pillow v9.1.1

## **Media**
![image1](https://i.postimg.cc/hPD7nt7s/image.png)

![image2](https://i.postimg.cc/15sYZwHd/image.png)

Video Coming Soon...

## **Installation**
1. Clone the given repository and use PyCharm to open and run the program.
2. Make sure you have all packages installed with the required version.
3. Make sure given the model's path is set to a path that exists within your file explorer.
4. Make sure images stay within the "static" directory, and make sure the "index.html" stays within the "templates" directory or else Flask will not be capable
to recognize the images and html page. 
5. Have fun with it.
