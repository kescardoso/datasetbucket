import glob
import os
import cv2
import main
import sys
#/Users/mac/IdeaProjects/datasetbucket/dataFiles/profilesPics/01.jpg
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
    print(files)
# img = cv2.imread(files[0])
# cv2.imshow("hi", img)
# print(files[0])
# for f in files:
#     print(f)
    print(len(files))
    return files
#Wait for any key before image disappears
# cv2.waitKey(0)
# cv2.destroyAllWindows()

my_path = os.getcwd()
files_jpg = glob.glob(my_path + '\\datafiles_\\**\\*.jpg' , recursive=True)
files_jpeg = glob.glob(my_path + '\\datafiles_\\**\\*.jpeg' , recursive=True)
files_png = glob.glob(my_path + '\\datafiles_\\**\\*.png' , recursive=True)

files = files_jpeg + files_jpg + files_png
print(len(files))

main.readImage(files)