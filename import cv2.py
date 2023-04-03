import cv2
import face_recognition

# Load the image of the person to be recognized
known_image = face_recognition.load_image_file("MyImage.jpg")

# Get the face encoding of the known person
known_encoding = face_recognition.face_encodings(known_image)[0]

# Initialize the video capture device
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the video stream
    ret, frame = cap.read()

    # Convert the frame to RGB color format for face_recognition
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces in the frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face in the frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Compare the face encoding to the known encoding
        matches = face_recognition.compare_faces([known_encoding], face_encoding)

        # If there is a match, draw a green box around the face
        if matches[0]:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Exit the program if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture device and close the window
cap.release()
cv2.destroyAllWindows()