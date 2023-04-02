from tkinter import *


class PlayerInterface:
    def __init__(self):
        self.mainWindow = Tk()
        self.mainWindow.title("PyAdventure")
        self.mainWindow.iconbitmap("img/icon.ico")
        self.mainWindow.resizable(False, False)
        self.mainWindow.geometry("1280x720")
        self.mainWindow["bg"] = "#DBE9F4"
        self.mainWindow.grid_columnconfigure(0, weight=1)
        self.mainWindow.grid_rowconfigure(0, weight=1)
        self.mainWindow.grid_rowconfigure(1, weight=20)
        self.mainWindow.grid_rowconfigure(2, weight=3)

        self.statusBoard = Frame(self.mainWindow)
        self.statusBoard.grid(row=0, column=0, sticky="nsew")
        self.statusBoard.grid_columnconfigure(0, weight=1)
        self.statusBoard.grid_columnconfigure(1, weight=6)
        self.statusBoard.grid_columnconfigure(2, weight=1)
        self.statusBoard.grid_rowconfigure(0, weight=1)
        self.statusBoard.grid_rowconfigure(1, weight=1)

        self.lifePlayer1 = Label(self.statusBoard, text="Vida: X")
        self.lifePlayer1.grid(row=0, column=0)
        self.manaPlayer1 = Label(
            self.statusBoard, text="Mana: X", padx=0, pady=0)
        self.manaPlayer1.grid(row=1, column=0)
        self.lifePlayer2 = Label(self.statusBoard, text="Vida: Y")
        self.lifePlayer2.grid(row=0, column=2)
        self.lifePlayer2 = Label(
            self.statusBoard, text="Mana: Y", padx=0, pady=0)
        self.lifePlayer2.grid(row=1, column=2)
        self.roundCounter = Label(self.statusBoard, text="Round X")
        self.roundCounter.grid(row=0, column=1)

        self.barraTarefasFrame = Frame(
            self.mainWindow, bg="#36696F")
        self.barraTarefasFrame.grid(row=2, column=0, sticky="nsew")
        self.barraTarefasFrame.grid_columnconfigure(0, weight=6)
        self.barraTarefasFrame.grid_columnconfigure(1, weight=1)
        self.barraTarefasFrame.grid_rowconfigure(0, weight=1)

        self.cardBoard = Frame(self.barraTarefasFrame, bg="#56899F")
        self.cardBoard.grid(row=0, column=0, sticky="nsew")
        self.cardBoard.grid_rowconfigure(0, weight=1)
        self.cardBoard.grid_rowconfigure(1, weight=10)

        for i in range(5):
            self.cardBoard.grid_columnconfigure(i, weight=1)

            carta = Button(self.cardBoard, name=str(i), text="Carta {}".format(i+1),
                           padx=50, pady=80, command=self.remove_card)
            carta.grid(row=1, column=i)

            carta.bind('<Button-1>', self.remove_card)

        self.pular_vez = Button(self.barraTarefasFrame, text="Passar vez", bg="#91DBBB", fg="black", font=("Arial", 14),
                                width=10, height=2, bd=5, relief="raised", activebackground="#254954", activeforeground="white", command=self.add_card)
        self.pular_vez.grid(row=0, column=1)

        self.mainWindow.mainloop()

    def remove_card(self, event=None):
        card = event.widget
        column = int(card.winfo_name())
        card.grid_remove()
        self.cardBoard.grid_columnconfigure(column, minsize=0)

    def add_card(self, event=None):
        new_column = self.cardBoard.grid_size()[0] + 1
        self.cardBoard.grid_columnconfigure(new_column, weight=1)
        new_card = Button(self.cardBoard, text="Carta", name=str(new_column),
                          padx=50, pady=80)
        new_card.grid(row=1, column=new_column)
        new_card.bind('<Button-1>', self.remove_card)


PlayerInterface()
