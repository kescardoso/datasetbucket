import cv2
import getColorInformation
from sklearn.cluster import KMeans
import warnings


def extractDominantColor(image,number_of_colors,hasThresholding=False):
  
  # Quick Fix Increase cluster counter to neglect the black(Read Article) 
  if hasThresholding == True:
    number_of_colors +=1
  
  # Taking Copy of the image
  img = image.copy()
  
  # Convert Image into RGB Colours Space
  img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
  
  # Reshape Image
  img = img.reshape((img.shape[0]*img.shape[1]) , 3)
  
  #Initiate KMeans Object
  estimator = KMeans(n_clusters=number_of_colors, random_state=0)
  
  # Fit the image
  with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    # cluster_data(data_arr)
    estimator.fit(img)
  
  # Get Colour Information
  colorInformation = getColorInformation.getColorInformation(estimator.labels_,estimator.cluster_centers_,hasThresholding)
  return colorInformation