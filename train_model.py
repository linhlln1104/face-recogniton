import os
import preprocessing
import path
import joblib
import cv2 as cv
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.decomposition import PCA
from sklearn.metrics import classification_report
from sklearn.calibration import CalibratedClassifierCV

def training():
    pca = PCA()
    X_train, y_train, X_test, y_test = preprocessing.creat_data_table(path.path_train, path.path_test)
    clf = LinearSVC(max_iter=100000)
    clf = CalibratedClassifierCV(clf)
    X_train = pca.fit_transform(X_train)
    clf.fit(X_train, y_train)
    y_predict = clf.predict(pca.transform(X_test))
    print("Performance Of The Model")
    print(classification_report(y_test, y_predict))
    joblib.dump(clf, "file_and_data/file/model.npy")

def run():
    label = creat_label()
    face_detection = cv.CascadeClassifier(path.path_haar)
    capture = cv.VideoCapture(0)
    model = joblib.load(path.path_model)
     
    print(label)
    while True:

        pca = PCA()
        isTrue, frame = capture.read()
        model = joblib.load(path.path_model)
        faces = face_detection.detectMultiScale(frame)
        X_train, y_train, X_test, y_test = preprocessing.creat_data_table(path.path_train, path.path_test)

        x = pca.fit_transform(X_train)

        for (x, y, w, h) in faces:
            face = frame[y: h+y, x: w+x]
            face = cv.resize(face, (64, 64))
            face = cv.cvtColor(face, cv.COLOR_BGR2GRAY)
            face = preprocessing.image_preprocessing(face)
            face = [face]
            face = pca.transform(face)
            y_predict = model.predict_proba(face)
            index = list(y_predict[0]).index(max(y_predict[0]))
            if max(y_predict[0]) >= 0.6:
                name = label[index]
                cv.putText(frame, name, (x, y), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv.LINE_AA)
                cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            else:
                name = "Unknown"
                cv.putText(frame, name, (x, y), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
                cv.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

        cv.imshow("Webcam", frame)
        if cv.waitKey(1) & 0xFF == ord('d'):
            break
    capture.release()
    cv.destroyAllWindows()


def creat_label():
    res = {}
    final = {}

    file = open(path.path_students_in_class, "r")
    data = file.read()
    data = data.split("\n")
    data = data[:-1]

    count = 0
    for i in data:
        i = i.split("/")
        res[i[0]] = i[1]
        count += 1

    lst_id = []
    for i in os.listdir(path.path_train):
        lst_id.append(i)

    for i in range(len(lst_id)):
        final[i] = res[lst_id[i]]

    return final


#run()
# training()
