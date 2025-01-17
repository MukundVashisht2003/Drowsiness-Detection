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

# Initialize video capture source
cap = cv2.VideoCapture(0)  # Use 0 for the default camera or provide a video file path

# Initialize counters and variables
sleep = 0
drowsy = 0
active = 0
status = ""
color = (0, 0, 0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame. Exiting...")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        x1, y1, x2, y2 = face.left(), face.top(), face.right(), face.bottom()

        # Draw rectangle around the face
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Detect facial landmarks
        landmarks = predictor(gray, face)
        landmarks = face_utils.shape_to_np(landmarks)

        # Check for blinking
        left_blink = blinked(
            landmarks[36], landmarks[37], landmarks[38], 
            landmarks[41], landmarks[40], landmarks[39]
        )
        right_blink = blinked(
            landmarks[42], landmarks[43], landmarks[44], 
            landmarks[47], landmarks[46], landmarks[45]
        )

        # Update status based on blink detection
        if left_blink == 0 or right_blink == 0:
            sleep += 1
            drowsy = 0
            active = 0
            if sleep > 6:
                status = "SLEEPING !!!"
                color = (255, 0, 0)
        elif left_blink == 1 or right_blink == 1:
            sleep = 0
            active = 0
            drowsy += 1
            if drowsy > 6:
                status = "Drowsy !"
                color = (0, 0, 255)
        else:
            drowsy = 0
            sleep = 0
            active += 1
            if active > 6:
                status = "Active :)"
                color = (0, 255, 0)

        # Display status
        cv2.putText(frame, status, (90, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)

        # Draw landmarks on the face
        for n in range(0, 68):
            (x, y) = landmarks[n]
            cv2.circle(frame, (x, y), 1, (255, 255, 255), -1)

    # Display the frames
    cv2.imshow("Frame", frame)

    # Break the loop on pressing 'ESC'
    key = cv2.waitKey(1)
    if key == 27:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
