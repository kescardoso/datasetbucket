from collections import Counter
import numpy as np
import cv2 

def removeBlack(estimator_labels, estimator_cluster):
  
  
  # Check for black
  hasBlack = False
  
  # Get the total number of occurance for each color
  occurance_counter = Counter(estimator_labels)

  
  # Quick lambda function to compare to lists
  compare = lambda x, y: Counter(x) == Counter(y)
   
  # Loop through the most common occuring color
  for x in occurance_counter.most_common(len(estimator_cluster)):
    
    # Quick List comprehension to convert each of RBG Numbers to int
    color = [int(i) for i in estimator_cluster[x[0]].tolist() ]
    

    # Check if the color is [0,0,0] that if it is black

    # print(type(color))
    # print(color)

    r = color[0]
    g = color[1]
    b = color[2]

    hair = np.uint8([[[r,g,b]]])
    hair_hsv = cv2.cvtColor(hair, cv2.COLOR_RGB2HSV)

    # print(hair)
    # print(hair_hsv)

    l_ = np.array([0,0,0])
    h_ = np.array([255,255,10])

    mask = cv2.inRange(hair_hsv, l_, h_)
    
    if color not in mask:

      # delete the occurance
      del occurance_counter[x[0]]
      
      # remove the cluster 
      hasBlack = True
      estimator_cluster = np.delete(estimator_cluster,x[0],0)
      
      break


  return (occurance_counter,estimator_cluster,hasBlack)