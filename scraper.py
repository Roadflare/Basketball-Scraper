import requests

all_teams = ("ATL", "BOS", "NJN", "CHA", "CHI", "CLE", "DAL", "DEN", "DET", "GSW", 
"HOU", "IND", "LAC", "LAL", "MEM", "MIA", "MIL", "MIN", "NOH", "NYK", "OKC", 
"ORL", "PHI", "PHO", "POR", "SAC", "SAS", "TOR", "UTA", "WAS")


def User_input() -> tuple[tuple, tuple]:
    """Input function to pick teams and/or start/end year"""
    team, year = [], ()
    teams_str = "\n".join([f"{all_teams.index(x)}: {x}" for x in all_teams])
    print("Select numbers from the teams to scrape. Leave empty for all. Space seperated!")
    print(teams_str)
    select = input()
    year = (input("Start year: \n"), input("End year: \n"))
    if select:
        for item in select.split():
            team.append(all_teams[int(item)])
    else:
        team = all_teams
    team = tuple(team)
    return team, year

def Scraper(teams: tuple[str], year: tuple[int, int]) -> int:
    """Scrape statistics from the desired teams and year dates"""
    for team in teams:
        with open(f"{team}.csv", "w") as file:
            r = requests.get(f"https://www.basketball-reference.com/teams/{team}/")
            file.write(r.text)
    return 0