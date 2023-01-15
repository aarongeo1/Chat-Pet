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

# importing the idle gif
idle = [tkinter.PhotoImage(file = r"C:\Users\Aaron Geo Binoy\Virtual-Pet\src\assets\Pochita_Idle_Animated_1.gif",format = 'gif -index %i' %(i)) for i in range(31)]
walk_left = [tkinter.PhotoImage(file = r"C:\Users\Aaron Geo Binoy\Virtual-Pet\src\assets\Pochita_walking_2.gif",format = 'gif -index %i' %(i)) for i in range(11)]

cycle = 0
check = 0 # 0 == idle
x = 1400
time = 2400
# making the background transparent
win.config(highlightbackground='white')
label = tkinter.Label(win,bd=0,bg='white')
win.overrideredirect(True)
win.wm_attributes('-transparentcolor','white')

label.pack()

# to iterate among the index of the array of frames

def run(cycle,array):
    if cycle < len(array)-1:
        cycle += 1
    else:
        cycle = 0
    return cycle

# function to change frames
def change(cycle,check,time):
    time -= 75
    if time == 0:
        check = random.randint(0,1)
        time = 2400

    if check == 0:
        frame = idle[cycle]
        cycle = run(cycle,idle)
        #check +=1
        win.geometry('100x100+' + "1000" + '+{}'.format(bottom - (y - bottom) - 50))
        label.configure(image=frame)
        win.after(75, change, cycle, check,time)


    elif check == 1:
        global x
        frame = walk_left[cycle]
        cycle = run(cycle,walk_left)
        win.geometry('100x100+' + "1000" + '+{}'.format(bottom - (y - bottom) - 50))
        label.configure(image=frame)
        win.after(75, change, cycle, check,time)
        x-=3

    #win.geometry('100x100+' + "1000" + '+{}'.format(bottom - (y - bottom) - 50))
    # win.geometry('100x100+'+str(x)+'+1050')
    # label.configure(image=frame)

# to start the loop
check = random.randint(0,1)
win.after(1,change,cycle,check,time)

# to render the pet above all windows
win.lift()
win.attributes('-topmost',False)
win.after_idle(win.attributes,'-topmost',False)

win.mainloop()
