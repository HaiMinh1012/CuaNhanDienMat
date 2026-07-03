import cv2
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

dataset_path = r"D:\BTLNhung\Anhnhandien"

if not os.path.exists(dataset_path):
    os.makedirs(dataset_path)

cap = cv2.VideoCapture(0)

face_id = input("Nhập ID khuôn mặt của bạn (số nguyên): ")  

existing_files = [f for f in os.listdir(dataset_path) if f.startswith(f"user_{face_id}_")]
existing_numbers = [int(f.split("_")[-1].split(".")[0]) for f in existing_files if f.split("_")[-1].split(".")[0].isdigit()]
start_count = max(existing_numbers, default=0) 

count = start_count 

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        count += 1
        face_img = gray[y:y+h, x:x+w]  
        file_path = f"{dataset_path}/user_{face_id}_{count}.jpg"
        cv2.imwrite(file_path, face_img)  
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("Thu thập dữ liệu khuôn mặt", frame)

    if cv2.waitKey(1) & 0xFF == ord('q') or count >= start_count + 100:  
        break

cap.release()
cv2.destroyAllWindows()
print(f"Đã lưu thêm {count - start_count} ảnh trong thư mục {dataset_path}.")
