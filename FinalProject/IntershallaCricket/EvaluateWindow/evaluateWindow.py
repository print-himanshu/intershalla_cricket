import os
import sys

from PyQt5.QtWidgets import QApplication, QWidget,QHBoxLayout,QVBoxLayout, QLabel
from PyQt5.QtWidgets import QFrame, QSplitter, QListWidget, QComboBox, QPushButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtCore import Qt





class EvaluateWindowClass(QWidget):
    #------------Constructor---------
    def __init__(self):
        super().__init__()

        self.evaluateInputList = QListWidget()
        self.evaluateOutputList = QListWidget()
        self.teamSelection = QComboBox()
        self.matchSelection = QComboBox()
        self.evaluateButton = QPushButton("EvaluateTeam")
        self.evaluateWidget = QWidget()
        self.evaluateWindowTotalPoint = QLabel("###")
        


    #---------end of Constructor------------

    #---------------evaluateInflate---------------
    def evaluateInflate(self):
        #=======Configuring bottom layout=============

        #For Bottom Layout Configuration I am using QSplitter
        evaluateBottomSplitter = QSplitter(Qt.Horizontal)

        evaluateBottomLeft = QSplitter(Qt.Vertical)
        bottomLeftPlayer = QLabel("Players")
        evaluateBottomLeft.addWidget(bottomLeftPlayer)
        evaluateBottomLeft.addWidget(self.evaluateInputList)

        evaluateBottomRight= QSplitter(Qt.Vertical)
        bottomPoint = QSplitter(Qt.Horizontal)
        bottomLeftPoint = QLabel("Points")

        bottomPoint.addWidget(bottomLeftPoint)
        bottomPoint.addWidget(self.evaluateWindowTotalPoint)

        evaluateBottomRight.addWidget(bottomPoint)
        evaluateBottomRight.addWidget(self.evaluateOutputList)

        evaluateBottomSplitter.addWidget(evaluateBottomLeft)
        evaluateBottomSplitter.addWidget(evaluateBottomRight)

        #--------button layout Configure -------------------------

        buttonFrame = QFrame()
        buttonLayout = QHBoxLayout(buttonFrame)
        buttonLayout.addStretch(1)
        buttonLayout.addWidget(self.evaluateButton)
        buttonLayout.addStretch(1)
        evaluateBottomSplitter.addWidget(buttonFrame)
        #---------end of button layout configure----------------

        #=========end of bottom Layout Configuration==============




        #===========Configuring Total Layout========================

        #Top Layout frame and Splitter
        evaluateTopFrame = QFrame()
        evaluateTopLayout = QHBoxLayout(evaluateTopFrame)
        evaluateTopLabel = QLabel("Evaluate the Performance of your Fantasy Team")

        #Total Layout Splitter and Layout
        evaluateTotalSplitter = QSplitter(Qt.Vertical)
        evaluateTotalLayout = QVBoxLayout()


        evaluateTopLayout.addWidget(self.teamSelection)
        evaluateTopLayout.addWidget(self.matchSelection)

        evaluateTotalSplitter.addWidget(evaluateTopLabel)
        evaluateTotalSplitter.addWidget(evaluateTopFrame)
        evaluateTotalSplitter.addWidget(evaluateBottomSplitter)

        evaluateTotalLayout.addWidget(evaluateTotalSplitter)

        #=======end of Configuring Total Layout========================





        #=============Combo Box initial value==========================
        DisplayMessage1 = QLineEdit()
        DisplayMessage1.setPlaceholderText("Select Team")
        self.teamSelection.setLineEdit(DisplayMessage1)
        DisplayMessage2 = QLineEdit()
        DisplayMessage2.setPlaceholderText("Select Match")
        self.matchSelection.setLineEdit(DisplayMessage2)

        #============end of Combo Box ==================================
        
        self.evaluateWidget.setLayout(evaluateTotalLayout)
        self.evaluateWidget.setWindowTitle("Evaluate Team")
        self.evaluateWidget.setGeometry(50,50,600,800)
        self.evaluateWidget.setWindowIcon(QIcon(resource_path("evaluateImg.png")))

#-------------------end  of Evaluate Window----------------------------------

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)