import cv2 as cv

# Load the Cascade Classifier
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# Start capturing video from the webcam
cap = cv.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detect faces
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

    # Draw rectangles around the faces
    for (x, y, w, h) in faces_rect:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

    # Display the frame with detected faces
    cv.imshow('Detected Faces', frame)

    # Break the loop when 'q' is pressed
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv.destroyAllWindows()
