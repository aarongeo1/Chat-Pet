import tkinter
import pyautogui
import random
import sys
from ctypes import windll, wintypes, byref

SPI_GETWORKAREA = 0x0030
    
# This var will receive the result to SystemParametersInfoW  
desktopWorkingArea = wintypes.RECT()

_ = windll.user32.SystemParametersInfoW(SPI_GETWORKAREA,0,byref(desktopWorkingArea),0)

left = desktopWorkingArea.left
top = desktopWorkingArea.top
right = desktopWorkingArea.right
bottom = desktopWorkingArea.bottom

x,y = windll.user32.GetSystemMetrics(0), windll.user32.GetSystemMetrics(1)

win = tkinter.Tk()

idle = [tkinter.PhotoImage(file = r"C:\Users\Aaron Geo Binoy\Virtual-Pet\src\assets\Pochita_Idle_Animated_1.gif",format = 'gif -index %i' %(i)) for i in range(31)]


cycle = 0
check = 1 # 1 == idle


win.config(highlightbackground='white')
label = tkinter.Label(win,bd=0,bg='white')
win.overrideredirect(True)
win.wm_attributes('-transparentcolor','white')
label.pack()


def run(cycle,array):
    if cycle < len(array)-1:
        cycle += 1
    else:
        cycle = 0
    return cycle

def change(cycle,check):
    if check == 1:
        frame = idle[cycle]
        cycle = run(cycle,idle)
    win.geometry('100x100+'+"1000"+'+{}'.format(bottom - (y-bottom) - 50))
    label.configure(image=frame)
    win.after(75,change,cycle,check)




win.after(1,change,cycle,check)
win.lift()
win.attributes('-topmost',True)
win.after_idle(win.attributes,'-topmost',True)
win.mainloop()

