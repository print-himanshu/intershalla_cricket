from PyQt5.QtWidgets import QInputDialog, QWidget, QMessageBox
from IntershallaCricket.Design import design
from IntershallaCricket.EvaluateWindow import evaluateWindow
from IntershallaCricket.OpenTeam import openWindow
from IntershallaCricket.Evaluate import evaluate
import sqlite3


#Inheritance Diagram
# SubPackage Name :        Design               EvaluateWindow                      OpenTeam
# Module Name:              -- design.py             --evaluateWindow.py                -- openWindow.py
# Class Name:                   --MainUI               --EvaluateWindowClass               --openClass
#                                   |                             |                            |
#                                                         UIHandling
class UIHandling(design.MainUI, evaluateWindow.EvaluateWindowClass, openWindow.openClass):

    def __init__(self, parent=None):

        #parent Constructor call
        design.MainUI.__init__(self)       #This Parent Constructor is of Design Module which initialize the main UI

        evaluateWindow.EvaluateWindowClass.__init__(self) #This Parent Constructor is of EvaluateWindow Module which initialize
                                                          #the evaluate window UI when evaluate action from the menubar is clicked

        openWindow.openClass.__init__(self) #This Parent Constructor is of OpenTeam Module which initialize the UI when openTeam
                                            #action is clicked from the menu
        #List of variable needed by Handling module
        self.newTeamFlag = False   # This variable is used for knowing, if the new team action from the menubar is clicked or not,
                                   # If False means the newTeam Action from menubar is not clicked and nothing in the UI should work.
                                   # If True then the newTeam action is clicked and now the UI is initialized with value corresponding
                                   #  to the tagand radio button and list starts working

        self.teamNameVar = ""      # This variable stores the currently selected teamName in the Main UI

        self.fetchData = []        # This variable is used to stores the data fetch from the database during every UI handling
        self.mydb = None           # This variable is used to connect with the sqlite database
        self.mycursor = None       # This variable is used for operation in the database

        self.teamResult = []       # self.teamResult is used for storing all the team Name from the database
        self.matchResult = []      # self.matchResult is used for storing the point after evaluation of score of a team
        self.playerName = ()        # This variable is used for storing the name of all the player of a team

        self.totalPoint = 0         # This variable is used for storing the addition of the evaluated score

        # Method calling
        self.definingMethod()       # Method of UIHandling class from handling.py
        self.openTeamInitUI()       # Method of openClass class from openWindow.py
        self.evaluateInflate()      # Method of EvaluateWindowClass class from evaluateWindow.py
        #self.sameTeamName = ""

    def definingMethod(self):
        #Defining Method for knowing what should happen when the UI is interacted

        # Taking Care of all the Menu Bar action interaction
        self.newTeam.triggered.connect(self.newTeamAction)
        self.evaluateTeam.triggered.connect(self.evaluateTeamAction)
        self.saveTeam.triggered.connect(self.saveTeamAction)
        self.openTeam.triggered.connect(self.openTeamAction)

        # Taking Care of all the Radio Button Toggled of the Main UI
        self.BAT.toggled.connect(lambda: self.btnState(self.BAT))
        self.BOW.toggled.connect(lambda: self.btnState(self.BOW))
        self.AR.toggled.connect(lambda: self.btnState(self.AR))
        self.WK.toggled.connect(lambda: self.btnState(self.WK))

        # Taking care of all the list double click of teh main ui
        self.inputList.itemDoubleClicked.connect(self.removeInputList)
        self.outputList.itemDoubleClicked.connect(self.removeOutputList)

        # Taking care of the button click
        self.evaluateButton.clicked.connect(self.inflateList)
        self.openTeamButton.clicked.connect(self.openTeamButtonAction)


    def newTeamAction(self):
        # Handling new Team Action of the Menu
        # QInputDialog return entered text and a boolean value
        # For taking team Name and connecting to database

        test, ok = QInputDialog.getText(self, "New Team", "Enter Team Name : ")

        # ----If user after entering name press enter then ok is true-----
        # Setting all the blank field in the UI with its corresponding value
        # Setting Status message for the blank field
        if ok == True:
            self.outputList.clear()
            self.teamNameVar = str(test)
            self.CheckingTeamNameExist()

            self.mydb = sqlite3.connect("player.db")
            self.mycursor = self.mydb.cursor()
            # setting a Class Attribute for knowing that the new TEam action is pressed or not
            self.newTeamFlag = True
            # setting Bat radio button to be toggled initially
            self.BAT.setChecked(False)
            self.BAT.setChecked(True)

            self.initializationOfUI(self.teamNameVar)       #Method Call


    def removeInputList(self, item):
        # ===============handling Input list function in UI===================
        # Fetching the data from the stats database and filling it in the fetchData variable
        # For removing the item from the input list and placing it in the output list
        # we need to make sure some conditions
        # 1.) Output List should not have more than 11 players
        self.fetchData = []
        selectQuery = " select player,value,ctg from stats;"

        temp = self.mycursor.execute(selectQuery).fetchall()
        for i in range(len(temp)):
            self.fetchData.append(list(temp[i]))
        temp.clear()
        if self.outputList.count() <= 11:

            self.inputList.takeItem(self.inputList.row(item))
            playerName = item.text().split(" ")
            # ---------searching for the selected item from the listWidget
            for i in range(len(self.fetchData)):
                if self.fetchData[i][0] == playerName[0]:
                    break

            # ----------------Updating point Variable in UI--------------------
            temp = self.pointAvailableBox.text()
            try:
                value = int(temp)
                updateValue = value - self.fetchData[i][1]
                if updateValue < 0:
                    QMessageBox.warning(self, "Warning", "You don't have enough points available")
                    self.inputList.addItem(item.text())

                else:
                    self.pointAvailableBox.setText(str(updateValue))
                    temp = int(self.pointUsedBox.text())
                    updateValue = temp + self.fetchData[i][1]
                    self.pointUsedBox.setText(str(updateValue))

                    # ------------Updating the topLayout in UI-----------------------------
                    if self.fetchData[i][2] == "BAT":
                        temp = self.topLabelBatBox.text()
                        topValue = int(temp)
                        topValue += 1
                        self.topLabelBatBox.setText(str(topValue))


                    elif self.fetchData[i][2] == "BWL":
                        temp = self.topLabelBowlBox.text()
                        topValue = int(temp)
                        topValue += 1
                        self.topLabelBowlBox.setText(str(topValue))


                    elif self.fetchData[i][2] == "AR":
                        temp = self.topLabelAllRounderBox.text()
                        topValue = int(temp)
                        topValue += 1
                        self.topLabelAllRounderBox.setText(str(topValue))


                    elif self.fetchData[i][2] == "WK":
                        temp = self.topLabelWicketKeeperBox.text()
                        topValue = int(temp)
                        if topValue == 0:
                            topValue += 1
                            self.topLabelWicketKeeperBox.setText(str(topValue))
                            self.outputList.addItem(item.text())

                        elif topValue > 0:
                            QMessageBox.warning(self, "Warning", "You can't select more than one wicket keeper")
                            self.inputList.addItem(item.text())
                            self.pointAvailableBox.setText(str(value))
                            self.pointUsedBox.setText(str(int(self.pointUsedBox.text()) - self.fetchData[i][1]))

                    if self.fetchData[i][2] != "WK":
                        self.outputList.addItem(item.text())

                # ----------end of updation of the topLayout in UI--------------


            except ValueError as err:
                print("Fetch value cant be typecasted in integer")
                print("value : ", value)
                print("Error : ", err)

        # -----------------end of Updating point Variable in UI------------------
        else:
            QMessageBox.warning(self, "Warning", "You can not select more than 11 players")


    def removeOutputList(self, item):
        # ==========handling output list================================
        # For taking care of moving the item from the output list to input list
        # on moving that item whole UI variable had some change in its value
        self.fetchData = []
        self.outputList.takeItem(self.outputList.row(item))
        playerName = item.text().split(" ")
        removeOutputListSelectQuery = "select * from stats where player like '%s';" % (playerName[0])
        try:
            self.fetchData = self.mycursor.execute(removeOutputListSelectQuery).fetchone()
        except sqlite3.Error as err:
            print(err)
        # ----------------Updating point Variable in UI--------------------
        temp = self.pointUsedBox.text()
        try:
            value = int(temp)
            updateValue = value - self.fetchData[1]
            self.pointUsedBox.setText(str(updateValue))

            temp = int(self.pointAvailableBox.text())
            updateValue = temp + self.fetchData[1]
            self.pointAvailableBox.setText(str(updateValue))

            # ------------Updating the topLayout in UI-----------------------------
            if self.fetchData[6] == "BAT":
                temp = self.topLabelBatBox.text()
                self.topLabelBatBox.setText(str(int(temp) - 1))


            elif self.fetchData[6] == "BWL":
                temp = self.topLabelBowlBox.text()
                self.topLabelBowlBox.setText(str(int(temp) - 1))

            elif self.fetchData[6] == "AR":
                temp = self.topLabelAllRounderBox.text()
                self.topLabelAllRounderBox.setText(str(int(temp) - 1))

            elif self.fetchData[6] == "WK":
                temp = self.topLabelWicketKeeperBox.text()
                self.topLabelWicketKeeperBox.setText(str(int(temp) - 1))

            # ----------end of updation of the topLayout in UI--------------
            try:
                ctgSelectQuery = "select ctg from stats where player like '%s'" % (playerName[0])
                againToInputList = self.mycursor.execute(ctgSelectQuery).fetchone()
            except sqlite3.Error as err:
                print("Error caused in line 213 in removeOutputList function")
                print(err)
            try:
                fetchedCategory = againToInputList[0]

                if self.BAT.isChecked():
                    RadioVar = "BAT"
                elif self.BOW.isChecked():
                    RadioVar = "BWL"
                elif self.AR.isChecked():
                    RadioVar = "AR"
                elif self.WK.isChecked():
                    RadioVar = "WK"

                if RadioVar == fetchedCategory:
                    self.listFillingFn(RadioVar)
            except UnboundLocalError as err:
                print("Error occur in line 231 in removeOutputList function")
                print(err)
            except TypeError as err:
                print("Error occur in line 234 in removeOutputList function")
                print(err)
            except:
                print("Error occur in line 237 in removeOutputList function")
                print("Handle by except statement")
                print(err)




        except ValueError as err:
            print("Fetch value cant be typecasted in integer")
            print("value : ", value)
            print("Error : ", err)


    def btnState(self, pressedRadio):
    # For handling of Radio Button toggle
    # Checking which Radio Button is toggled currently
    # after checking passing the toggled radio button tag(name)
    # to a function listFilling

        if pressedRadio.isChecked():
            if self.newTeamFlag == True:
                self.inputList.clear()
                if pressedRadio.text() == "BOW":
                    tag = "BWL"
                else:
                    tag = str(pressedRadio.text())

                self.listFillingFn(tag) #Calling list Filling function


            else:
                # if the RadioButton is toggled without clicking on the new team action of the menubar
                # Then this warning message box will pop up on the screen.
                QMessageBox.warning(self, "Selection Error",
                                    """For Selection of Player\nGo to Manage Teams ----> New Team """)

    def evaluateTeamAction(self):

        self.evaluateWidget.show()
        try:
            evaluateFlag = False
            # Clearing the initial UI of the Evaluation window
            self.teamSelection.clear()
            self.matchSelection.clear()
            self.evaluateInputList.clear()
            self.evaluateOutputList.clear()

            # Creating a connection to the database
            self.mydb = sqlite3.connect("player.db")
            self.mycursor = self.mydb.cursor()

            # Fetching the team name and match name from the database for inflating the list to the spinner
            # in the evaluate window UI
            self.teamInDatabase()
            self.matchResult = self.mycursor.execute(
                "select name from sqlite_master where type = 'table' and name like 'match%'").fetchall()

            # Taking care that we have atleast one team and match for inflating it in the spinner
            if self.teamResult == None:
                QMessageBox.warning(self, "Warning", "Before Evaluating Score Please Create atleast one Team")
                evaluateFlag = True
            if self.matchResult == None:
                QMessageBox.warning(self, "Warning", "You dont have any Match database Available")
                evaluateFlag = True
            # After filling the spinner item we will fill the list
            if evaluateFlag == False:
                for i in range(len(self.teamResult)):
                    self.teamSelection.addItem(self.teamResult[i][0])
                for i in range(len(self.matchResult)):
                    self.matchSelection.addItem(self.matchResult[i][0])
                # print(self.teamResult)
                # print(self.matchResult)


        except sqlite3.Error as err:
            print("Exception Handled at line 334 in evaluateTeamAction function")
            print(err)
            self.mydb.rollback()
        except TypeError as err:
            print("Exception handled at line 338 in evaluateTeamAction function")
            print(err)
        except BaseException as err:
            print("Exception handle by except statement at line 341 in evaluateTeamFunction")
            print(err)
        finally:
            self.mycursor.close()
            self.mydb.close()

    def saveTeamAction(self):
        if self.outputList.count() == 11:
            try:
                self.fetchData = []
                for index in range(self.outputList.count()):
                    try:
                        temp = self.outputList.item(index).text()
                        secondVariable = temp.split(" ")

                    except BaseException as err:
                        print("Error occured in line 324 by saveTeamAction")
                        print(err)

                    self.fetchData.append((self.teamNameVar, secondVariable[0], 0))

                self.CheckingTeamNameExist()



                if self.topLabelWicketKeeperBox.text() == "0":
                    QMessageBox.warning(self, "Warning", "No Wicket Keeper Selected")
                    self.WK.setChecked(True)
                elif self.topLabelWicketKeeperBox.text() > "1":
                    QMessageBox.warning(self, "Warning", "You can select only one wicket keeper")
                    self.WK.setChecked(True)
                else:
                    self.updatingDatabaseAfterSave()
                    self.inputList.clear()
                    self.outputList.clear()
                    self.saveTeamRestorationOfUI()
                    self.mycursor.close()
                    self.mydb.close()

            except BaseException as err:
                print("Error at line 350 inside saveTeamAction() in MenuHandling")
                print(err)

        else:
            QMessageBox.warning(self, "Warning", "You should have 11 player in the team before saving the team")

    def inflateList(self):
        self.playerName = ()
        self.totalPoint = 0
        try:
            self.evaluateInputList.clear()
            self.evaluateOutputList.clear()
            self.mydb = sqlite3.connect("player.db")
            self.mycursor = self.mydb.cursor()
            if self.teamSelection.currentIndex() != -1:
                if self.matchSelection.currentIndex() != -1:
                    currentTeam = self.teamSelection.itemText(self.teamSelection.currentIndex())
                    currentMatch = self.matchSelection.itemText(self.matchSelection.currentIndex())
                    evaluateplayerSelect = "select players from '%s';" % (currentTeam)
                    self.playerName = self.mycursor.execute(evaluateplayerSelect).fetchall()
                    # print(self.playerName)
                    evaluateCalcVar = evaluate.MatchData()
                    for i in range(0, len(self.playerName)):
                        evaluateCalcVar.initialization()
                        returnedPoint = evaluateCalcVar.calculatingMOM(currentMatch, self.playerName[i][0])
                        self.evaluateInputList.addItem(self.playerName[i][0])
                        self.totalPoint += returnedPoint
                        self.evaluateOutputList.addItem(str(returnedPoint))
                        tableUpdateQuery = "update '%s' set value = '%s' where players like '%s' ;" % (
                            currentTeam, returnedPoint, self.playerName[i][0])
                        self.mycursor.execute(tableUpdateQuery)
                        self.mydb.commit()
                    # print(self.totalPoint)
                    self.evaluateWindowTotalPoint.setText(str(self.totalPoint))
                else:
                    QMessageBox.warning(self, "Warning", "You have not selected any match")
            else:
                QMessageBox.warning(self, "Warning", "No Team has been selected")
        except sqlite3.Error as err:
            print("""Error in inflate list method:
                'MenuHandling.py' line 396 function inflateList""", err)
            self.mydb.rollback()
        except BaseException as err:
            print(err)
            print("Exception handled at line 373 inside inflateListMethod function in menuHandling file")
        finally:
            self.mycursor.close()
            self.mydb.close()

    def listFillingFn(self, pressedRadio):
        self.inputList.clear()
        self.fetchData = []
        try:
            selectQuery = " select player,value,ctg from stats where ctg like '%s'; " % (pressedRadio)
            # print(selectQuery)
            temp = self.mycursor.execute(selectQuery).fetchall()
            for i in range(len(temp)):
                self.fetchData.append(list(temp[i]))
            temp.clear()
            msg = ""
            for i in range(len(self.fetchData)):
                msg = self.fetchData[i][0] + " \t point : " + str(self.fetchData[i][1]) + " \t ctg : " + \
                      self.fetchData[i][2]
                # print(msg)
                self.fetchData[i][0] = msg
            # Validating that after the output list is populated
            # Radio Button does not show the output list item in input list---------------------
            tempOutputData = []
            for i in range(self.outputList.count()):
                tempOutputData.append(self.outputList.item(i).text())

            for i in range(0, len(self.fetchData)):
                outputDataMatchVar = False
                for j in range(0, len(tempOutputData)):
                    if self.fetchData[i][0] == tempOutputData[j]:
                        outputDataMatchVar = True
                        break

                if outputDataMatchVar == False:
                    self.inputList.addItem(self.fetchData[i][0])
            # ----------------------------end of Validation---------------------------------------

        except sqlite3.Error as err:
            print("Exception hadled at line 388 in listFillingfn function")
            print(err)
            QMessageBox.warning(self, "Selection Error",
                                """For Selection of Player\nGo to Manage Teams ----> New Team """)

    def saveTeamRestorationOfUI(self):
        self.topLabelBatBox.setText("##")
        self.topLabelBowlBox.setText("##")
        self.topLabelAllRounderBox.setText("##")
        self.topLabelWicketKeeperBox.setText("##")
        self.pointAvailableBox.setText("##")
        self.pointUsedBox.setText("##")
        self.teamNameBox.setText("##")
        self.teamNameVar = ""
        self.newTeamFlag = False

    def openTeamAction(self):

        self.openTeamWindow.show()
        self.openTeamSpinner.clear()
        try:
            self.mydb = sqlite3.connect("player.db")
            self.mycursor = self.mydb.cursor()

            openTeamSelectQuery = "select name from sqlite_master where type = 'table' and name not like 'match%' and name not like 'stat%'"
            openTeamTemp = self.mycursor.execute(openTeamSelectQuery).fetchall()
            for i in range(len(openTeamTemp)):
                self.openTeamSpinner.addItem(openTeamTemp[i][0])

        except sqlite3.Error as err:
            print("Exception handled from openTeamButtonAction Function from UIHandling File")
            print(err)

        except BaseException as err:
            print("Exception handled from openTeamButtonAction Function from UIHandling file")
            print(err)

    def openTeamButtonAction(self):
        try:
            btgCtgCount = 0
            bowlCtgCount = 0
            ARCtgCount = 0
            WKCtgCount = 0
            pointUsedCount = 0
            if self.openTeamSpinner.currentIndex() != -1:
                self.outputList.clear()
                teamName = self.openTeamSpinner.itemText(self.openTeamSpinner.currentIndex())
                openTeamSelectQueryforTeam = "select players, value from '%s' " % (teamName)
                self.fetchData = []
                self.fetchData = self.mycursor.execute(openTeamSelectQueryforTeam).fetchall()
                evaluateScore = 0
                for i in range(len(self.fetchData)):
                    evaluateScore += self.fetchData[i][1]
                    updateQuery = "select player, value, ctg from stats where player like '%s'" % (self.fetchData[i][0])
                    openTeamValue = self.mycursor.execute(updateQuery).fetchone()
                    message = {}

                    message = openTeamValue[0] + " \t point : " + str(openTeamValue[1]) + " \t ctg : " + openTeamValue[
                        2]
                    pointUsedCount += openTeamValue[1]
                    if openTeamValue[2] == "BAT":
                        btgCtgCount += 1
                    elif openTeamValue[2] == "BWL":
                        bowlCtgCount += 1
                    elif openTeamValue[2] == "AR":
                        ARCtgCount += 1
                    elif openTeamValue[2] == "WK":
                        WKCtgCount += 1

                    self.outputList.addItem(message)

                self.initializationOfUI(teamName, btgCtgCount, bowlCtgCount, ARCtgCount, WKCtgCount, pointUsedCount,
                                        (1000 - pointUsedCount))
                self.newTeamFlag = True
                self.openTeamWindow.close()
                if evaluateScore == 0:
                    QMessageBox.information(self, "Information", "Team has been opened\nEvaluation of Team is Remaning")
                else:
                    QMessageBox.information(self, "Information",
                                            "Team has been opened\nEvaluation of Team is %s" % (evaluateScore))

            else:
                QMessageBox.warning(self, "Warning",
                                    """Currently there are zero team in your Database\nPlease Create a New Team\nGo to ManageTeam ---->NewTeam""")
        except sqlite3.Error as err:
            print("Exception handled from openTeamButtonAction Function from UIHandling File")
            print("Handled at line 502 inside openTeamButtonAction")
            print(err)

        except BaseException as err:
            print("Exception handled from openTeamButtonAction Function from UIHandling file")
            print("Handled at line 507 inside openTeamButtonAction function")
            print(err)

    def initializationOfUI(self, name="###", bat=0, bowl=0, ar=0, wk=0, pointUsed=0, pointAv=1000):
        self.topLabelBatBox.setText(str(bat))
        self.topLabelBowlBox.setText(str(bowl))
        self.topLabelAllRounderBox.setText(str(ar))
        self.topLabelWicketKeeperBox.setText(str(wk))
        self.pointAvailableBox.setText(str(pointAv))
        self.pointUsedBox.setText(str(pointUsed))
        self.teamNameBox.setText(name)

        # ---------------------Status Tip Handling---------------------------------------
        self.pointUsed.setStatusTip("Used Point : %s " % (self.pointUsedBox.text()))
        self.teamName.setStatusTip("Your Team Name : %s " % (self.teamNameBox.text()))
        self.pointAvailable.setStatusTip("Remaining Point : %s " % (self.pointAvailableBox.text()))
        self.topLabelBat.setStatusTip("Your Team has Currently : %s Batsman" % (self.topLabelBatBox.text()))
        self.topLabelBowl.setStatusTip("Your Team has Currently : %s Bowler" % (self.topLabelBowlBox.text()))
        self.topLabelAllRounder.setStatusTip(
            "Your Team has Currently : %s All Rounder" % (self.topLabelAllRounderBox.text()))

        self.topLabelWicketKeeper.setStatusTip(
            "Your Team has Currently : %s Wicket Keeper" % (self.topLabelWicketKeeperBox.text()))

        self.pointAvailableBox.setStatusTip("Remaining Point : %s " % (self.pointAvailableBox.text()))
        self.pointUsedBox.setStatusTip("Used Point : %s " % (self.pointUsedBox.text()))
        self.teamNameBox.setStatusTip("Your Team Name : %s " % (self.teamNameBox.text()))
        self.topLabelBatBox.setStatusTip("Your Team has Currently : %s Batsman" % (self.topLabelBatBox.text()))
        self.topLabelBowlBox.setStatusTip("Your Team has Currently : %s Bowler" % (self.topLabelBowlBox.text()))
        self.topLabelAllRounderBox.setStatusTip(
            "Your Team has Currently : %s All Rounder" % (self.topLabelAllRounderBox.text()))

        self.topLabelWicketKeeperBox.setStatusTip(
            "Your Team has Currently : %s Wicket Keeper" % (self.topLabelWicketKeeperBox.text()))
        # --------------------------End of Status Tip Handling

    def CheckingTeamNameExist(self):
        # ====Checking for the Team Exists or not==================
        teamNameDataBeforeSearch = []
        searchingNameQuery = "select name from sqlite_master where type = 'table' and name not like 'match%' and name not like 'stat%'"
        try:
            self.mydb = sqlite3.connect("player.db")
            self.mycursor = self.mydb.cursor()
            existingTeamTemp = self.mycursor.execute(searchingNameQuery).fetchall()
        except sqlite3.Error as err:
            print(err)
            print("Error occured at line 548 inside CheckingTeamNameExist()")
        except BaseException as err:
            print(err)
            print("Error occurred at line 551 inside CheckingTeamNameExist()")

        for i in range(len(existingTeamTemp)):
            teamNameDataBeforeSearch.append(existingTeamTemp[i][0])
        # ========end of Checking team Name Query====================
        try:
            if self.teamNameVar in teamNameDataBeforeSearch:
                QMessageBox.warning(self, "Warning", "Team Name already Exists\nPlease Change Your Team Name")
                try:
                    test, ok = QInputDialog.getText(self, "Team Name Change", "Enter New Team Name : ")

                    if ok:
                        self.teamNameVar = str(test)
                        self.CheckingTeamNameExist()
                        self.teamNameBox.setText(self.teamNameVar)
                except BaseException as err:
                    print("Error occurred at line 568")
                    print(err)
        except BaseException as err:
            print("Error occurred at line 568")
            print(err)


    def updatingDatabaseAfterSave(self):
        try:
            saveSelectQuery = "create table '%s' (name varchar(20),players varchar(20),value int(20));" % (
                self.teamNameVar)
            self.mycursor.execute(saveSelectQuery)

            saveInsertQuery = "insert into '%s' (name,players,value) values(?,?,?)" % (self.teamNameVar)
            self.mycursor.executemany(saveInsertQuery, (self.fetchData))
            self.mydb.commit()
            QMessageBox.information(self, 'Information', "Team has been saved")


        except sqlite3.Error as err:
            print("Error occured in line 310 by saveTeamAction function")
            print(err)
            self.mydb.rollback()


    def teamInDatabase(self):
        try:
            self.mydb = sqlite3.connect("player.db")
            self.mycursor = self.mydb.cursor()
            self.teamResult = self.mycursor.execute(
                "select name from sqlite_master where type = 'table' and name not like 'match%' and name not like 'stats%';").fetchall()
        except sqlite3.Error as err:
            print("Error occured at line 649 inside teamInDatabase function ")
            print(err)

    def updatingTotalVariable(self):
        pass

