import pyfirmata
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Servo Kontrol')
        self.geometry('300x150')

        # Arduino ile bağlantı kur
        self.board = pyfirmata.Arduino('COM11')
        self.servo1_pin = 9
        self.servo2_pin = 10

        # İki adet kaydırma çubuğu oluştur
        self.servo1 = tk.Scale(self, from_=0, to=180, orient=tk.HORIZONTAL, tickinterval=10, length=200, label='Servo 1', command=self.sliderValueChanged)
        self.servo1.config(troughcolor='white', sliderrelief='flat', sliderlength=20, showvalue=False)

        self.servo2 = tk.Scale(self, from_=0, to=180, orient=tk.HORIZONTAL, tickinterval=10, length=200, label='Servo 2', command=self.sliderValueChanged)
        self.servo2.config(troughcolor='white', sliderrelief='flat', sliderlength=20, showvalue=False)

        # Pack kaydırma çubuklarını ekleyin
        self.servo1.pack()
        self.servo2.pack()

    def sliderValueChanged(self, value):
        # Kaydırma çubuğundan değer oku ve servolara gönder
        servo1Value = self.servo1.get()
        self.board.digital[self.servo1_pin].write(servo1Value)

        servo2Value = self.servo2.get()
        self.board.digital[self.servo2_pin].write(servo2Value)

if __name__ == '__main__':
    app = App()
    app.mainloop()
