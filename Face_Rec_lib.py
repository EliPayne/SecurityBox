import cv2
from imutils import paths
import face_recognition
import pickle
import os
import imutils
from imutils.video import VideoStream
from imutils.video import FPS
import time

#cam = cv2.VideoCapture(0)
#cv2.namedWindow('cam',cv2.WINDOW_NORMAL)
#cv2.setWindowProperty('web cam', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


def Pics():
    name = 'Elijah' #replace with your name

    cam = cv2.VideoCapture(0)
    
    cv2.namedWindow("press space to take a photo", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("press space to take a photo", 500, 300)
    cv2.setWindowProperty("press space to take a photo", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("press space to take a photo", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "dataset/"+ name +"/image_{}.jpg".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

    cam.release()

    cv2.destroyAllWindows()
    
    
    
    
def Model():
    # our images are located in the dataset folder
    print("[INFO] start processing faces...")
    imagePaths = list(paths.list_images("dataset"))

    # initialize the list of known encodings and known names
    knownEncodings = []
    knownNames = []

    # loop over the image paths
    for (i, imagePath) in enumerate(imagePaths):
	    # extract the person name from the image path
	    print("[INFO] processing image {}/{}".format(i + 1,
		    len(imagePaths)))
	    name = imagePath.split(os.path.sep)[-2]

	    # load the input image and convert it from RGB (OpenCV ordering)
	    # to dlib ordering (RGB)
	    image = cv2.imread(imagePath)
	    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	    # detect the (x, y)-coordinates of the bounding boxes
	    # corresponding to each face in the input image
	    boxes = face_recognition.face_locations(rgb,
		    model="hog")

	    # compute the facial embedding for the face
	    encodings = face_recognition.face_encodings(rgb, boxes)

	    # loop over the encodings
	    for encoding in encodings:
		    # add each encoding + name to our set of known names and
		    # encodings
		    knownEncodings.append(encoding)
		    knownNames.append(name)

    # dump the facial encodings + names to disk
    print("[INFO] serializing encodings...")
    data = {"encodings": knownEncodings, "names": knownNames}
    f = open("encodings.pickle", "wb")
    f.write(pickle.dumps(data))
    f.close()
    
    
    
def Rec(bool):
    #Initialize 'currentname' to trigger only when a new person is identified.
    currentname = "unknown"
    #Determine faces from encodings.pickle file model created from train_model.py
    encodingsP = "encodings.pickle"

    # load the known faces and embeddings along with OpenCV's Haar
    # cascade for face detection
    print("[INFO] loading encodings + face detector...")
    data = pickle.loads(open(encodingsP, "rb").read())

    vs = VideoStream(src=0,framerate=10).start()
    cv2.namedWindow("vs", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("vs", 500, 300)
    cv2.setWindowProperty("vs", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    
    time.sleep(2.0)

    # start the FPS counter
    fps = FPS().start()

    # loop over frames from the video file stream
    while True:
	    # grab the frame from the threaded video stream and resize it
	    # to 500px (to speedup processing)
	    frame = vs.read()
	    #imutils.resize(vs, width=500)
	    # Detect the fce boxes
	    boxes = face_recognition.face_locations(frame)
	    # compute the facial embeddings for each face bounding box
	    encodings = face_recognition.face_encodings(frame, boxes)
	    names = []

	    # loop over the facial embeddings
	    for encoding in encodings:
		    # attempt to match each face in the input image to our known
		    # encodings
		    matches = face_recognition.compare_faces(data["encodings"],
			    encoding)
		    name = "Unknown" #if face is not recognized, then print Unknown

		    # check to see if we have found a match
		    if True in matches:
			    # find the indexes of all matched faces then initialize a
			    # dictionary to count the total number of times each face
			    # was matched
			    matchedIdxs = [i for (i, b) in enumerate(matches) if b]
			    counts = {}

			    # loop over the matched indexes and maintain a count for
			    # each recognized face face
			    for i in matchedIdxs:
				    name = data["names"][i]
				    counts[name] = counts.get(name, 0) + 1

			    # determine the recognized face with the largest number
			    # of votes (note: in the event of an unlikely tie Python
			    # will select first entry in the dictionary)
			    name = max(counts, key=counts.get)

			    #If someone in your dataset is identified, print their name on the screen
			    if currentname != name:
				    currentname = name
				    print(currentname)
					#return True

		    # update the list of names
		    names.append(name)

	    # loop over the recognized faces
	    for ((top, right, bottom, left), name) in zip(boxes, names):
		    # draw the predicted face name on the image - color is in BGR
		    cv2.rectangle(frame, (left, top), (right, bottom),
			    (0, 255, 225), 2)
		    y = top - 15 if top - 15 > 15 else top + 15
		    cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
			    .8, (0, 255, 255), 2)

	    # display the image to our screen
	    #cv2.imshow("Facial Recognition is Running", frame)
	    key = cv2.waitKey(1) & 0xFF

	    # quit when 'q' key is pressed
	    if key == ord("q"):
		    break

	    # update the FPS counter
	    fps.update()

    # stop the timer and display FPS information
    fps.stop()
    print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    # do a bit of cleanup
    cv2.destroyAllWindows()
    vs.stop()