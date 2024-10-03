"""import pyfirmata
import tkinter as tk

 # Arduino ile bağlantı kur
board = pyfirmata.Arduino('COM11')
iter8 = pyfirmata.util.Ierator(board)





import pyfirmata
import time

# Arduino'ya bağlan
board = pyfirmata.Arduino('COM11')

# Servo motor için pin belirle (9 numaralı pin)
servo_pin = board.get_pin('d:9:s')

# Servoyu belirtilen açıya göre hareket ettir
def set_servo_angle(angle):
    servo_pin.write(angle)
    time.sleep(0.05)

# Servoyu 0 dereceye getir
set_servo_angle(0)

# Servoyu 90 dereceye getir
set_servo_angle(90)

# Servoyu 180 dereceye getir
set_servo_angle(180)

# Arduino bağlantısını kapat
board.exit()
"""

import pyfirmata
print(pyfirmata.__version__)
