import sqlite3
from IntershallaCricket.EvaluationPackage import EvaluationLogic

class MatchData:
    count = 0
    def __init__(self):
        self.run = 0
        self.noOf4 = 0
        self.noOf6 = 0
        self.field = 0
        self.balls = 0
        self.wkts = 0
        self.overs = 0
        self.point = 0
        self.mydb = None
        self.mycursor = None

    def initialization(self):
        #Variable for batting Evaluation--------------------------
        self.run = 0    #for run index of tuple is 1
        self.noOf4 = 0  #for noOf4 index of tuple is 3
        self.noOf6 = 0  #for noOf6 index of tuple is 4

        #for fielding  runout + catches
        #for runout index of tuple is 11
        #for catches index of tuple is 9
        #for stumping index of tuple is 10
        self.field = 0
        self.balls = 0 # for balls index of tuplie is 2
        #-----------------------------------------------------------
        # Variable for Bowling Evaluation-----------------------
        self.wkts =0  #for wkts index of tuple is 8
        #First given bowl to over
        #Index of bowled in tuple is 5
        self.overs =0
        self.runGiven =0 #index for runGiven is 7
        #-----------------------------------------------------------
        
        self.mydb = sqlite3.connect("player.db")
        self.mycursor = self.mydb.cursor()

        self.point = 0


    def calculatingMOM(self,currentMatch,playerName):#(MOM : Man of the Match)
        try:
            #finding count
            #countQuery = """select count(player) from match;"""
            #temp = self.mycursor.execute(countQuery).fetchone()
            #MatchData.count = temp[0]

            #fetching Data
            fetchData = self.mycursor.execute("select * from '%s' where player like '%s'"%(currentMatch,playerName)).fetchone()


            #evaluating score
            self.point = 0

            self.run = fetchData[1]
            self.noOf4 = fetchData[3]
            self.noOf6 = fetchData[4]
            self.field = fetchData[11]+ fetchData[9]+fetchData[10]
            self.balls = fetchData[2]
            self.point=EvaluationLogic.batting(self.run,
                                        self.noOf4,
                                        self.noOf6,
                                        self.balls,
                                        self.field)
            self.wkts = fetchData[8]
            self.overs = fetchData[5]/6
            self.runGiven = fetchData[7]
            self.point +=EvaluationLogic.bowling(self.wkts,
                                        self.overs,
                                        self.runGiven
                                        )

            return self.point

        except sqlite3.Error as err:
                print("Error has occured : ",err)
        finally:
                self.mycursor.close()
                self.mydb.close()





