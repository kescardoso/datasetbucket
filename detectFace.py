import cv2

def draw_found_faces(detected, image, color: tuple):
    for (x, y, width, height) in detected:
        cv2.rectangle(
            image,
            (x, y),
            (x + width, y + height),
            color,
            thickness=2
        )

def detect_faces(img_path):
    # creating haar cascade classifier

    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
    
    # not in use
    profileCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_profileface.xml")

    # reading image
    img = cv2.imread(img_path)
   
    # reducing the size of image to a standard 256x256 image
    img = cv2.resize(img,(256,256))
    img_copy = img.copy()

    # converting to gray scale face (makes detection easier :D)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    front_faces = faceCascade.detectMultiScale(
        gray_img,
        scaleFactor=1.3,
        minNeighbors=5,
    )

    profile_faces = profileCascade.detectMultiScale(
        gray_img,
        scaleFactor=1.3,
        minNeighbors=5,
    )

    # Filter out profiles
    # profiles_not_front_faces = [x for x in profile_faces if x not in front_faces]

    # Draw rectangles around faces on the original, colored image
    draw_found_faces(front_faces, img, (0, 255, 0)) # RGB - green
    # draw_found_faces(profile_faces, img, (0, 0, 255)) # RGB - red

    # showing image + rectangle
    # cv2.imshow('image',img)

    #Wait for any key before image disappears
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return img_copy,front_faces