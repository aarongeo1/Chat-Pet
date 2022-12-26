import tkinter
import pyautogui
import random

win = tkinter.Tk()

idle = [tkinter.PhotoImage(file = r"C:\Users\Aaron Geo Binoy\Virtual-Pet\src\assets\Pochita_Idle_Animated_1.gif",format = 'gif -index %i' %(i)) for i in range(31)]


win.config(highlightbackground='white')
win.overrideredirect(True)
win.wm_attributes('-transparentcolor','white')

label = tkinter.Label(win,bd=0,bg='white')
label.pack()

win.after(1,update,cycle,check,event_number,x)
win.mainloop()
