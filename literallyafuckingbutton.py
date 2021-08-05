import tkinter as tk


curcolor = True


def InitTK():
    root= tk.Tk()
    root.title("A Fucking Button")
    root.configure(background="black")
    return root

class MainWindow(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master = master
        self.configure(width=600,height=400,bg="black")
        self.mainFunc()
        self.pack()

    def mainFunc(self):
        self.btn = tk.Button(self,text="",bg="red",command=self.changecolor)
        self.btn.place(x=200,y=150,width=200,height=100)

        self.lbl = tk.Label(self,text="Useless Button!",bg="black",fg="white",font="Rockwell 20 bold",anchor="c")
        self.lbl.place(x=200,y=25,width=200,height=100)

    def changecolor(self):
        global curcolor
        if curcolor:
            curcolor = False
            self.btn.config(bg="green")
        else:
            curcolor = True
            self.btn.config(bg="red")


if __name__ == "__main__":
    root = InitTK()
    window = MainWindow(root)
    root.mainloop()
