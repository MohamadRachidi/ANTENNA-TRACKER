import serial
import time
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Servo Kontrol')
        self.geometry('300x150')

        # Seri port bağlantısı
        self.serialPort = serial.Serial('COM11', 9600)

        # Arka plan rengini gri yap
        self.config(bg='grey')

        # İki adet kaydırma çubuğu oluştur
        self.servo1 = tk.Scale(self, from_=0, to=180, orient=tk.HORIZONTAL, tickinterval=10, length=200, label='Servo 1', command=self.sliderValueChanged)
        self.servo1.config(troughcolor='white', sliderrelief='flat', sliderlength=20, showvalue=False)

        self.servo2 = tk.Scale(self, from_=0, to=180, orient=tk.HORIZONTAL, tickinterval=10, length=200, label='Servo 2', command=self.sliderValueChanged)
        self.servo2.config(troughcolor='white', sliderrelief='flat', sliderlength=20, showvalue=False)

        # İki adet trim ayarı kaydırma çubuğu oluştur
        self.servo1Trim = tk.Scale(self, from_=-10, to=10, orient=tk.HORIZONTAL, tickinterval=2, length=200, label='Servo 1 Trim', command=self.sliderValueChanged)
        self.servo1Trim.config(troughcolor='white', sliderrelief='flat', sliderlength=20, showvalue=False)

        self.servo2Trim = tk.Scale(self, from_=-10, to=10, orient=tk.HORIZONTAL, tickinterval=2, length=200, label='Servo 2 Trim', command=self.sliderValueChanged)
        self.servo2Trim.config(troughcolor='white', sliderrelief='flat', sliderlength=20, showvalue=False)

        # Pack kaydırma çubuklarını ekleyin
        self.servo1.pack()
        self.servo2.pack()
        self.servo1Trim.pack()
        self.servo2Trim.pack()

    def sliderValueChanged(self, value):
        # Kaydırma çubuğundan değerleri oku ve seri bağlantı üzerinden gönder
        servo1Value = self.servo1.get() + self.servo1Trim.get()
        servo1Value = max(min(servo1Value, 180), 0)  # Servo 1 için açı sınırlandırması
        self.serialPort.write(str(servo1Value).encode())
        time.sleep(0.01)  # Servo hareketlerinde gecikme oluşmaması için 10ms bekleyin

        servo2Value = self.servo2.get() + self.servo2Trim.get()
        servo2Value = max(min(servo2Value, 180), 0)  # Servo 2 için açı sınırlandırması
        self.serialPort.write(str(servo2Value).encode())
        time.sleep(0.01)  # Servo hareketlerinde gecikme oluşmaması için 10ms bekleyin

if __name__ == '__main__':
    app = App()
    app.mainloop
