import MainGUI,globalVars,Datenbank

def MainFunc():
    global root,window
    Datenbank.connection()
    root = MainGUI.InitTK()
    window = MainGUI.MainWindow(root)

    root.bind("<KeyPress>",GetKeyPress)

    root.mainloop()
    
def GetKeyPress(event):
    global window
    if window.CurrentGame == 0:
        #print(event.char)
        if window.CurrentScreen == "options":
            if event.char == "+":
                window.btn_ScreenMultSizeUp_pressed()
            elif event.char == "-":
                window.btn_ScreenMultSizeDown_pressed()
            
        
        if event.keysym == "Escape":
            window.InitLoadingScreen("main")

if __name__ == "__main__":
    MainFunc()

# Project By Alex Bruksch | Nick Dziewior | Jean Neumann | Daniel Pyka