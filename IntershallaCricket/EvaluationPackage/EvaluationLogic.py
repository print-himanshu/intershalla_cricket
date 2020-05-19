# This module is created for find the man of the match

def batting(run,noOf4,noOf6,balls,field):
    point = 0

    #point scored by half century and century
    if run >=100:
        point +=10
    if run>=50 :
        point +=5

    if balls !=0:
        #point scored by strike rate
        strikeRate= (run/balls)*100

        if strikeRate>=80 and strikeRate<=100:
            point +=2
        if strikeRate>100:
            point +=4

        # for hanling point scored by fours
        point +=noOf4
        # for handling point scored by six
        point += noOf6*2


    # for handling 1 point for 2 run scored
    #modifiedRun = run - (noOf4 * 4) - (noOf6 *6)
    #point +=modifiedRun//2
        point +=run//2

    #for fielding
    point+=field*10
    return point


def bowling(wkts,overs,run):
    point = 0

    point +=wkts*10

    # additional for three wicket
    if wkts >=3:
        point +=5
    #additional for 5 wicket
    if wkts>=5:
        point+=10
    if overs !=0:
        economyRate = (run/overs)

        #economy rate calculation
        if economyRate>=3.5 and economyRate <=4.5:
            point+=4
        elif economyRate>=2 and economyRate<3.5:
            point+=7
        elif economyRate<2:
            point+=10


    return point
















