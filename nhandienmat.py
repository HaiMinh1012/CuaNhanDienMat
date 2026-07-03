import cv2
import serial
import time

arduino = serial.Serial("COM5", 9600)
time.sleep(2)
arduino.reset_input_buffer()  # Đợi Arduino khởi động

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("face_model.xml")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
current_state = None  # Trạng thái gửi gần nhất

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    if len(faces) > 0:
        (x, y, w, h) = faces[0]
        face = gray[y:y+h, x:x+w]
        label, confidence = recognizer.predict(face)

        if confidence < 65:
            text = f"User {label} ({confidence:.2f})"
            if current_state != '1':
                arduino.write(b'1')  # Gửi tín hiệu mở cửa
                current_state = '1'
        else:
            text = "Khong nhan dien duoc"
            if current_state != '0':
                arduino.write(b'0')  # Gửi tín hiệu đóng cửa
                current_state = '0'
        cv2.putText(frame, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    else:
        if current_state != '0':
            arduino.write(b'0')  # Không thấy mặt thì đóng cửa luôn
            current_state = '0'

    cv2.imshow("Nhận diện khuôn mặt", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()
