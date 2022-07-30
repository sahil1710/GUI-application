from time import sleep
import numpy as np
import cv2
import pyautogui

# pyautogui takes image in Python image Library
# we use numpy to convert RGB image array taken by puautogui into BGR because for image writing we are using cv2
# and when the image file is read with the OpenCV using imread(), the order of colors should be BGR
def screenShot():
    sleep(1)
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    cv2.imwrite("image.png", image)

