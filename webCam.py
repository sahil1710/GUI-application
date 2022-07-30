import cv2

def webCam():
    cap = cv2.VideoCapture(0)

    while True:
        # read() func will capture a single frame and will return 2 values
        # ret : if frame is returned successfully then it hold true else false
        # frame : contains the captured frame
        ret, frame = cap.read()
        frame = cv2.flip(frame,1)

        # We will show that frame on screen using imshow() function
        cv2.imshow('frame', frame)

        # Taking user input to stop the loop
        # cv2.waitKey(1) will wait for user input for 1 millisecond and if any key is pressed then it returns its ASCII value
        # ord('q') : returns the ASCII value of q
        if cv2.waitKey(1) == ord('q'):
            break

    # Releasing The Camera resource
    cap.release()
    cv2.destroyAllWindows()


