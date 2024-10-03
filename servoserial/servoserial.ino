/*#include <Servo.h>

Servo servo1;
Servo servo2;

void setup() {
  Serial.begin(9600);
  servo1.attach(9); // Servo 1, 9 numaralı pine bağlı
  servo2.attach(10); // Servo 2, 10 numaralı pine bağlı
}

void loop() {
  if (Serial.available() > 0) {
    int val = Serial.parseInt(); // Seri bağlantıdan gelen değeri oku
    val = constrain(val, 0, 180); // Değer aralığını 0-180 arasında tut
    servo1.write(val); // Servo 1'in pozisyonunu ayarla
    servo2.write(val); // Servo 2'nin pozisyonunu ayarla
  }
}





#include <Servo.h>

Servo servo1;  // Servo motor nesnesi
Servo servo2;  // İkinci servo motor nesnesi

int servo1Pin = 9;  // Servo motor 1 bağlantı pini
int servo2Pin = 10; // Servo motor 2 bağlantı pini

void setup() {
  servo1.attach(servo1Pin);  // Servo motor 1'i ayarla
  servo2.attach(servo2Pin);  // Servo motor 2'yi ayarla
  Serial.begin(9600);        // Seri bağlantıyı başlat
}

void loop() {
  if (Serial.available() > 0) {
    int servo1Value = Serial.parseInt();  // İlk servo motorun değerini oku
    int servo2Value = Serial.parseInt();  // İkinci servo motorun değerini oku
    
    // Servo motorların değerlerini ayarla
    servo1.write(servo1Value);
    servo2.write(servo2Value);
  }
}
*/



#include <Servo.h>

// Servo nesnelerini oluştur
Servo servo1;
Servo servo2;

void setup() {
  // Servo nesnelerine bağlantı pimlerini atayın
  servo1.attach(9);
  servo2.attach(10);

  // Seri haberleşme hızını ayarla
  Serial.begin(9600);
}

void loop() {
  // Seri haberleşme yoluyla servo pozisyonlarını okuyun
  if (Serial.available() > 0) {
    // İlk veriyi servo 1 pozisyonuna ata
    int servo1Pos = Serial.parseInt();
    servo1.write(servo1Pos);

    // İkinci veriyi servo 2 pozisyonuna ata
    int servo2Pos = Serial.parseInt();
    servo2.write(servo2Pos);

    // 15ms gecikme ekleyin
    delay(15);
  }
}
