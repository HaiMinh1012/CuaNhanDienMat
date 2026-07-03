#include <Servo.h>

Servo myServo;

void setup() {
    myServo.attach(2);
    myServo.write(0);  // Ban đầu servo ở vị trí 0° (cửa đóng)
    Serial.begin(9600);
}

void loop() {
    if (Serial.available() > 0) {
        char cmd = Serial.read();

        if (cmd == '1') {  
            myServo.write(180);
        } 
        //else if (cmd == '0') {  
        //    myServo.write(0);
        //    delay(10000); 
        //}
    }
}