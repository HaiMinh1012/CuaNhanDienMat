# Hệ thống cửa tự động sử dụng nhận diện khuôn mặt để xác thực người dùng.  

---

## Features

- Chụp ảnh khuôn mặt và xây dựng dataset
- Huấn luyện mô hình nhận diện khuôn mặt
- Nhận diện khuôn mặt realtime bằng webcam
- Giao tiếp Python ↔ Arduino qua Serial
- Tự động điều khiển đóng / mở cửa

---

## Project Structure

```bash
FaceRecognitionDoor/
│
├── chupanh.py        # Chụp ảnh khuôn mặt để tạo dataset
├── train.py          # Huấn luyện model nhận diện
├── nhandienmat.py    # Nhận diện khuôn mặt realtime
├── BTL.ino           # Arduino điều khiển motor/servo cửa
```

---

## Technologies Used

- Python
- OpenCV
- NumPy
- Face Recognition / LBPH
- Arduino
- Serial Communication
- Servo Motor

---

## Workflow

### 1. Thu thập dữ liệu khuôn mặt
Chạy:

```bash
python chupanh.py
```

Chương trình:
- mở webcam
- phát hiện khuôn mặt
- chụp nhiều ảnh khuôn mặt
- lưu vào thư mục 'anhnhandien'

---

### 2. Huấn luyện mô hình
Chạy:

```bash
python train.py
```

Kết quả:
- trích xuất đặc trưng khuôn mặt
- huấn luyện model nhận diện
- lưu model vào thư mục `facemodel.xml`

---

### 3. Nhận diện khuôn mặt và điều khiển cửa
Chạy:

```bash
python nhandienmat.py
```

Hệ thống:
- đọc camera realtime
- phát hiện khuôn mặt
- so sánh với model đã train

Nếu nhận diện thành công:

```text
1
```

Python gửi `1` qua cổng Serial → Arduino mở cửa.

Nếu không hợp lệ:

```text
0
```

Python gửi `0` → Arduino giữ cửa đóng.

---

## Arduino Logic

File:

```bash
BTL.ino
```

Arduino:
- nhận dữ liệu Serial từ Python
- đọc giá trị `0/1`
- điều khiển servo hoặc motor

Pseudo logic:

```cpp
if (signal == 1) {
    openDoor();
} else {
    closeDoor();
}
```

---

## Installation

Cài thư viện Python:

```bash
pip install opencv-python numpy pillow pyserial
```

---

## Future Improvements

- Nâng cấp bằng Deep Learning (FaceNet / ArcFace)
- Tích hợp anti-spoofing chống ảnh giả
- Thêm cơ chế log lịch sử ra vào
- Kết hợp cảnh báo khi phát hiện người lạ

---

## Demo

- Authorized face → Door opens
- Unknown face → Door remains closed

---

## Author

Hai Minh  
GitHub: https://github.com/HaiMinh1012
