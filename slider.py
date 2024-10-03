import tkinter as tk

# Pencereyi oluştur
root = tk.Tk()

# Kaydırma çubuğunu oluştur
slider = tk.Scale(root, from_=0, to=180, orient=tk.HORIZONTAL, length=200)

# Kaydırma çubuğunu ekrana yerleştir
slider.pack()

# Pencereyi göster
root.mainloop()