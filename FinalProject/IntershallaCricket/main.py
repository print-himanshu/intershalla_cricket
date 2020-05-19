from PyQt5.QtWidgets import QApplication
from sys import argv,exit
from IntershallaCricket.PreProcessing import Handling
from IntershallaCricket.Database import databaseFile

from os import path #For checking database file is created or not


if __name__ == "__main__":
    #Database Created
    if not path.exists("player.db"):
        creatingDatabase = databaseFile.databaseEntry()

    #Inflating UI
    app = QApplication(argv)
    inflatingUI = Handling.UIHandling()
    exit(app.exec_())