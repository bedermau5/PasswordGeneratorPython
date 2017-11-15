from tkinter import *
import random
def password(event):
    population="123456789qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlLzZxXcCvVbBnNmM@#$%&"
    res.configure(text = "Your password:" + ''.join(random.sample(population, int(entry.get()))))
w = Tk()
w.title("Генератор паролей")
Label(w, text="Введите длину длину пароля (максимум 66)").pack()
entry = Entry(w)
entry.bind("<Return>", password)
entry.pack()
res = Label(w)
res.pack()
b1 = Button(w, text='Quit', command=w.quit)
b1.pack()
w.mainloop()

