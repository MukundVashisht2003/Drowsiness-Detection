import cv2
import numpy as np
import dlib
from imutils import face_utils

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  # Ensure correct path

# Function to compute Euclidean distance
def compute(ptA, ptB):
    return np.linalg.norm(ptA - ptB)

# Function to determine blinking status
def blinked(a, b, c, d, e, f):
    up = compute(b, d) + compute(c, e)
    down = compute(a, f)
    ratio = up / (2.0 * down)  # Eye Aspect Ratio (EAR)

    if ratio > 0.25:
        return 2  # Active
    elif 0.21 < ratio <= 0.25:
        return 1  # Drowsy
    else:
        return 0  # Sleeping

# Initialize counters and variables
sleep = 0
drowsy = 0
active = 0
status = ""
color = (0, 0, 0)

