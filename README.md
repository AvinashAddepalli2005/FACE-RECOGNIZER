# Real-Time Face Detection using OpenCV

This project demonstrates real-time face detection using a webcam feed with OpenCV's Haar Cascade classifier.

## Requirements

- Python 3.x
- OpenCV library (cv2)
- Haar Cascade XML file for face detection (provided by OpenCV)

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/).
2. Install OpenCV using pip:
   ```bash
   pip install opencv-python
   pip install opencv-python-headless
   ```
3. Ensure the Haar Cascade XML file is present in your OpenCV data directory. The file path typically looks like:
   ```
   C:/Users/<YourUsername>/AppData/Local/Programs/Python/<PythonVersion>/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml
   ```

## Usage

1. Copy the provided Python script into a `.py` file (e.g., `face_detection.py`).
2. Run the script using:
   ```bash
   python face_detection.py
   ```
3. The program will:
   - Open a live video feed from your webcam.
   - Detect faces in real-time and highlight them with green rectangles.
   - Display the video feed in a window named `video_live`.

4. To exit the program, press the `a` key.

## Code Overview

- **Haar Cascade Classifier**: Pre-trained model for detecting frontal faces.
- **cv2.VideoCapture(0)**: Captures live video from the default webcam.
- **cv2.cvtColor**: Converts frames to grayscale for efficient face detection.
- **cv2.rectangle**: Draws rectangles around detected faces.
- **Exit Mechanism**: Program exits when the `a` key is pressed.

## Example Output

- Detected faces are highlighted with green rectangles in the live webcam feed.

## Applications

- Security systems
- Interactive applications
- Face recognition pre-processing

## Troubleshooting

- **No video feed**: Ensure your webcam is connected and accessible.
- **No faces detected**: Adjust detection parameters (`scaleFactor`, `minNeighbors`, `minSize`) in the code.
- **Haar Cascade XML not found**: Verify the file path in the script.

## License

This project uses OpenCV, an open-source library, under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
