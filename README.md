# Birds Recognition
 This Github contains all codes and data used and created for our 3rd Semester Project at IMT Atlantique. This project answers to a request of Lorient Agglomeration, that is to test if Machine Learning can be used in order to help the study of birds in a mudflat.
 

# Classification
It is the part of the project that aims at identifying the species of a bird on a photo. You will find 2 folders in it. One contains the code that we used to do classification with YOLO, and the other contains the code and Data used with Resnet_18. You will also find the code that we used for Data_Augmentation.

The folders Train, Test and Valid contain the photos of birds alone classified by species in order to be used for the Train, Validation and Test phases of our algorithm training.

The file DataAugmentation's purpose is to improve our Dataset by adding new version of the images in it. These new version are obtained by turning the images or changing their brightness.

The file SpeciesClassification contains the definition of the neural network, and it's training, with some results representation.

# Detection
It is the part of the project that aims at detecting birds on a picture, and create boxes, each one containing one bird.

# Researches
This folder contains the 3 docs that sum up our work for Lorient Agglomérarion. The purpose was to test if Deep Learning methods could be useful in order to help the study of birds in a mudflat.

# Web_Scraping
This contains the tutorial to follow in order to get images from the internet with Web_Scraping.