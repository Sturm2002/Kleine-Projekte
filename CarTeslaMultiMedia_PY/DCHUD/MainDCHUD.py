
import GUIDCHUD,globs

def Start():
    global root,DCWin
    root = GUIDCHUD.InitTK()
    DCWin = GUIDCHUD.MainDC(root)
    #root.after(0, DCWin.UpdateSplash, 0)
    root.bind("<KeyPress>",GetKeyPress)
    root.mainloop()

def GetKeyPress(event):
    global DCWin
    if event.char == "+":
        DCWin.Testplus()
    elif event.char == "-":
        DCWin.Testminus()
            
        
    if event.keysym == "Escape":
        exit()

if __name__ == "__main__":
    Start()