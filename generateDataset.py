import pandas as pd
import numpy as np

finalList=[]
premierLeagueSeasons=["1415","1516","1617","1718","1819"]

def addSeason(seasonName,df):
    for index,row in df.iterrows():
        foundHome=True
        foundAway=True
        for team in finalList:
            if team["TeamName"]==row["HomeTeam"] and team["season"]==season:
                if row["FTHG"]> row["FTAG"]:
                    team["points"]+=3
                    team["TotalWins"]+=1
                    team["TotalDraws"]+=0
                    team["TotalLosses"]+=0
                elif row["FTHG"]== row["FTAG"]:
                    team["points"]+=1
                    team["TotalWins"]+=0
                    team["TotalDraws"]+=1
                    team["TotalLosses"]+=0
                else:
                    team["points"]+=0
                    team["TotalWins"]+=0
                    team["TotalDraws"]+=0
                    team["TotalLosses"]+=1
                # tempDict["season"]="18/19"
                team["GoalsScored"]+=row["FTHG"]
                team["GoalsConceded"]+=row["FTAG"]
                team["GoalDifference"]+=row["FTHG"]-row["FTAG"]
                team["YellowCard"]+=row["HY"]
                team["RedCard"]+=row["HR"]
                team["totalFouls"]+=row["HF"]
                foundHome=False

            elif team["TeamName"]==row["AwayTeam"] and team["season"]==season: 
                if row["FTAG"]> row["FTHG"]:
                    team["points"]+=3
                    team["TotalWins"]+=1
                    team["TotalDraws"]+=0
                    team["TotalLosses"]+=0
                elif row["FTAG"]== row["FTHG"]:
                    team["points"]+=1
                    team["TotalWins"]+=0
                    team["TotalDraws"]+=1
                    team["TotalLosses"]+=0
                else:
                    team["points"]+=0
                    team["TotalWins"]+=0
                    team["TotalDraws"]+=0
                    team["TotalLosses"]+=1
                # tempDict["season"]="18/19"
                team["GoalsScored"]+=row["FTAG"]
                team["GoalsConceded"]+=row["FTHG"]
                team["GoalDifference"]+=row["FTAG"]-row["FTHG"]
                team["YellowCard"]+=row["AY"]
                team["RedCard"]+=row["AR"]
                team["totalFouls"]+=row["AF"]
                foundAway=False

            if foundHome == False and foundAway == False:
                break
        if foundHome: #HomeTeam not found
            tempDict={}
            tempDict["TeamName"]=row["HomeTeam"]
            if row["FTHG"]> row["FTAG"]:
                tempDict["points"]=3
                tempDict["TotalWins"]=1
                tempDict["TotalDraws"]=0
                tempDict["TotalLosses"]=0
            elif row["FTHG"]== row["FTAG"]:
                tempDict["points"]=1
                tempDict["TotalWins"]=0
                tempDict["TotalDraws"]=1
                tempDict["TotalLosses"]=0
            else:
                tempDict["points"]=0
                tempDict["TotalWins"]=0
                tempDict["TotalDraws"]=0
                tempDict["TotalLosses"]=1
            tempDict["season"]=season
            tempDict["GoalsScored"]=row["FTHG"]
            tempDict["GoalsConceded"]=row["FTAG"]
            tempDict["GoalDifference"]=row["FTHG"]-row["FTAG"]
            tempDict["YellowCard"]=row["HY"]
            tempDict["RedCard"]=row["HR"]
            tempDict["totalFouls"]=row["HF"]

            finalList.append(tempDict)

        if foundAway: #AwayTeam not found
            tempDict={}
            tempDict["TeamName"]=row["AwayTeam"]
            if row["FTAG"]> row["FTHG"]:
                tempDict["points"]=3
                tempDict["TotalWins"]=1
                tempDict["TotalDraws"]=0
                tempDict["TotalLosses"]=0
            elif row["FTAG"]== row["FTHG"]:
                tempDict["points"]=1
                tempDict["TotalWins"]=0
                tempDict["TotalDraws"]=1
                tempDict["TotalLosses"]=0
            else:
                tempDict["points"]=0
                tempDict["TotalWins"]=0
                tempDict["TotalDraws"]=0
                tempDict["TotalLosses"]=1
            tempDict["season"]=season
            tempDict["GoalsScored"]=row["FTAG"]
            tempDict["GoalsConceded"]=row["FTHG"]
            tempDict["GoalDifference"]=row["FTAG"]-row["FTHG"]
            tempDict["YellowCard"]=row["AY"]
            tempDict["RedCard"]=row["AR"]
            tempDict["totalFouls"]=row["AF"]

            finalList.append(tempDict)

for season in premierLeagueSeasons:
    df = pd.read_csv("data/laLiga/season-{}.csv".format(season))
    addSeason(season,df)


finalDf = pd.DataFrame(finalList)
finalDf.sort_values(by=['points'],inplace=True,ascending=False)
finalDf.reset_index(drop=True,inplace=True)
finalDf.to_csv("generatedDataset/laLiga.csv")