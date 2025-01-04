import cv2

# Load the Haar Cascade XML file for frontal face detection
# This file contains pre-trained data for identifying faces
face_cap = cv2.CascadeClassifier(
    "C:/Users/aavi9/AppData/Local/Programs/Python/Python313/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml"
)

# Initialize video capture from the webcam (device 0)
video_cap = cv2.VideoCapture(0)

# Start an infinite loop for live video processing
while True:
    # Capture a frame from the webcam
    ret, video = video_cap.read()

    # Check if the frame was successfully captured
    if not ret:
        print("Error: Unable to capture video frame.")
        break

    # Convert the captured frame to grayscale for face detection
    # Face detection algorithms work better with grayscale images
    col = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    # - scaleFactor: Specifies how much the image size is reduced at each image scale
    # - minNeighbors: Defines how many neighbors a rectangle should have to retain it
    # - minSize: Minimum possible face size to be considered
    # - flags: Specifies optional flags, such as cv2.CASCADE_SCALE_IMAGE
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Loop through all detected faces and draw rectangles around them
    for (x, y, w, h) in faces:
        # Draw a green rectangle around the detected face
        # - (x, y) is the top-left corner of the rectangle
        # - (x+w, y+h) is the bottom-right corner of the rectangle
        # - (0, 255, 0) specifies the color (green) in BGR format
        # - 2 is the thickness of the rectangle
        cv2.rectangle(video, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the video frame with rectangles around detected faces
    cv2.imshow("video_live", video)

    # Check if the 'a' key is pressed to exit the loop
    if cv2.waitKey(10) == ord("a"):
        break

# Release the webcam and free resources
video_cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
