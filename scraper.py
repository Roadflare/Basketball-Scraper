import requests

teams = ("ATL", "BOS", "NJN", "CHA", "CHI", "CLE", "DAL", "DEN", "DET", "GSW", 
"HOU", "IND", "LAC", "LAL", "MEM", "MIA", "MIL", "MIN", "NOH", "NYK", "OKC", 
"ORL", "PHI", "PHO", "POR", "SAC", "SAS", "TOR", "UTA", "WAS")


def Input() -> list:
    """Input function to pick teams and/or start/end year"""
    team, year = [], ()
    teams_str = "\n".join([f"{teams.index(x)}: {x}" for x in teams])
    print("Select numbers from the teams to scrape. Type None to skip. Space seperated!")    
    print(teams_str)
    select = input()
    year = (input("Start year: \n"), input("End year: \n"))
    team = team.append()
    return team, year

def Scraper(team=teams: tuple[str], year=(1980, 2024): tuple[int, int]) -> int:
    """Scrape statistics from the desired teams and year dates"""
    for team in team:
        for year in range(year[0], year[1]):
    return 0