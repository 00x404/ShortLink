from tkinter import *
from tkinter import messagebox
import pyperclip
import pyshorteners
import clipboard
import webbrowser

root = Tk()
root.title("ShortLink")
root.geometry("400x320")
root["bg"] = "black"


Label(root, text="ShortLink", font = "Calibri 15 bold", bg = "black", fg = "white").pack()
Label(root, text="Делайте ссылки короче!", font = "Calibri 8 bold", bg = "black", fg = "white").pack(pady=3)
Label(root, text="Введите ссылку:", font = "Calibri 11 bold", bg = "black", fg = "white").pack(pady=5)
# Label(root, text="Введите ссылку:", font = "Calibri 11 bold", bg = "black", fg = "white").pack(pady=5)

link = Entry(root, width=30)
link.pack()

Label(root, text="Готовая ссылка:", font = "Calibri 11 bold", bg="black", fg = "white").pack(pady=5)

res = Entry(root, width=30)
res.pack()

def short():
	try:
		a = link.get()
		s = pyshorteners.Shortener().tinyurl.short(a)
		res.insert(0, s)
		webbrowser.open(s)
	except:
		messagebox.showerror("Error 0x1", "Неверная ссылка!\nUPD:Такая шибка также случается при отсутствии или низкой скорости интернета")

def shorto():
	try:
		a = link.get()
		s = pyshorteners.Shortener().tinyurl.short(a)
		res.insert(0, s)
		webbrowser.open(s)
	except:
		messagebox.showerror("Error 0x1", "Неверная ссылка!\nUPD:Такая шибка также случается при отсутствии или низкой скорости интернета")
def openb():
	webbrowser.open(s)

def q():
	quit()



#
# def wbop():
# 	webbrowser.open('a.html', new=2)

Button(root, text="Сократить ссылку", command=short, fg='white', bg='black').pack(pady=2)
Button(root, text="Выйти", command=q, fg='white', bg='black').pack(pady=2)
# Button(root, text="Подробнее", command=a, fg='white', bg='black').pack(pady=2)
Button(root, text="Сократить и открыть готовую ссылку", command=shorto, fg='white', bg='black').pack(pady=2)
root.mainloop()
