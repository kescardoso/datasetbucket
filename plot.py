import cv2
# from matplotlib import pyplot as plt
import numpy as np
import pprint

colors = []
  
def plotColorBar(colorInformation):

  colors = []
  #Create a 500x100 black image
  color_bar = np.zeros((100,500,3), dtype="uint8")
  
  top_x = 0
  for x in colorInformation:    
    bottom_x = top_x + (x["color_percentage"] * color_bar.shape[1])

    color = tuple(map(int,(x['color'])))

    colors.append(list(color))
    # print(colors)

    cv2.rectangle(color_bar , (int(top_x),0) , (int(bottom_x),color_bar.shape[0]) ,color , -1)
    top_x = bottom_x
  return color_bar 

def prety_print_data(color_info):
  for x in color_info:
    # print(pprint.pformat(x))
    text = str(pprint.pformat(x))
    # print()
    return text
    