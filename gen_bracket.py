import database
import math
team_dict = database.import_dataset(r'C:\Users\Bryan\Downloads\summary25.csv')
def odds_of_winning(team1, team2):
    points_diff = ((team_dict[team1].adj_tempo - team_dict[team2].adj_tempo) * (team_dict[team1].adj_em - team_dict[team2].adj_em))/200
    cdf = 0.5 * (1 + math.erf(-2.24)/(11*math.sqrt(2)))
class Team:
    def __init__(self, name):
        self.name = name

class Matchup:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.winner = None

    def play_match(self):
        # Placeholder for match logic, randomly select a winner for now
        import random

        self.winner = random.choice([self.team1, self.team2])
        return self.winner

class Bracket:
    def __init__(self, teams):
        self.teams = teams
        self.rounds = []

    def generate_bracket(self):
        current_round = [Matchup(self.teams[i], self.teams[i+1]) for i in range(0, len(self.teams), 2)]
        self.rounds.append(current_round)

        while len(current_round) > 1:
            next_round = []
            for matchup in current_round:
                winner = matchup.play_match()
                next_round.append(winner)
            current_round = [Matchup(next_round[i], next_round[i+1]) for i in range(0, len(next_round), 2)]
            self.rounds.append(current_round)

    def display_bracket(self):
        for i, round in enumerate(self.rounds):
            print(f"Round {i+1}:")
            for matchup in round:
                print(f"{matchup.team1.name} vs {matchup.team2.name} - Winner: {matchup.winner.name if matchup.winner else 'TBD'}")
            print()

def run_bracket(dataset):
    teams = [Team(f"{database.team_names[i]} {i+1}") for i in range(64)]
    bracket = Bracket(teams)
    bracket.generate_bracket()
    bracket.display_bracket()
    