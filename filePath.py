import glob
import os
import cv2
import main
import sys

def getPath(folder):

    if sys.platform.startswith('darwin') or sys.platform.startswith('linux') : # - elizabeth - my mac wasn't recognizing the regex in the elif 'win32' code
        my_path = os.getcwd()+'/dataFiles/'+folder+'/'
        files_jpg = glob.glob(my_path + '*.jpg' , recursive=True)
        files_jpeg = glob.glob(my_path + '*.jpeg' , recursive=True)
        files_png = glob.glob(my_path + '*.png' , recursive=True)

    elif sys.platform.startswith('win32'):
        my_path = os.getcwd()
        files_jpg = glob.glob(my_path + '\\dataFiles\\**\\*.jpg' , recursive=True)
        files_jpeg = glob.glob(my_path + '\\dataFiles\\**\\*.jpeg' , recursive=True)
        files_png = glob.glob(my_path + '\\dataFiles\\**\\*.png' , recursive=True)
    
    files = files_jpeg + files_jpg + files_png
    l = len(files)
    # files = sorted(files)
    
    # print(files)
    # print(len(files))

    return files, l

# For debugging without running the whole app

# my_path = os.getcwd()
# files_jpg = glob.glob(my_path + '\\dataFiles\\**\\*.jpg' , recursive=True)
# files_jpeg = glob.glob(my_path + '\\dataFiles\\**\\*.jpeg' , recursive=True)
# files_png = glob.glob(my_path + '\\dataFiles\\**\\*.png' , recursive=True)

# files = files_jpeg + files_jpg + files_png
# l = len(files)

# main.readImage(files, l)