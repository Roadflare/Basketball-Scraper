import requests
from bs4 import BeautifulSoup
import json

ALL_TEAMS = ("ATL", "BOS", "NJN", "CHA", "CHI", "CLE", "DAL", "DEN", "DET", "GSW", 
"HOU", "IND", "LAC", "LAL", "MEM", "MIA", "MIL", "MIN", "NOH", "NYK", "OKC", 
"ORL", "PHI", "PHO", "POR", "SAC", "SAS", "TOR", "UTA", "WAS")


def User_input() -> tuple[tuple, tuple]:
    """Input function to pick teams and/or start/end year"""
    team, year = [], ()
    teams_str = "\n".join([f"{ALL_TEAMS.index(x)}: {x}" for x in ALL_TEAMS])
    print("Select numbers from the teams to scrape. Leave empty for all. Space separated!")
    print(teams_str)
    select = input()
    year = (input("Start year: \n"), input("End year: \n"))
    if select:
        for item in select.split():
            team.append(ALL_TEAMS[int(item)])
    else:
        team = ALL_TEAMS
    team = tuple(team)
    return team, year

def Scraper(x: tuple[tuple]) -> dict:
    """Scrape statistics from the desired teams and year dates"""
    teams = x[0]
    data = dict()
    for team in teams:
        data[team] = dict()
        request = requests.get(f"https://www.basketball-reference.com/teams/{team}/")
        soup = Table_rows(BeautifulSoup(request.text, 'html.parser'))
        for row in soup[1:]:
            data[team][Season_year(row)] = dict()
            for cell in Table_cells(row):
                name = cell["data-stat"]
                if name not in {"DUMMY", "lg_id", "coaches", "top_ws", "rank_team_playoffs"}:
                    data[team][Season_year(row)][name] = cell.text
    return data

def Table_rows(soup: str) -> list:
    """Takes HTML5 and returns table rows"""
    return soup.find("table").find_all("tr")

def Table_cells(row):
    """Returns all tables cell from given row"""
    return row.find_all("td")

def Season_year(row):
    """Returns the year of the season"""
    return row.find_all("th")[0].text