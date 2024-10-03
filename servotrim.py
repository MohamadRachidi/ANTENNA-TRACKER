import serial
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Servo Kontrol')
        self.geometry('400x150')

        # Seri port bağlantısı
        self.serialPort = serial.Serial('COM11', 9600)

        # Arka plan rengini gri yap
        self.config(bg='grey')

        # İki adet kaydırma çubuğu oluştur
        self.servo1 = tk.Scale(self, from_=0, to=180, orient=tk.HORIZONTAL, tickinterval=10, length=200, label='Servo 1', command=self.sliderValueChanged)
        self.servo1.config(troughcolor='white', sliderrelief='flat', sliderlength=20, showvalue=False)
        self.servo1.pack()

        self.servo1plusButton = tk.Button(self, text='+', command=lambda:self.adjustTrim(1, 1))
        self.servo1minusButton = tk.Button(self, text='-', command=lambda:self.adjustTrim(1, -1))
        self.servo1plusButton.pack(side=tk.LEFT, padx=(20,0), pady=10)
        self.servo1minusButton.pack(side=tk.LEFT, pady=10)

        self.servo2 = tk.Scale(self, from_=0, to=180, orient=tk.HORIZONTAL, tickinterval=10, length=200, label='Servo 2', command=self.sliderValueChanged)
        self.servo2.config(troughcolor='white', sliderrelief='flat', sliderlength=20, showvalue=False)
        self.servo2.pack()

        self.servo2plusButton = tk.Button(self, text='+', command=lambda:self.adjustTrim(2, 1))
        self.servo2minusButton = tk.Button(self, text='-', command=lambda:self.adjustTrim(2, -1))
        self.servo2plusButton.pack(side=tk.LEFT, padx=(20,0), pady=10)
        self.servo2minusButton.pack(side=tk.LEFT, pady=10)

    def sliderValueChanged(self, value):
        # Kaydırma çubuğundan değer oku ve seri bağlantı üzerinden gönder
        servo1Value = self.servo1.get()
        self.serialPort.write(str(servo1Value).encode())

        servo2Value = self.servo2.get()
        self.serialPort.write(str(servo2Value).encode())

    def adjustTrim(self, servoNumber, direction):
        # İlgili düğmeye basıldığında, ilgili servo trim ayarını değiştirir ve güncel değeri seri port üzerinden gönderir
        if servoNumber == 1:
            servo = self.servo1
        else:
            servo = self.servo2

        currentValue = servo.get()
        newValue = currentValue + direction
        if newValue < 0:
            newValue = 0
        elif newValue > 180:
            newValue = 180

        servo.set(newValue)
        self.serialPort.write(str(servo.get()).encode())

if __name__ == '__main__':
    app = App()
    app.mainloop()
