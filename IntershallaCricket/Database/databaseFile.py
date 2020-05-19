import sqlite3

class databaseEntry:
    def __init__(self):
        self.mydb = sqlite3.connect("player.db")

        self.mycursor = self.mydb.cursor()

        self.matchCreateQuery = """create table match(player varchar(20) primary key,
                                         scored int(20),
                                         faced int(20),
                                         fours int(20),
                                         sixes int(20),
                                         bowled int(20),
                                         maiden int(20),
                                         given int(20),
                                         wkts int(20),
                                         catches int(20),
                                         stumping int(20),
                                         ro int(20)
                                         );"""


        self.statsCreateQuery = """ create table stats(player varchar(20) primary key,
                                          value int(20) ,
                                          matches int(20),
                                          runs int(20),
                                          _100s int(20),
                                          _50s int(20),
                                          ctg varchar(20),
                                          foreign key(value) references match(player));"""

        self.matchDataList =[
            ["Kohli"       ,102 ,98 ,8 ,2 ,0  ,0 ,0  ,0 ,0  ,0 ,1],
            ["Yuvraj"       ,12  ,20 ,1 ,0 ,48 ,0 ,36 ,1 ,0  ,0 ,0],
            ["Rahane"       ,49  ,75 ,3 ,0 ,0  ,0 ,0  ,0 ,1  ,0 ,0],
            ["Dhawan"       ,32  ,35 ,4 ,0 ,0  ,0 ,0  ,0 ,0  ,0 ,0 ],
            ["Dhoni"        ,56  ,45 ,3 ,1 ,0  ,0 ,0  ,0 ,3  ,2 ,0],
            ["Axar"         ,8   ,4  ,2 ,0 ,48 ,2 ,35 ,1 ,0  ,0 ,0],
            ["Pandya"       ,42  ,36 ,3 ,3 ,30 ,0 ,25 ,0 ,1  ,0 ,0],
            ["Jadega"       ,18  ,10 ,1 ,1 ,60 ,3 ,50 ,2 ,1  ,0 ,1],
            ["Kedar"        ,65  ,60 ,7 ,0 ,24 ,0 ,24 ,0 ,0  ,0 ,0],
            ["Ashwin"       ,23  ,42 ,3 ,0 ,60 ,2 ,45 ,6 ,0  ,0 ,0],
            ["Umesh"        ,0   ,0  ,0 ,0 ,54 ,0 ,50 ,4 ,1  ,0 ,0],
            ["Bumrah"       ,0   ,0  ,0 ,0 ,60 ,2 ,49 ,1 ,0  ,0 ,0],
            ["Bhuwaneshwar",15   ,12 ,2 ,0 ,60 ,1 ,46 ,2 ,0  ,0 ,0],
            ["Rohit"       ,46   ,65 ,5 ,1 ,0  ,0 ,0  ,0 ,1  ,0 ,0],
            ["Kartik"      ,29   ,42 ,3 ,0 ,0  ,0 ,0  ,0 ,2  ,0 ,1]]

        self.statsDataList=[
            ["Kohli"       ,120 ,189 ,8257 ,28   ,43,"BAT"],
            ["Yuvraj"       ,100 ,86  ,3589 ,10   ,21,"BAT"],
            ["Rahane"       ,100 ,158 ,5435 ,11   ,31,"BAT"],
            ["Dhawan"       ,85  ,25  ,565  ,2    ,1,"AR"],
            ["Dhoni"        ,75  ,78  ,2573 ,3    ,19,"BAT"],
            ["Axar"         ,100 ,67  ,208  ,0    ,0,"BWL"],
            ["Pandya"       ,75  ,70  ,77   ,0    ,0,"BWL"],
            ["Jadega"       ,85  ,16  ,1    ,0    ,0,"BWL"],
            ["Kedar"        ,90  ,111 ,675  ,0    ,1,"BWL"],
            ["Ashwin"       ,100 ,136 ,1914 ,0    ,10,"AR"],
            ["Umesh"        ,110 ,296 ,9496 ,10   ,64,"WK"],
            ["Bumrah"       ,60  ,73  ,1365 ,0    ,8,"WK"],
            ["Bhuwaneshwar" ,75  ,17  ,289  ,0    ,2,"AR"],
            ["Rohit"        ,85  ,304 ,8701 ,14   ,52,"BAT"],
            ["Kartik"       ,75  ,11  ,111  ,0    ,0,"AR"]]

        self.matchInsertQuery = """ insert into match(player,scored, faced,
                                         fours,sixes, bowled,
                                         maiden, given, wkts,
                                         catches,stumping,ro)
                                    values(?,?,?,
                                           ?,?,?,
                                           ?,?,?,
                                           ?,?,?);"""

        self.statsInsertQuery = """insert into stats(player, value, matches,
                                        runs,_100s,_50s, ctg)
                                  values(?,?,?,
                                         ?,?,?,?);"""
        self.executeMain()

    
    def executeMain(self):
        try:
            self.mycursor.execute(self.matchCreateQuery)
            self.mycursor.execute(self.statsCreateQuery)

            self.mycursor.executemany(self.matchInsertQuery,self.matchDataList)
            self.mydb.commit()
            self.mycursor.executemany(self.statsInsertQuery,self.statsDataList)
            print("Table Created")
            self.mydb.commit()
        
        except sqlite3.Error as er:
            print(er)
            self.mydb.rollback()
        finally:
            self.mycursor.close()
            self.mydb.close()



