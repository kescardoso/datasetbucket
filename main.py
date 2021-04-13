import numpy as np
import cv2
import os
from matplotlib import pyplot as plt
import shutil
import sys

import detectFace
import extractDominantColor
import extractSkin
import getColorInformation
import imageCalculations
import plot
import ROI

import generatePDF
import passToPDF


def readImage(f, l, targetReportPath):


  print("main")
      
  N = 5
  data = []
  dataResultsCSV = {}
  dataResultsJSON = {}
  dataResultsIMG = {}
  names = []
  


  # for root, directories, files in path:
  # for 
  for filename in f:

    img_path = filename 
    # if '.png' or '.jpeg' or '.jpg' in filename:
    img_copy,faces = detectFace.detect_faces(img_path = img_path)
               
    # if the faces are detected by the haarcascade files
    if len(faces) != 0:
      image = ROI.region_of_interest(faces = faces, img_copy = img_copy)

    # if the faces are not detected by the haarcascade files, we will try to detect the skin
    else:
      image = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)

    # Resize image to a width of 250

    scale_percent = 50
    
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)

    dsize = (width, height)

    #Show image
    # plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
    # plt.show()

    # Apply Skin Mask
    skin = extractSkin.extractSkin(image = image)
    # plt.imshow(cv2.cvtColor(skin,cv2.COLOR_BGR2RGB))
    # plt.show()

    # Find the dominant color. Default is 1 , pass the parameter 'number_of_colors=N' where N is the specified number of colors 
    dominantColors = extractDominantColor.extractDominantColor(skin, number_of_colors = N, hasThresholding=True)

    #Show in the dominant color information
    # print("Color Information")
    # plot.prety_print_data(dominantColors)

    #Show in the dominant color as bar
    # print("Color Bar")

    color_bar = plot.plotColorBar(dominantColors)

    colors = []
    for clr in dominantColors:
      colors.append(clr['color'])
    
    if len(colors) != 0:
      c = colors[0]

      b = int(c[0])
      g = int(c[1])
      r = int(c[2])
    
    else:
      # cases where color is not detected, we set it default (white)
      b = int(255)
      g = int(255)
      r = int(255)

    c = np.array([b,g,r])
    
    # adding the most dominant color to a list for doing statistical analysis
    imageCalculations.addToList(l = c)

    # skin color to test
    skinColor = np.uint8([[[b,g,r]]])    

    skinColorHSV = cv2.cvtColor(skinColor,cv2.COLOR_BGR2HSV)
    temp = skinColorHSV[0]
    temp = temp[0]
        
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    

    #Show the dominant color information
    info = plot.prety_print_data(dominantColors)
    
    # dominantColors:[{'cluster_index: int, 'color':[float,float,float], 'color_percentage': float} x N]

    info = "             "
    # clrs = []
    colour_bar = plot.plotColorBar(dominantColors)
    for clr in dominantColors:

      # clrs.append(color)
      per_age = clr['color_percentage']
      info += str(int(per_age*100)) + "%" + " "

    # print(clrs)
    # plt.axis("off")
    # plt.imshow(colour_bar)
    # plt.show()
    # print('info in main.py line 139', info)
    
    imgName = filename[:-4] +  "_res.jpg"
    colour_bar = cv2.cvtColor(colour_bar, cv2.COLOR_BGR2RGB)
    cv2.imwrite(imgName, colour_bar)

    
    
    ## (Maybe Instead of profileImage pass the statistical data to pdf)
    imageCalculations.stats()
    analysis = l

    # info = dominantColors
    colorBar = imgName
    names.append(colorBar)
    # colorBar = cv2.cvtColor(colorBar, cv2.COLOR_BGR2RGB)

    data.append(passToPDF.createData(analysis, info, colorBar))

  reportMade, nameOfReport = generatePDF.generatePDFReport(targetReportPath, None, None, dataResultsCSV, dataResultsJSON, dataResultsIMG = data)

  
  # imageCalculations.printList()
  
  
  for f in names:
    os.remove(f)

  os.remove('mean_color.jpg')

  return reportMade, nameOfReport
