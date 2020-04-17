import face_recognition, argparse, pickle, cv2, glob, os
from pytube import YouTube

def recognizeImage(args):
    image = cv2.imread(args.image_path)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    boxes = face_recognition.face_locations(rgb, model='cnn')
    encodingsTest = face_recognition.face_encodings(rgb, boxes)

    encodingsTrain = {}
    totalPeople = 0
    for file in glob.glob("*.encodings"):
        encodingsTrain[totalPeople] = pickle.loads(open(file, "rb").read())
        totalPeople += 1

    names = []
    name = "Unknown"

    for encodingTest in encodingsTest:
        for peopleId in range(0, totalPeople):
            matches = face_recognition.compare_faces(encodingsTrain[peopleId]['encodings'], encodingTest)

            if True in matches:
                matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                counts = {}

                for i in matchedIdxs:
                    name = encodingsTrain[peopleId]["names"][i]
                    counts[name] = counts.get(name, 0) + 1

                name = max(counts, key=counts.get)
        names.append(name)
    #print(names)
    for ((top, right, bottom, left), name) in zip(boxes, names):
        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
        y = top - 15 if top - 15 > 15 else top + 15
        cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0, 255, 0), 2)

    cv2.imwrite(args.output_file, image)

def recognizeVideo(args):
    yt = YouTube(args.youtube_url)
    video_filename = yt.streams.filter(file_extension='mp4').get_highest_resolution().download()

    if(os.path.exists("data.mp4")):
        os.remove("data.mp4")
    os.rename(video_filename, "data.mp4")
    videoCaptureInput = cv2.VideoCapture('data.mp4')
    fps = videoCaptureInput.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
    videoCaptureOutput = cv2.VideoWriter(args.output_file, fourcc, fps, (640, 480))
    counterImg = 0

    while(True):
        ret, frame = videoCaptureInput.read()
        if frame is None or counterImg > 200:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        boxes = face_recognition.face_locations(rgb, model='cnn')
        encodingsTest = face_recognition.face_encodings(rgb, boxes)

        encodingsTrain = {}
        totalPeople = 0
        for file in glob.glob("*.encodings"):
            encodingsTrain[totalPeople] = pickle.loads(open(file, "rb").read())
            totalPeople += 1

        names = []
        name = "Unknown"

        for encodingTest in encodingsTest:
            for peopleId in range(0, totalPeople):
                matches = face_recognition.compare_faces(encodingsTrain[peopleId]['encodings'], encodingTest)

                if True in matches:
                    matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                    counts = {}

                    for i in matchedIdxs:
                        name = encodingsTrain[peopleId]["names"][i]
                        counts[name] = counts.get(name, 0) + 1

                    name = max(counts, key=counts.get)
            names.append(name)

        for ((top, right, bottom, left), name) in zip(boxes, names):
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            y = top - 15 if top - 15 > 15 else top + 15
            cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0, 255, 0), 2)

        frame = cv2.resize(frame, (640, 480))
        videoCaptureOutput.write(frame)

        counterImg += 1
    videoCaptureInput.release()
    videoCaptureOutput.release()

parser = argparse.ArgumentParser(description='Recognize a face in youtube video.')
parser.add_argument('-y', dest = 'youtube_url', action='store', help='youtube url')
parser.add_argument("-i", dest = 'image_path', action='store', help="image path")
parser.add_argument("-o", dest = 'output_file', action='store', help="output file")
args = parser.parse_args()

if(args.image_path is not None):
    recognizeImage(args)
elif(args.youtube_url is not None):
    recognizeVideo(args)
