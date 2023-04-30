import logging
from game_logic.interface.py import PyAdventureInterface

if __name__ == "main":
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("main.py").info("Project has run")
    PyAdventureInterface()
