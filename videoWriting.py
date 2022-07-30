import cv2

def recording():
    # WRITING video to our Storage Device
    cap = cv2.VideoCapture(0)

    # This codec allows us to encode video in digital file
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    # Writing Video in a file
    # Syntax : (<filename>, codec, frames_per_sec, resolution)
    out = cv2.VideoWriter("TextVideo.mp4", fourcc, 20.0, (640, 480))

    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame,1)
        if ret == True:
            out.write(frame)
            cv2.imshow('output', frame)
            if cv2.waitKey(1) == ord('q'):
                break
        else:
            break
    cap.release()