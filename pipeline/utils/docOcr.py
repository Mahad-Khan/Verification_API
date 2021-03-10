import numpy as np
import cv2
import imutils
from imutils.object_detection import non_max_suppression
import pytesseract
from matplotlib import pyplot as plt
import pandas as pd
import math
import re


def preprocess_and_ocr(path, ground_truth_list):
    """
    :param path: path to document image.
    :param ground_truth_list: list of strings that the OCR is searching for...
    
    [ex]: ground_truth_list = ["firstname", "lastname", "address item", "city", "state", "zipcode", "MM-DD-YYYY"]
    
    :return: a list of a matches or failure messages whose index positions correspond to the index position of 
             each item in the ground_truth_list
    """
    extractions = []
    
    img = cv2.imread(path)
    

    
    data = pytesseract.image_to_string(img, config="--psm 11")
    
    for item in ground_truth_list:
        starting_point = data.find(item)
        if starting_point != []:
            item_length = len(item)
        
            item_discovered = data[starting_point:starting_point + item_length]
            extractions.append(item_discovered)
        else:
            extractions.append()
            
        
    return extractions