from tkinter import *

# --------- importações do PyNetgames que serão usadas posteriormente(?): -----------

# import logging
# from typing import Dict, Optional
# from uuid import UUID

# from py_netgames_client.tkinter_client.PyNetgamesServerListener import PyNetgamesServerListener
# from py_netgames_client.tkinter_client.PyNetgamesServerProxy import PyNetgamesServerProxy
# from py_netgames_model.messaging.message import MatchStartedMessage, MoveMessage

# from tkinter_sample.ServerConnectionMenubar import ServerConnectionMenubar

# -------------------------------------------------------------------------------------


class PyAdventureInterface():

    # _tk: Tk
    # _server_proxy: PyNetgamesServerProxy
    # _menu_bar = ServerConnectionMenubar
    # _ongoing_match: bool
    # _match_id: UUID
    # _board: Optional[PyAdventureBoard]
    # _buttons: Dict[PyAdventureCoordinate, Button]
    # _logger: logging.Logger

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
            self.mainWindow)
        self.barraTarefasFrame.grid(row=2, column=0, sticky="nsew")
        self.barraTarefasFrame.grid_columnconfigure(
            0, weight=7)  # coluna das cartas
        self.barraTarefasFrame.grid_columnconfigure(
            1, weight=2)  # coluna do menu
        self.barraTarefasFrame.grid_rowconfigure(0, weight=1)

        self.cardBoard = Frame(self.barraTarefasFrame, bg="#56899F")
        self.cardBoard.grid(row=0, column=0, sticky="nsew")
        self.cardBoard.grid_rowconfigure(0, weight=1)
        self.cardBoard.grid_rowconfigure(1, weight=10)

        self.menu = Frame(self.barraTarefasFrame, bg="#36696F")
        self.menu.grid(row=0, column=1, sticky="nsew")
        self.menu.grid_rowconfigure(0, weight=1)
        self.menu.grid_rowconfigure(1, weight=1)
        self.menu.grid_columnconfigure(0, weight=1)

        for i in range(4):
            self.cardBoard.grid_columnconfigure(i, weight=1)

            carta = Button(self.cardBoard, name=str(i), text="Carta {}".format(i+1),
                           padx=50, pady=80, command=self.remove_card)
            carta.grid(row=1, column=i)

            carta.bind('<Button-1>', self.remove_card)

        self.pular_vez = Button(self.menu, text="Passar vez", bg="#91DBBB", fg="black", font=("Arial", 14),
                                width=10, height=2, bd=5, relief="raised", activebackground="#254954", activeforeground="white", command=self.add_card)
        self.pular_vez.grid(row=0, column=0)

        self.card_description = Button(self.menu, text="Cartas", bg="#91DBBB", fg="black", font=("Arial", 14),
                                       width=10, height=2, bd=5, relief="raised", activebackground="#254954", activeforeground="white", command=self.see_cards)
        self.card_description.grid(row=1, column=0)

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

    def see_cards(self):
        popup = Toplevel(self.mainWindow)
        popup.title("Cartas PyAdventure")
        popup.geometry("200x100")
        popup_label = Label(popup, text="Aqui ficarão as descrições!")
        popup_label.pack()


PyAdventureInterface()
