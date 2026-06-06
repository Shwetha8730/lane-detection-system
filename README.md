# Lane Detection System using OpenCV

## Overview

This project implements a lane detection system using Python and OpenCV. The system processes road videos, detects lane boundaries, and highlights the driving lane area to assist in road navigation and autonomous driving applications.

## Features

* Real-time lane detection from video input
* Region of Interest (ROI) based lane extraction
* Canny Edge Detection
* Hough Line Transform
* Lane averaging and smoothing
* Lane area highlighting using polygon filling
* Video processing and output generation

## Project Structure

```text
lane-detection-system/
│
├── assets/
│   └── test_video.mp4
│
├── outputs/
│
├── src/
│   ├── lane_detector.py
│   ├── pipeline.py
│   └── utils.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Technologies Used

* Python
* OpenCV
* NumPy

## Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/lane-detection-system.git
```

2. Navigate to the project folder

```bash
cd lane-detection-system
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

Run the lane detection pipeline:

```bash
python src/pipeline.py
```

The processed video will be saved in the `outputs` folder.

## Methodology

1. Convert video frames to grayscale
2. Apply Gaussian Blur for noise reduction
3. Perform Canny Edge Detection
4. Apply Region of Interest masking
5. Detect lane segments using Hough Transform
6. Average left and right lane lines
7. Highlight the driving lane region
8. Generate processed output video

## Results

The system successfully detects lane boundaries and highlights the driving lane region in road videos.

## Future Enhancements

* FPS Counter
* Lane Departure Warning System
* Curved Lane Detection
* Vehicle Detection using YOLOv8
* Vehicle Counting
* Advanced Driver Assistance System (ADAS) Dashboard

## Author

Shwethashree S

## License

This project is intended for educational and learning purposes.
