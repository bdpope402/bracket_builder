import database
from gen_bracket import team_names, Team, Bracket

def main():
    team_dict = database.import_dataset(r'C:\Users\Bryan\Downloads\summary25.csv')
    teams = [Team(f"{team_names[i]} {i+1}") for i in range(64)]
    bracket = Bracket(teams)
    bracket.generate_bracket()
    bracket.display_bracket()

if __name__ == "__main__":
    main()