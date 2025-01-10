# Drowsiness Detection

This project aims to detect drowsiness in individuals using computer vision techniques. It uses OpenCV, Dlib, and other libraries to capture video frames, detect facial landmarks, and compute the Eye Aspect Ratio (EAR) to determine the state of the eyes (active, drowsy, or sleeping).

## Features

- Real-time video capture and processing
- Face detection using Dlib's pre-trained model
- Eye aspect ratio calculation to determine drowsiness
- Visual feedback with rectangles around detected faces

## Requirements

- Python 3.x
- OpenCV
- Dlib
- imutils
- numpy

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/Drowsiness-Detection.git
    cd Drowsiness-Detection
    ```

2. Create and activate a virtual environment:
    - On Windows:
        ```sh
        python -m venv venv
        .\venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```

3. Install the required packages:
    ```sh
    pip install opencv-python dlib imutils numpy
    ```

4. Download the pre-trained shape predictor model:
    - [shape_predictor_68_face_landmarks.dat](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)
    - Extract the file and place it in the project directory.

## Usage

1. Ensure your virtual environment is activated.
2. Run the main script:
    ```sh
    python main.py
    ```

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Dlib
OpenCV
imutils
