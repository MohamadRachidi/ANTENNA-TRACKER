import serial
import tkinter as tk

# Arduino'nun seri port ayarları
ser = serial.Serial('COM11', 9600, timeout=1)

# Pencereyi oluştur
root = tk.Tk()
root.title("Servo Kontrol")

# Kaydırma çubuğunu oluştur
slider = tk.Scale(root, from_=0, to=180, orient=tk.HORIZONTAL)
slider.pack()

# Kaydırma çubuğu hareket ettiğinde çağrılacak işlev
def update_position(event):
    # Kaydırma çubuğunun değerini al ve seri port aracılığıyla gönder
    pos = slider.get()
    ser.write(bytes(str(pos), 'utf-8'))

    # Arduino'dan gelen yanıtı oku ve yazdır
    response = ser.readline().decode('utf-8').rstrip()
    print(response)

# Kaydırma çubuğu hareket ettikçe "update_position" işlevini çağır
slider.bind("<B1-Motion>", update_position)

# Pencereyi aç
root.mainloop()
