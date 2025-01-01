import cv2
import numpy as np
from Utils import *
from QuadTree import QuadTree

def frame_to_list(frame):
    frame_2d_list = frame.tolist()

    return [[(pix[0], pix[1], pix[2]) for pix in row] for row in frame_2d_list]

def list_to_frame(rgb_list):
    frame_rgb = np.array(rgb_list, dtype=np.uint8)
    frame_bgr = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)

    return frame_bgr

# Open video file
cap = cv2.VideoCapture('Dataset/sample.mov')  # Replace with your video file

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    image = frame_to_list(frame)
    qt = QuadTree(image)

    compressed = qt.compress(32).image
    cv2.imshow('Compressed', list_to_frame(compressed))

    # Break on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

