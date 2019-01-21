# Standard library imports
import base64
import io
import os
import random
import string

# Third party imports
import cv2
import imutils
from imageio import imread
from imutils.object_detection import non_max_suppression
import numpy as np

class ImageProcessor(object):

    def __init__(self, encoded_image, image_name):
        self.encoded_image = encoded_image
        self.image_name  = image_name

    def image_decode(self, encoded_image):
        b64_decoded = base64.b64decode(encoded_image)
        # reconstruct image as an numpy array
        img = imread(io.BytesIO(b64_decoded))
        # finally convert RGB image to BGR for opencv
        # and save result
        cv2_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        return(cv2_img)

    def image_encode(self, image):
        # create a 10 char random dir name
        random_dir = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        cv2.imwrite("/tmp/"+random_dir+"_image.jpg",image)
        image = open("/tmp/"+random_dir+"_image.jpg", 'rb')
        image_read = image.read()
        encoded_image = base64.b64encode(image_read)
        os.remove("/tmp/"+random_dir+"_image.jpg")
        return(encoded_image)

    def detectPedestrians(self):
        # initialize the HOG descriptor/person detector
        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        image = self.image_decode(self.encoded_image)
        image = imutils.resize(image, width=min(400, image.shape[1]))
        orig = image.copy()

        # detect people in the image
        (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
            padding=(8, 8), scale=1.05)

        # draw the original bounding boxes
        for (x, y, w, h) in rects:
            cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # apply non-maxima suppression to the bounding boxes 
        rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
        pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

        # draw the final bounding boxes
        for (xA, yA, xB, yB) in pick:
            cv2.rectangle(image, (xA, yA), (xB, yB), (0, 0, 255), 2)
        encoded_image = self.image_encode(image)
        return(str(encoded_image.decode("utf-8")))
        # cv2.imshow("Pedestrian's Detected", image)
        # cv2.waitKey(0)
