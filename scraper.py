import requests

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

def Scraper(x: tuple[tuple]) -> int:
    """Scrape statistics from the desired teams and year dates"""
    teams = x[0]
    for team in teams:
        with open(f"{team}.csv", "w") as file:
            r = requests.get(f"https://www.basketball-reference.com/teams/{team}/")
            file.write(r.text)
    return 0