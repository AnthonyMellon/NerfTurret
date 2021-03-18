import cv2

cam = cv2.VideoCapture(0)
casc_path = "../Classifiers/haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(casc_path)

def find_target():
    'returns the position of target'

    #Attempts to grap a fram from the camera
    ret, frame = cam.read()
    
    if not ret: #failed to get frame
        print("failed to get frame")

    else: #succed in getting frame

        #gray scale the frame for processing
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #find all targets in gray scaled frame
        targets = face_cascade.detectMultiScale(
            gray_frame,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
        )

        #Draw a rectangle around each target    
        for(x, y, w, h) in targets:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)            

        #Get first target, if there is one
        if targets.all():
            target = targets[0]
 
        #Show the tragets
        cv2.imshow("Faces!", frame)  

        return(target[0], target[1])      

def main():
    loop = True
    while loop:

        #Get the position of the target in screen space
        point = find_target()
        print(point)

        #close on esc press
        k = cv2.waitKey(1)
        if k%256 == 27:
            #Esc pressed
            print("escape hit, closing...")
            break


main()

cam.release()
cv2.destroyAllWindows()

