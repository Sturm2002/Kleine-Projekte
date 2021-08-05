from tkinter import *

def motion(event):
  msg.config(text="Whatever You do")
  return

def RightClick(event):
    msg.config(text=whatever_you_do)
    return

master = Tk()
whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
msg = Message(master, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.bind('<Button-3>',motion)
msg.bind("<Button-1>",RightClick)
msg.pack()
mainloop()