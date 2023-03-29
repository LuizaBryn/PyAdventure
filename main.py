from tkinter import *

class PlayerInterface:
    def __init__(self):
      self.mainWindow = Tk()
      self.mainWindow.title("PyAdventure")
      self.mainWindow.iconbitmap("img/icon.ico")
      self.mainWindow.geometry("1280x720")
      self.mainWindow.resizable(False, False)
      self.mainWindow["bg"] = "#DBE9F4"

      self.combateFrame = Frame(self.mainWindow, width=1280, height=520, bg="#DBE9F4")
      self.barraTarefasFrame = Frame(self.mainWindow, width=1280, height=200, bg="gray")


      self.label1 = Label(self.barraTarefasFrame, text='Sou um label e to no frame das carta na posição 0 0').place(x=0, y=0)

      self.combateFrame.pack()
      self.barraTarefasFrame.pack()

      self.mainWindow.mainloop()


PlayerInterface()
