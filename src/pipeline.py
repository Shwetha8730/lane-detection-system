import cv2
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from lane_detector import detect_lanes

def process_video(input_path, output_path):
    cap    = cv2.VideoCapture(input_path)
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps    = int(cap.get(cv2.CAP_PROP_FPS))

    crop_height = int(height * 0.95)

    out = cv2.VideoWriter(output_path,
                          cv2.VideoWriter_fourcc(*'mp4v'),
                          fps, (width, crop_height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = frame[:crop_height, :]
        result = detect_lanes(frame)
        out.write(result)

    cap.release()
    out.release()
    print(f"Done! Output saved to {output_path}")

if __name__ == "__main__":
    process_video(
    "../assets/test_video.mp4",
    "../outputs/demo_output.mp4"
)