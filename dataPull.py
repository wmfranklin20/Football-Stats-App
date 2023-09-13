import requests
from bs4 import BeautifulSoup
import re
import selenium
import pprint

#--- Initial page and table function ---#

### Function to pull specified url. Takes a url as arg in string format, returns the html of the url. ###
def pagePull():
    url = "https://fbref.com/en/comps/9/Premier-League-Stats"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return(soup)
soup = pagePull()

### Takes table id text and returns table element ###
def pullTable(div):
    table = soup.find(id=div)
    return(table)

### Takes a single row from table and parses data out into seperate list items to be called ###
def rowData(table, row):
    rows = []
    for data in table[row]:
        rows.append(data.text.strip())
    return(rows)


#--- Individual Table Pulls ---#

### Regular Season Stats Table ###
regSeasonTableID = "switcher_results2023-202491"
regSeasonTable = pullTable(regSeasonTableID)
regSeasonTable_Rows = regSeasonTable.find_all("tr")

### Squad Standard Stats Table ###
squadStandardStatsTableID = "switcher_stats_squads_standard"
squadStandardStatsTable = pullTable(squadStandardStatsTableID)
squadStandardStatsTable_Rows = squadStandardStatsTable.find_all("tr")

test = rowData(squadStandardStatsTable_Rows, 2)
print(test)

squadShootingTable = "switcher_stats_squads_shooting"
squadPassingTable = "switcher_stats_squads_passing"
squadPassingTypesTable = "switcher_stats_squads_passing_types"
squadGCATable = "switcher_stats_squads_gca"
squadDefensiveActionsTable = "switcher_stats_squads_defense"
squadPosessionTable = "switcher_stats_squads_possession"

#--- Data formatting and structuring ---#

### Takes a team and data set to pass to the team object !!!NOT COMPATIBLE WITH ALL TABLES!!! ###
def squadSSTGen(team, data):
    team.players_used = data[1]
    team.avg_age = data[2]
    team.avg_possession = data[3]

    team.goals = data[8]
    team.assists = data[9]
    team.goals_assists = int(team.goals) + int(team.assists)
    team.pk_goals = data[12]
    team.npk_goals = int(team.goals) - int(team.pk_goals)
    team.pk_attempts = data[13]
    team.yellows = data[14]
    team.reds = data[15]

    team.xG = data[16]
    team.npxG = data[17]
    team.xAG = data[18]
    team.npxG_xAG = float(team.npxG) + float(team.xAG)

    team.prgC = data[20]
    team.prgP = data[21]

    team.xG_G_delta = round(float(team.goals) - float(team.xG), 2)


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


        self.xG_G_delta = 0

#--- Team object generation and casting ---#

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

arsenalData = rowData(squadStandardStatsTable_Rows, 2)
squadSSTGen(Arsenal, arsenalData)

astonVillaData = rowData(squadStandardStatsTable_Rows, 3)
squadSSTGen(AstonVilla, astonVillaData)

bournemouthData = rowData(squadStandardStatsTable_Rows, 4)
squadSSTGen(Bournemouth, bournemouthData)

chelseaData = rowData(squadStandardStatsTable_Rows, 8)
squadSSTGen(Chelsea, chelseaData)

manCityData = rowData(squadStandardStatsTable_Rows, 14)
squadSSTGen(ManchesterCity, manCityData)

newcastleData = rowData(squadStandardStatsTable_Rows, 16)
squadSSTGen(NewcastleUnited, newcastleData)


### Testing ###

def testPrint(team):
    print(team.team_name, 
          team.team_abv, 
          team.players_used,
          team.avg_age, 
          team.avg_possession,
          team.goals,
          team.assists,
          team.goals_assists,
          team.pk_goals,
          team.pk_attempts,
          team.yellows,
          team.reds
          )

testPrint(Arsenal)
testPrint(AstonVilla)
testPrint(Bournemouth)
testPrint(Chelsea)
testPrint(ManchesterCity)
testPrint(NewcastleUnited)
print(' ')
list = [Arsenal, AstonVilla, Bournemouth, Chelsea, ManchesterCity, NewcastleUnited]
for team in list:
    print(str(team.team_name) + ": " + str(team.avg_possession) + "% " + str(team.goals) + ' goals ' + str(team.xG) + ' xG (' + str(team.xG_G_delta) + ') delta')