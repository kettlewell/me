#!/usr/bin/env python3
'''opencv module tests'''
import sys
import os
import inspect

import logging
logger = logging.getLogger('OPENCV')

import cv2
import numpy as np

import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib import ticker
from matplotlib.colors import LinearSegmentedColormap

def me_modules_opencv(args=None):
    logger.info("me_modules_opencv")

    if args:
        print(vars(args))
        logger.info(vars(args))

    #vid_test(args)

    NIRPlantVideoTracking(args)

    # https://www.geeksforgeeks.org/face-detection-using-python-and-opencv-with-webcam/
    #webcam_create_data(args)
    #webcam_face_recognize(args)

    # nieve approach to getting a list of webcam ids
    # https://stackoverflow.com/a/62639343
    #list_cams(args)

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
    sub_data = 'me2'	

    path = os.path.join(datasets, sub_data)
    if not os.path.isdir(path):
        os.mkdir(path)

    # defining the size of images
    (width, height) = (130, 100)

    #'0' is used for my webcam,
    # if you've any other camera
    # attached use '1' like this
    face_cascade = cv2.CascadeClassifier(haar_file)
    webcam = cv2.VideoCapture(2)
    cv2.normalize()

    # The program loops until it has 30 images of the face.
    count = 1
    while count < 50:
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
    webcam = cv2.VideoCapture(2)
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


def list_cams(args):
    """Test the ports and returns a tuple with the available ports and the ones that are working."""
    is_working = True
    dev_port = 0
    working_ports = []
    available_ports = []
    max_ports = 20
    while dev_port < max_ports:
        try:
            camera = cv2.VideoCapture(dev_port)
            if camera.isOpened():
            #    is_working = False
            #    print("Port %s is not working." %dev_port)
            #else:
                is_reading, img = camera.read()
                w = camera.get(3)
                h = camera.get(4)
                if is_reading:
                    print("Port %s is working and reads images (%s x %s)" %(dev_port,h,w))
                    working_ports.append(dev_port)
                else:
                    print("Port %s for camera ( %s x %s) is present but does not reads." %(dev_port,h,w))
                    available_ports.append(dev_port)
        except:
            a,b,c = sys.exc_info()
            print(a)
            print(b)
            print(c)

        dev_port +=1
    return available_ports,working_ports



# from: https://github.com/MuonRay/Image-VideoSegmentationinNIRforPlantDetection/blob/master/NIRPlantVideoTracking.py

def NIRPlantVideoTracking(args):

    cap = cv2.VideoCapture(0)

    #custom colormap for ndvi greyscale video
    cols3 = ['gray', 'blue', 'green', 'yellow', 'red']

    def create_colormap(args):
        return LinearSegmentedColormap.from_list(name='custom1', colors=cols3)

    #colour bar to match grayscale units
    def create_colorbar(fig, image):
            position = fig.add_axes([0.125, 0.19, 0.2, 0.05])
            norm = colors.Normalize(vmin=-1., vmax=1.)
            cbar = plt.colorbar(image,
                                cax=position,
                                orientation='horizontal',
                                norm=norm)
            cbar.ax.tick_params(labelsize=6)
            tick_locator = ticker.MaxNLocator(nbins=3)
            cbar.locator = tick_locator
            cbar.update_ticks()
            cbar.set_label("NDVI", fontsize=10, x=0.5, y=0.5, labelpad=-25)



    while(1):

        # Take each frame
        _, frame = cap.read()

        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # define range of red NIR vegetation color in HSV
        low_red = np.array([160, 105, 84])
        high_red = np.array([179, 255, 255])

        # Threshold the HSV image to get only red colors
        mask = cv2.inRange(hsv, low_red, high_red)

        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(frame,frame, mask= mask)
        
        
        #NDVI Processing
        ir = (res[:,:,0]).astype('float')
        r = (res[:,:,2]).astype('float')
        
        ndvi = np.true_divide(np.subtract(ir, r), np.add(ir, r))
        
        cols3 = ['gray', 'blue', 'green', 'yellow', 'red']
        
        def create_colormap(args):
            return LinearSegmentedColormap.from_list(name='custom1', colors=cols3)
        
        #colour bar to match grayscale units
        def create_colorbar(fig, image):
            position = fig.add_axes([0.125, 0.19, 0.2, 0.05])
            norm = colors.Normalize(vmin=-1., vmax=1.)
            cbar = plt.colorbar(image,
                                cax=position,
                                orientation='horizontal',
                                norm=norm)
            cbar.ax.tick_params(labelsize=6)
            tick_locator = ticker.MaxNLocator(nbins=3)
            cbar.locator = tick_locator
            cbar.update_ticks()
            cbar.set_label("NDVI", fontsize=10, x=0.5, y=0.5, labelpad=-25)

        
        
        image = plt.imshow(ndvi, cmap=create_colormap(colors))
        #plt.axis('off')
        #image = cv2.imshow(ndvi, cmap=create_colormap(colors))


        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)
        

        #this step adds considerable processing, be sure to use only 720p files at most a minute long
        #cv2.imshow('ndvi',ndvi)
        
        cv2.imshow('ndvi with color', ndvi)




        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()