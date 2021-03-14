import cv2

def find_target():
    'returns the position of target'

    cam = cv2.VideoCapture(0)
    casc_path = "../Classifiers/haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(casc_path)

    #Attempts to grap a fram from the camera
    ret, frame = cam.read()
    
    if not ret: #failed to get frame
            print("failed to get frame")

    else: #succed in getting frame

        #gray scale the frame for processing
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #find first target in gray scaled frame
        target = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
        )




