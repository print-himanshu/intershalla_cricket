import os
import sys

from PyQt5.QtWidgets import QLabel, QComboBox, QSplitter, QPushButton, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon



class openClass(QWidget):
    def __init__(self):
        super().__init__(self)
        self.openTeamSpinner = QComboBox()
        self.openTeamWindow = QWidget()
        self.openTeamButton = QPushButton("Select Team")


    def openTeamInitUI(self):
        openTeamLabel = QLabel("Choose your Team")

        openTeamSplitter = QSplitter(Qt.Vertical)

        openTeamSplitter.addWidget(openTeamLabel)
        openTeamSplitter.addWidget(self.openTeamSpinner)


        openTeamTotalLayout = QVBoxLayout()
        openTeamTotalLayout.addWidget(openTeamSplitter)
        openTeamTotalLayout.addStretch(1)
        openTeamTotalLayout.addWidget(self.openTeamButton)

        self.openTeamWindow.setLayout(openTeamTotalLayout)
        self.openTeamWindow.setWindowTitle("Open Team")
        self.openTeamWindow.setGeometry(200,200,300,300)
        self.openTeamWindow.setWindowIcon(QIcon(resource_path("openImg.jpg")))

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

