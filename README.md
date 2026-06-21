# Virtual Mouse Using Hand Gestures

A Computer Vision project that enables users to control the computer mouse using hand gestures captured through a webcam.

## Features

* Real-time hand tracking using MediaPipe
* Cursor movement using index finger tracking
* Mouse click detection using thumb-index pinch gesture
* Smooth cursor movement for better user experience
* Touch-free human-computer interaction

## Technologies Used

* Python
* OpenCV
* MediaPipe
* PyAutoGUI
* NumPy

## How It Works

1. Webcam captures live video feed.
2. MediaPipe detects hand landmarks.
3. Index finger tip controls cursor movement.
4. Thumb and index finger pinch gesture performs mouse click.
5. Cursor movement is smoothed to reduce jitter.

## Installation

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
python virtual_mouse.py
```

## Future Enhancements

* Right-click gesture support
* Drag and drop functionality
* Scroll gesture support
* Multi-hand tracking
* Custom gesture recognition

## Author

Sujal Rajput

B.Tech Robotics & Automation
Symbiosis Institute of Technology, Pune
