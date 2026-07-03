import cv2
import numpy as np
import os

dataset_path = r"D:\BTLNhung\Anhnhandien"
recognizer = cv2.face.LBPHFaceRecognizer_create()  

faces = []
labels = []
image_size = (100, 100)

for file in os.listdir(dataset_path):
    if file.endswith(".jpg"):
        path = os.path.join(dataset_path, file)
        face = cv2.imread(path, cv2.IMREAD_GRAYSCALE)  

        if face is None:
            continue 

        face = cv2.resize(face, image_size) 
        faces.append(face)
        labels.append(int(file.split("_")[1]))  

faces = np.array(faces, dtype='uint8')
labels = np.array(labels, dtype='int')

recognizer.train(faces, labels)
recognizer.save("face_model.xml") 

print("Huấn luyện hoàn tất! Mô hình đã được lưu.")
