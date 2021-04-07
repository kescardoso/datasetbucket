import cv2

def region_of_interest(faces, img_copy):

    for face in faces:
        x,y,w,h = face
        offset = 0
        face_section = img_copy[y-offset:y+h+offset, x-offset:x+w+offset]

    # showing region of interest   
    # cv2.imshow('Region of Interest',face_section)

    return face_section