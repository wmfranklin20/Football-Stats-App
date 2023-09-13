import requests
from bs4 import BeautifulSoup
import re
import selenium
import pprint

#Function to pull specified url. Takes a url as arg in string format, returns the html of the url.
def pagePull():
    url = "https://fbref.com/en/comps/9/Premier-League-Stats"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return(soup)
soup = pagePull()

def pullTable(div):
    table = soup.find(id=div)
    return(table)

regSeasonTableID = "switcher_results2023-202491"
regSeasonTable = pullTable(regSeasonTableID)
regSeasonTable_Rows = regSeasonTable.find_all("tr")
#for row in regSeasonTable_Rows:
#    print(row.text.strip())

squadStandardStatsTableID = "switcher_stats_squads_standard"
squadStandardStatsTable = pullTable(squadStandardStatsTableID)
squadStandardStatsTable_Rows = squadStandardStatsTable.find_all("tr")

### Takes a single row from table and parses data out into seperate list items to be called ###
def rowData(table, row):
    rows = []
    for data in table[row]:
        rows.append(data.text.strip())
    return(rows)
test = rowData(squadStandardStatsTable_Rows, 2)
print(test)



### Takes a team and data set to pass to the team object !!!NOT COMPATIBLE!!! ###
def squadSSTGen(team, data):
    team.players_used = data[1]
    team.avg_age = data[2]
    team.avg_possession = data[3]



def teamPull ():
    url = "https://fbref.com/en/comps/9/Premier-League-Stats"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')


    #Basic stats for all PL Sides
    """
    Stats to Pull:
        - Matches Played (MP)
        - Wins (W)
        - Draws (D)
        - Losses (L)
        - Goals For (GF)
        - Goals Against (GA)
        - Goal Difference (GD)
        - Points (Pts)
        - Points per Match (Pts/MP)
        - Expected Goals For (xGF)
        - Expected Goals Against (xGA)
        - Expected Goal Difference (xGD)
    """
    squadStandardStatsTable = soup.find(id="switcher_stats_squads_standard")
    """
    Stats to Pull:
        - Number of Players Used (#Pl)
        - Average Age of Players Used (Age)
        - Average Possession (Poss)
        - Matches Played (MP)
        - Assists (Ast)
        - Goals + Assists (G+A)
        - Penalty Kick Goals (PK)
        - Goals - Penalty Goals (G-PK)
        - Penalty Attempts (PKAtt)
        - Yellow Cards (CrdY)
        - Red Cards (CrdR)
        - Non-Penalty Expected Goals (NPxG)
        - Expected Assisted Goals (xAG)
        - Non-Penalty xG + xAG (NPxG + xAG)
        - Progressive Carries (PrgC)
        - Progressive Passes (PrgP)
    """
    squadShootingTable = soup.find(id="switcher_stats_squads_shooting")
    squadPassingTable = soup.find(id="switcher_stats_squads_passing")
    squadPassingTypesTable = soup.find(id="switcher_stats_squads_passing_types")
    squadGCATable = soup.find(id="switcher_stats_squads_gca")
    squadDefensiveActionsTable = soup.find(id="switcher_stats_squads_defense")
    squadPosessionTable = soup.find(id="switcher_stats_squads_possession")

    resultsRows = squadStandardStatsTable.findAll("tr")
    return(resultsRows)


class Team:
    def __init__(self, team_name, team_abv):
        self.team_name = team_name
        self.team_abv = team_abv

        #Stats pulled from 'Squad Standard Stats' table
        self.players_used = 0
        self.avg_age = 0
        self.avg_possession = 0

        self.goals = 0
        self.assists = 0
        self.goals_assists = self.goals + self.assists
        self.pk_goals = 0
        self.npk_goals = self.goals - self.pk_goals
        self.pk_attempts = 0
        self.yellows = 0
        self.reds = 0

        self.xG = 0
        self.npxG = 0
        self.xAG = 0
        self.npxG_xAG = self.npxG + self.xAG

        self.prgC = 0
        self.prgP = 0


### Generate initial team objects ###
Arsenal = Team("Arsenal", "ARS")
AstonVilla = Team("Aston Villa", "AVL")
Bournemouth = Team("Bournemouth", "BOU")
Brentford = Team("Brentford", "BRE")
Brighton = Team("Brighton", "BRI")
Burnley = Team("Burnley", "BUR")
Chelsea = Team("Chelsea", "CHE")
CrystalPalace = Team("Crystal Palace", "CRY")
Everton = Team("Everton", "EVE")
Fulham = Team("Fulham", "FUL")
Liverpool = Team("Liverpool", "LIV")
LutonTown = Team("Luton Town", "LTN")
ManchesterCity = Team("Manchester City", "MCI")
ManchesterUnited = Team("Manchester United", "MUN")
NewcastleUnited = Team("Newcastle United", "NEW")
NottinghamForrest = Team("Nottingham Forrest", "NFO")
SheffieldUnited = Team("Sheffield United", "SHE")
Tottenham = Team("Tottenham", "TOT")
WestHam = Team("West Ham", "WHU")
Wolves = Team("Wolves", "WOL")

squadSSTGen(Arsenal, test)



### Testing ###

print(Arsenal.team_name, Arsenal.team_abv, Arsenal.avg_age, Arsenal.avg_possession)
print(AstonVilla.team_name)