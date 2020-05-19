import os
import sys
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QRadioButton, QListWidget, QLabel, QSplitter
from PyQt5.QtWidgets import QLineEdit, QWidget, QAction, QFrame
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


# =-=-=-=-=-=-=-=-=-=-Example class=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class MainUI(QMainWindow):
    # *********************Constructor**********************************
    def __init__(self):
        QMainWindow.__init__(self)

        # --------topLayout-------------------------

        self.topLabelWicketKeeper = QLabel("Wicket-Keeper(WK)")
        self.topLabelAllRounder = QLabel("AllRounder(AR)")
        self.topLabelBowl = QLabel("Bowler(BOW)")
        self.topLabelBat = QLabel("Batsmen(BAT)")

        self.topLabelBatBox = QLabel("##")
        self.topLabelBowlBox = QLabel("##")
        self.topLabelAllRounderBox = QLabel("##")
        self.topLabelWicketKeeperBox = QLabel("##")

        # -----------end of topLayout------------------

        # ==============inputLayout===================

        self.pointAvailableBox = QLabel("####")
        self.pointAvailable = QLabel("Point Available")
        self.BAT = QRadioButton("BAT")
        self.BOW = QRadioButton("BOW")
        self.AR = QRadioButton("AR")
        self.WK = QRadioButton("WK")

        self.inputList = QListWidget()

        # ===================end of bottomInputLayout==================

        # ------------------bottomOutputLayout-------------------------
        self.outputList = QListWidget()

        self.pointUsedBox = QLabel("####")
        self.teamName = QLabel("Team Name")
        self.pointUsed = QLabel("Point Used")
        self.teamNameBox = QLabel("Displayed Here")
        # -----------------end of bottomOutputLayout--------------------

        # ===================menu=====================================
        menu = self.menuBar()

        self.manageTeam = menu.addMenu("Manage Team")
        try:
            self.newTeam = QAction(QIcon(resource_path("newImg.png")), "New Team", self)
            self.openTeam = QAction(QIcon(resource_path("openImg.jpg")), "Open Team", self)
            self.saveTeam = QAction(QIcon(resource_path("saveImg.png")), "Save Team", self)
            self.evaluateTeam = QAction(QIcon(resource_path("evaluateImg.png")), "Evaluate team", self)
        except BaseException as err:
            print("Exception handled at line 67 inside constructor of Example Class in design file")
        # ===============end of menu =========================================

        self.initUI()

    # ******************end of Constructor***************************************

    # ************initUI file************************************************

    def initUI(self):

        # ------------topLayout Configure----------------------

        topLabel = QLabel("View Selections")

        topHLayout = QHBoxLayout()

        topFrame = QFrame(self)
        topFrame.setFrameShape(QFrame.StyledPanel)
        topFrame.setObjectName("top_frame")

        topLayout = QVBoxLayout(topFrame)

        topHLayout.addWidget(self.topLabelBat)
        topHLayout.addWidget(self.topLabelBatBox)
        self.topLabelBatBox.setObjectName("blue")
        topHLayout.addStretch(1)

        topHLayout.addWidget(self.topLabelBowl)
        topHLayout.addWidget(self.topLabelBowlBox)
        self.topLabelBowlBox.setObjectName("blue")
        topHLayout.addStretch(1)

        topHLayout.addWidget(self.topLabelAllRounder)
        topHLayout.addWidget(self.topLabelAllRounderBox)
        self.topLabelAllRounderBox.setObjectName("blue")
        topHLayout.addStretch(1)

        topHLayout.addWidget(self.topLabelWicketKeeper)
        topHLayout.addWidget(self.topLabelWicketKeeperBox)
        self.topLabelWicketKeeperBox.setObjectName("blue")
        topHLayout.addStretch(1)

        topLayout.addWidget(topLabel)
        topLayout.addLayout(topHLayout)
        # -------------end of topLayout Configure---------------------

        # ============inputLayout Configure============================

        bottomInputDisplayLayout = QHBoxLayout()

        inputDetailFrame = QFrame(self)
        inputDetailFrame.setFrameShape(QFrame.StyledPanel)
        inputDetailFrame.setObjectName("input_frame")

        bottomInputRadio = QHBoxLayout()
        bottomInput = QVBoxLayout(inputDetailFrame)

        inputFrame = QFrame(self)

        inputLayout = QVBoxLayout(inputFrame)

        bottomInputDisplayLayout.addWidget(self.pointAvailable)
        bottomInputDisplayLayout.addWidget(self.pointAvailableBox)
        self.pointAvailableBox.setObjectName("blue")
        bottomInputDisplayLayout.addStretch(1)

        bottomInputRadio.addWidget(self.BAT)
        bottomInputRadio.addWidget(self.BOW)
        bottomInputRadio.addWidget(self.AR)
        bottomInputRadio.addWidget(self.WK)

        bottomInput.addLayout(bottomInputRadio)
        bottomInput.addWidget(self.inputList)

        inputLayout.addLayout(bottomInputDisplayLayout)
        inputLayout.addWidget(inputDetailFrame)
        # ============end of inputLayout Configure=========================

        # ---------------outputLayout Configure-----------------------------

        bottomOutputDisplayLayout = QHBoxLayout()

        outputDetailFrame = QFrame(self)
        outputDetailFrame.setFrameShape(QFrame.StyledPanel)
        outputDetailFrame.setObjectName("output_frame")

        bottomOutputTeamName = QHBoxLayout()
        bottomOutput = QVBoxLayout(outputDetailFrame)

        outputFrame = QFrame(self)
        outputLayout = QVBoxLayout(outputFrame)

        bottomOutputDisplayLayout.addWidget(self.pointUsed)
        bottomOutputDisplayLayout.addWidget(self.pointUsedBox)
        self.pointUsedBox.setObjectName("blue")
        bottomOutputDisplayLayout.addStretch(1)

        bottomOutputTeamName.addWidget(self.teamName)
        bottomOutputTeamName.addWidget(self.teamNameBox)
        self.teamNameBox.setObjectName("blue")
        bottomOutputTeamName.addStretch(1)

        bottomOutput.addLayout(bottomOutputTeamName)
        bottomOutput.addWidget(self.outputList)

        outputLayout.addLayout(bottomOutputDisplayLayout)
        outputLayout.addWidget(outputDetailFrame)
        # --------------end of outputLayout Configure--------------------------

        # ============total Configure=======================================

        # ===========total Window Configure Variable======================

        totalLayout = QVBoxLayout()
        bottomSplitter = QSplitter(Qt.Horizontal)
        totalSplitter = QSplitter(Qt.Vertical)
        widget = QWidget()

        # ===========end of total Window Configure Variable================

        bottomSplitter.addWidget(inputFrame)
        bottomSplitter.addWidget(outputFrame)

        totalSplitter.addWidget(topFrame)
        totalSplitter.addWidget(bottomSplitter)
        bottomSplitter.setObjectName("main_window")

        # ============end of total Configure================================

        # -------------Styling---------------------------------------------
        stylesheet = """
        #top_frame
        {
            background-color:#e5dfdf;
        }

        #blue
        {
            color:#46b5d1;
        }

        #main_window
        {
            background-color:white;
        }

        QMainWindow
        {
            background-color:white;
        }"""

        # -------------Styling---------------------------------------------

        # ===============setting layout==================================
        self.setCentralWidget(widget)

        totalLayout.addWidget(totalSplitter)

        widget.setLayout(totalLayout)
        # ================end of setting layout==========================

        # ---------------menu Configure------------------------------
        self.manageTeam.addAction(self.newTeam)
        self.manageTeam.addAction(self.openTeam)
        self.manageTeam.addAction(self.saveTeam)
        self.manageTeam.addAction(self.evaluateTeam)
        # ---------------end of menu Configure------------------------

        # ===================main Window configure================================
        self.statusBar()
        self.setStyleSheet(stylesheet)
        self.setWindowTitle("Fantasy Cricket Team")
        self.setGeometry(50, 50, 800, 800)
        self.setWindowIcon(QIcon(resource_path("cricketImg.png")))
        self.show()
# ====================end of main Window configure========================


# =-=-=-=-=-=-=-=-=-=-end of Example class=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)