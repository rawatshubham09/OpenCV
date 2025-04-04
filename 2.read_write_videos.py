import numpy as np
import cv2 as cv
import os

def videoFromWebcam():
    cap = cv.VideoCapture(0)

    if not cap.isOpened():
        print("Error opening video capture")
        exit()
    
    while True:
        # return value -> T,F and Frame
        ret, frame = cap.read()
        if ret:
            cv.imshow("WebCamp", frame)
        
        if cv.waitKey(1) == ord("q"):
            break

    cap.release()
    cv.destroyAllWindows()

def videoFromFile():
    video_path = "OpenCV\\demoImage\\VID-20250215-WA0002.mp4"
    cap = cv.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        cv.imshow('video', frame)
        delay = int(1000/60)

        if cv.waitKey(delay) & 0xFF == ord('q'):
            break
    

def writeVideoToFile():
    cap = cv.VideoCapture(0)

    fourcc = cv.VideoWriter_fourcc(*"XVID")
    outPath = "OpenCV\\demoImage\\webcam.avi"

    out = cv.VideoWriter(outPath, fourcc, 20.0, (640, 480))
    
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            cv.imshow("WebCam", frame)
        
        if cv.waitKey(1) == ord("q"):
            break
        
    cap.release()
    out.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    #videoFromWebcam()
    #videoFromFile()
    writeVideoToFile()
