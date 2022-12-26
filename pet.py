import tkinter
import pyautogui
import random

win = tkinter.Tk()

idle = [tkinter.PhotoImage(file = r"C:\Users\Aaron Geo Binoy\Virtual-Pet\src\assets\Pochita_Idle_Animated_1.gif",format = 'gif -index %i' %(i)) for i in range(31)]

cycle = 0
check = 1

def update(cycle,check,event_number,x):
 #idle
 if check ==0:
  frame = idle[cycle]
  cycle ,event_number = work(cycle,idle,event_number,1,9)

  win.geometry('100x100+'+str(1400)+'+1050')
  label.configure(image=frame)
  win.after(1,event,cycle,check,event_number,x)

def event(cycle,check,event_number,x):
 if event_number in idle_num:
  check = 0
  print('idle')
  win.after(400,update,cycle,check,event_number,x)

def work(cycle,frames,event_number,first_num,last_num):
 if cycle < len(frames) -1:
  cycle+=1
 else:
  cycle = 0
  event_number = random.randrange(first_num,last_num+1,1)
 return cycle,event_number

win.config(highlightbackground='white')
win.overrideredirect(True)
win.wm_attributes('-transparentcolor','white')

label = tkinter.Label(win,bd=0,bg='white')
label.pack()

win.after(1,update,cycle,check,event_number,x)
win.mainloop()
