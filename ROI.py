import cv2

def region_of_interest(faces, img_copy):

    for face in faces:
        x,y,w,h = face
        offset = 0
        face_section = img_copy[y-offset:y+h+offset, x-offset:x+w+offset]

    return face_section