import requests
from bs4 import BeautifulSoup
import time

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

def Scraper(teams: tuple) -> dict:
    """Scrape statistics from the desired teams and year dates"""
    data = dict()
    for team in teams:
        time.sleep(30)
        data[team] = dict()
        request = requests.get(f"https://www.basketball-reference.com/teams/{team}/")
        soup = Table_rows(BeautifulSoup(request.text, 'html.parser'))
        for row in soup[1:]:
            data[team][Season_year(row)] = dict()
            for cell in Table_cells(row):
                name = cell["data-stat"]
                if name not in {"DUMMY", "lg_id", "coaches", "top_ws", "rank_team_playoffs", "team_name"}:
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

def Sort_by_stats(teams: dict[str, dict[str, dict[str, int]]], stats: str) -> list[tuple[int, str, str]]:
    """Returns list of sorted statistic type"""
    scores: list[tuple[int, str, str]] = []
    for team, team_val in teams.items():
        for year, year_val in team_val.items():
            scores.append((int(year_val[stats]), year, team))
    return sorted(scores)[::-1]

def Float_Zero(value):
    """Float conversion with error handling"""
    try:
        return float(value)
    except:
        return 0.0

def Sort_by_dominance(teams: dict[str, dict[str, dict[str, int]]]) -> list[tuple[int, str, str]]:
    """Sorts teams by my terms of dominance"""
    scores: list[tuple[int, str, str]] = []
    for team, team_val in teams.items():
        for year, year_val in team_val.items():
            scores.append(((10 * Float_Zero(year_val["win_loss_pct"]) + (Float_Zero(year_val["off_rtg_rel"]) / 100) + (Float_Zero(year_val["def_rtg_rel"]) / -100)), year, team))
    return sorted(scores)[::-1]

def Count_occurence(data: list[tuple]) -> dict:
    """Counts how many times a number is listed in given list"""
    count = {}
    for i in data:
        wins = i[0]
        if wins in count:
            count[wins] += 1
        else:
            count[wins] = 1
    return count