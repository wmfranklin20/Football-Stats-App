import requests
from bs4 import BeautifulSoup
import re
import selenium
import pprint

#Function to pull specified url. Takes a url as arg in string format, returns the html of the url.
def teamPull (url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    #Basic stats for all PL Sides
    regularSeasonTable = soup.find(id="switcher_results2023-202491")
    squadStandardStatsTable = soup.find(id="switcher_stats_squads_standard")
    squadShootingTable = soup.find(id="switcher_stats_squads_shooting")
    squadPassingTable = soup.find(id="switcher_stats_squads_passing")
    squadPassingTypesTable = soup.find(id="switcher_stats_squads_passing_types")
    squadGCATable = soup.find(id="switcher_stats_squads_gca")
    squadDefensiveActionsTable = soup.find(id="switcher_stats_squads_defense")
    squadPosessionTable = soup.find(id="switcher_stats_squads_possession")

    resultsRows = regularSeasonTable.findAll("tr")
    return(resultsRows)


def tablePull (soup):
    soup.find("")

PremierLeague = "https://fbref.com/en/comps/9/Premier-League-Stats"


table = teamPull(PremierLeague)

for row in table:
    print(row.text.strip())