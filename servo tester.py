import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider
from PyQt5.QtCore import Qt
import serial
import time
import math

# Serial port bağlantısı ayarları
ser = serial.Serial('COM11', 9600) # Port ismi ve baudrate ayarları

# Servo motorların açıları
servo1_aci = 0 # İlk servo motorun açısı
servo2_aci = 0 # İkinci servo motorun açısı

# Servo motorların açılarını ayarlamak için yardımcı fonksiyon
def set_servo_angles(servo1_aci, servo2_aci):
    ser.write(str(servo1_aci).encode()) # İlk servo motorun açısını Arduino'ya gönder
    time.sleep(0.05) # Bekleme süresi
    ser.write(str(servo2_aci).encode()) # İkinci servo motorun açısını Arduino'ya gönder
    time.sleep(0.05) # Bekleme süresi 
    

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Pencere boyutu ayarları
        self.width = 500
        self.height = 300
        self.setGeometry(100, 100, self.width, self.height)

        # Kaydırma çubuğu oluşturma
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setFocusPolicy(Qt.NoFocus)
        self.slider.setGeometry(50, 50, 400, 30)
        self.slider.setMinimum(0)
        self.slider.setMaximum(1023)
        self.slider.setSingleStep(1)
        self.slider.valueChanged.connect(self.sliderValueChanged)

        # Başlangıçta kaydırma çubuğu değeri sıfır olsun
        self.slider.setValue(0)

    def sliderValueChanged(self):
        global servo1_aci, servo2_aci

        # Kaydırma çubuğu değerini oku
        slider_value = self.slider.value()

        # İlk servo motoru kontrol et
        servo1_aci = int(slider_value/4) # Kaydırma çubuğunun değerini servonun açısına çevir
        set_servo_angles(servo1_aci, servo2_aci) # Servo motorların açılarını ayarla

        # İkinci servo motoru kontrol et
        servo2_aci = int(math.sin(math.radians(slider_value))*90+90) # Kaydırma çubuğunun değerini servonun açısına çevir
        set_servo_angles(servo1_aci, servo2_aci) # Servo motorların açılarını ayarla

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())




