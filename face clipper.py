import numpy
import cv2


def allFaces(orig, x, y, w, h,faceNum):
    crop_img = orig[y - int(h * 0.1):y + int(h * 1.1),
                    x - int(0.1 * w):x + int(w * 1.1)]
    cv2.imwrite('face_' + str(faceNum) + '.png', crop_img)


def largestFace(faces,orig,maxy,maxx):
    size = list(range(len(faces)))
    print(faces)
    print(len(size))
    maxSize=0
    maxSizePos=-1
    i = 0
    for (x, y, w, h) in faces:
        size[i] = w * h
        if (size[i] > maxSize):
            maxSize=size[i]
            maxSizePos=i
        i+=1
    (x, y, w, h)=faces[maxSizePos]
    crop_img = orig[max(0,y - int(h * 0.1)):min(y + int(h * 1.1),maxy),
                    max(0,x - int(0.1 * w)):min(x + int(w * 1.1),maxx)]
    cv2.imwrite('LargestImage.png', crop_img)

def run():
    video_capture = cv2.VideoCapture(0)
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    while(True):
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        # ret, orig = video_capture.read()
        # Our operations on the frame come here
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            frame,
            scaleFactor=1.2,
            minNeighbors=10,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        (x2, y2, w2, h2) = (0, 0, 0, 0)
        faceNum = 0
        for (x, y, w, h) in faces:

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            allFaces(frame, x, y, w, h,faceNum)
            faceNum += 1
        # largestFace(faces,frame,video_capture.get(4),video_capture.get(3))
        # Display the resulting frame
        #cv2.imshow("cropped", crop_img)
        cv2.imshow('Webcam', frame)

        # if cv2.waitKey(1) & 0xFF == ord('p'):
        #     clickPhoto = True

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()

run()