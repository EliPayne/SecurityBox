import cv2
import tkinter
from imutils import paths
import face_recognition
import pickle
import os
import imutils
#from Hall import HL
#from Lock import Open, Close
from imutils.video import VideoStream
from imutils.video import FPS
#from add_remove import Add, Remove
import time

#cam = cv2.VideoCapture(0)
#cv2.namedWindow('cam',cv2.WINDOW_NORMAL)
#cv2.setWindowProperty('web cam', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


def Pics(id):
    root = 'dataset'
    list = id.split(",")
    for i in list:
        path = os.path.join(root, i)
        os.mkdir(path)
    
    cam = cv2.VideoCapture(0)
    
    cv2.namedWindow("press space to take a photo", cv2.WINDOW_NORMAL)
    #cv2.resizeWindow("press space to take a photo", 500, 300)
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
            img_name = "dataset/"+ id +"/image_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
            #Add(id,img_name,db)

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
        #Open()
        #time.sleep(30)
        #if(HL == True):
            #Close()
            #break
        
        frame = vs.read()
        boxes = face_recognition.face_locations(frame)
        encodings = face_recognition.face_encodings(frame, boxes)
        names = []
        
        for encoding in encodings:
            matches = face_recognition.compare_faces(data["encodings"],
			    encoding)
            name = "Unknown" #if face is not recognized, then print Unknow
            if True in matches:
                matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                counts = {}
                for i in matchedIdxs:
                    name = data["names"][i]
                    counts[name] = counts.get(name, 0) + 1
                    name = max(counts, key=counts.get)
                    
                if currentname != name:
                    currentname = name
                    print(currentname)
                
                names.append(name)
        
        for ((top, right, bottom, left), name) in zip(boxes, names):
            cv2.rectangle(frame, (left, top), (right, bottom),
			    (0, 255, 225), 2)
            y = top - 15 if top - 15 > 15 else top + 15
            cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
			    .8, (0, 255, 255), 2)
            
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord("q"):
            break
        fps.update()

    # stop the timer and display FPS information
    fps.stop()
    print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    # do a bit of cleanup
    cv2.destroyAllWindows()
    vs.stop()