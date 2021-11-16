#!/usr/bin/env python3
'''opencv module tests'''
import sys
import os
import inspect

import logging
logger = logging.getLogger('OPENCV')

import cv2
import numpy as np

def me_modules_opencv(args=None):
    logger.info("me_modules_opencv")

    if args:
        print(vars(args))
        logger.info(vars(args))

    #vid_test(args)



    # https://www.geeksforgeeks.org/face-detection-using-python-and-opencv-with-webcam/
    webcam_create_data(args)
    webcam_face_recognize(args)

def webcam_create_data(args):

    module_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    input_dir = module_dir + "/../../input"
    output_dir = module_dir + "/../../output"

    # Creating database
    # It captures images and stores them in datasets
    # folder under the folder name of sub_data
    haar_file = input_dir + '/haarcascade_frontalface_default.xml'

    # All the faces data will be
    # present this folder
    datasets = output_dir + '/datasets'
    if not os.path.isdir(datasets):
        os.mkdir(datasets)


    # These are sub data sets of folder,
    # for my faces I've used my name you can
    # change the label here
    sub_data = 'me'	

    path = os.path.join(datasets, sub_data)
    if not os.path.isdir(path):
        os.mkdir(path)

    # defining the size of images
    (width, height) = (130, 100)

    #'0' is used for my webcam,
    # if you've any other camera
    # attached use '1' like this
    face_cascade = cv2.CascadeClassifier(haar_file)
    webcam = cv2.VideoCapture(0)

    # The program loops until it has 30 images of the face.
    count = 1
    while count < 500:
        (_, im) = webcam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face = gray[y:y + h, x:x + w]
            face_resize = cv2.resize(face, (width, height))
            cv2.imwrite('% s/% s.png' % (path, count), face_resize)
        count += 1
        
        cv2.imshow('OpenCV', im)
        key = cv2.waitKey(10)
        if key == 27:
            break

def webcam_face_recognize(args):

    module_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    input_dir = module_dir + "/../../input"
    output_dir = module_dir + "/../../output"

    # It helps in identifying the faces
    size = 4
    haar_file = input_dir + '/haarcascade_frontalface_default.xml'

    datasets = output_dir + '/datasets'
    if not os.path.isdir(datasets):
        os.mkdir(datasets)
    
    # Part 1: Create fisherRecognizer
    print('Recognizing Face Please Be in sufficient Lights...')

    # Create a list of images and a list of corresponding names
    (images, labels, names, id) = ([], [], {}, 0)
    for (subdirs, dirs, files) in os.walk(datasets):
        for subdir in dirs:
            names[id] = subdir
            subjectpath = os.path.join(datasets, subdir)
            for filename in os.listdir(subjectpath):
                path = subjectpath + '/' + filename
                label = id
                images.append(cv2.imread(path, 0))
                labels.append(int(label))
            id += 1
    (width, height) = (130, 100)

    # Create a Numpy array from the two lists above
    (images, labels) = [np.array(lis) for lis in [images, labels]]

    # OpenCV trains a model from the images
    # NOTE FOR OpenCV2: remove '.face'
    model = cv2.face.LBPHFaceRecognizer_create()
    model.train(images, labels)

    # Part 2: Use fisherRecognizer on camera stream
    face_cascade = cv2.CascadeClassifier(haar_file)
    webcam = cv2.VideoCapture(0)
    while True:
        (_, im) = webcam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face = gray[y:y + h, x:x + w]
            face_resize = cv2.resize(face, (width, height))
            # Try to recognize the face
            prediction = model.predict(face_resize)
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)

            if prediction[1]<500:
                cv2.putText(im, '% s - %.0f' % (names[prediction[0]], prediction[1]), (x-10, y-10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
            else:
                cv2.putText(im, 'not recognized', (x-10, y-10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))

        cv2.imshow('OpenCV', im)
        
        key = cv2.waitKey(10)
        if key == 27:
            break

def vid_test(args=None):
    cap = cv2.VideoCapture(0)
    
    # Check if camera opened successfully
    if (cap.isOpened()== False):
        print("Error opening video  file")
    
    # Read until video is completed
    while(cap.isOpened()):
        
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
    
            # Display the resulting frame
            cv2.imshow('Frame', frame)
        
            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        
        # Break the loop
        else: 
            break
        
    # When everything done, release 
    # the video capture object
    cap.release()
    
    # Closes all the frames
    cv2.destroyAllWindows()
