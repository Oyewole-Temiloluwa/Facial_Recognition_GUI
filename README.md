# Face Recognition Project

## Overview
The Face Recognition Project uses advanced computer vision techniques to recognize and identify faces in images and video streams. This project can be applied in various fields such as security systems, user authentication, and human-computer interaction.

## Features
- Real-time face recognition
- Modular design for easy integration
- Visual feedback through a webcam feed

## Requirements
- Python 3.x
- OpenCV
- dlib
- face_recognition

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/Oyewole-Temiloluwa/Face_Recognition_GUI.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Face_Recognition_GUI
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Files

### main2.py
This is the main script that runs the face recognition application. It captures video from the webcam, processes the frames to detect and recognize faces, and displays the results in real-time.

### util.py
This module contains utility functions used in the project, such as loading face encodings, comparing faces, and other helper functions.

### face_recognition.exe
This executable file is used for running the face recognition application on Windows systems without requiring a Python environment.

## Usage
1. Ensure you have a webcam connected to your computer.
2. Run the main script:
    ```bash
    python main2.py
    ```
3. A window will open showing the webcam feed with face recognition functionalities.

## How It Works
1. The `util.py` module contains functions to load face encodings and compare faces.
2. The `main2.py` script captures video frames from the webcam, processes these frames to detect and recognize faces using the functions in `util.py`, and displays the recognized faces in real-time.

## Contributing
Feel free to fork this repository, make your changes, and submit a pull request. Contributions are welcome!

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- The OpenCV library for providing the computer vision functionalities.
- The dlib and face_recognition libraries for enabling face detection and recognition.
