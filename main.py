from tkinter import *

class PlayerInterface:
    def __init__(self):
      self.mainWindow = Tk()
      self.mainWindow.title("PyAdventure")
      self.mainWindow.iconbitmap("img/icon.ico")
      self.mainWindow.geometry("1280x720")
      self.mainWindow.resizable(False, False)
      self.mainWindow["bg"] = "#DBE9F4"

      self.barraTarefasFrame = Frame(self.mainWindow, width=1280, height=200, bg="gray")
      self.barraTarefasFrame.grid(row=1, column=2)
      self.barraTarefasFrame.pack(side=BOTTOM, expand=False)

      label1 = Label(self.barraTarefasFrame, text="I'm at (0, 0)", bg="red")
      label1.grid(row=1, column=1)

      self.mainWindow.mainloop()


PlayerInterface()

#teste teste