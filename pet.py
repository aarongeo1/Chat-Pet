import tkinter
import pyautogui
import random

win = tkinter.Tk()

idle = [tkinter.PhotoImage(file = r"C:\Users\Aaron Geo Binoy\Virtual-Pet\src\assets\Pochita_Idle_Animated_1.gif",format = 'gif -index %i' %(i)) for i in range(31)]


x = 1400
cycle = 0
check = 1

win.config(highlightbackground='white')
label = tkinter.Label(win,bd=0,bg='white')
win.overrideredirect(True)
win.wm_attributes('-transparentcolor','white')
label.pack()

frame = idle[cycle]
win.title('Hello Python')
win.geometry('100x100+'+"1400"+'+925')
label.configure(image=frame)

win.mainloop()

