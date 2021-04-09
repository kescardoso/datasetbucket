import numpy as np
import cv2
from matplotlib import pyplot as plt

colors = []

# results = [total images, mean_color image, values less then mean val, values more than mean val]

# mean = sum of all terms / number of terms

# variance = value^2 - mean^2


def addToList(l):
    colors.append(l)

def printList():
    print(colors)
    print(len(colors))

def stats():

    variance = []
    idx = 0
    
    # mean:
    sum_of_terms = np.array([0, 0, 0])
    
    for l in colors:
        sum_of_terms += l

    mean_of_terms = sum_of_terms/len(colors)


    b = int(mean_of_terms[0])
    g = int(mean_of_terms[1])
    r = int(mean_of_terms[2])

    mean_color = np.uint8([[[b,g,r]]])
    
    mean_color = cv2.cvtColor(mean_color, cv2.COLOR_BGR2RGB)
    cv2.imwrite("mean_color.jpg", mean_color)
