import glob
import os
import cv2
import main

def getPath():
    my_path = os.getcwd()
    files_jpg = glob.glob(my_path + '\\dataFiles\\**\\*.jpg' , recursive=True)
    files_jpeg = glob.glob(my_path + '\\dataFiles\\**\\*.jpeg' , recursive=True)
    files_png = glob.glob(my_path + '\\dataFiles\\**\\*.png' , recursive=True)

    files = files_jpeg + files_jpg + files_png
    # print(files)

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