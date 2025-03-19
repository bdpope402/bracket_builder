import database
import math
import random
team_dict = database.import_dataset(r'C:\Users\Bryan\Downloads\summary25.csv')
def odds_of_winning(team1, team2):
    '''Calculate the odds of team1 winning against team2'''
    points_diff = ((team_dict[team1.name].adj_tempo + team_dict[team2.name].adj_tempo) * (team_dict[team1.name].adj_em - team_dict[team2.name].adj_em))/200
    points_diff = round(points_diff, 2)
    cdf = 0.5 * (1 + math.erf((points_diff-2.24)/(11*math.sqrt(2))))
    percentage = round(cdf * 100, 2)
    return( [points_diff, percentage])

class Team:
    def __init__(self, name):
        self.name = name

class Matchup:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.predicted_winner = None
        self.predicted_win_percentage = None
        self.point_diff = None
        self.winner = None

    def play_match(self):
        odds = odds_of_winning(self.team1, self.team2)
        t1_perc = odds[1]
        t2_perc = 100 - t1_perc
        if (t1_perc >= t2_perc):
            self.predicted_winner = self.team1.name
            self.predicted_win_percentage = t1_perc
        else:
            self.predicted_winner = self.team2.name
            self.predicted_win_percentage = t2_perc
        self.point_diff = abs(odds[0])
        self.winner = random.choices(
            [self.team1, self.team2],
            weights=[t1_perc, t2_perc],
            k=1
            )[0]
        return self.winner

class Bracket:
    def __init__(self, teams):
        self.teams = teams
        self.rounds = []

    def generate_bracket(self):
        current_round = [Matchup(self.teams[i], self.teams[i+1]) for i in range(0, len(self.teams), 2)]
        self.rounds.append(current_round)

        while len(current_round) > 0:
            next_round = []
            for matchup in current_round:
                winner = matchup.play_match()
                next_round.append(winner)
            if len(next_round) != 1:
                current_round = [Matchup(next_round[i], next_round[i+1]) for i in range(0, len(next_round), 2)]
                self.rounds.append(current_round)
            else:
                self.rounds.append(current_round)
                break
            

    def display_bracket(self):
        for i, round in enumerate(self.rounds):
            print("--------------------------------")
            print(f"Round {i+1}:")
            print("--------------------------------")
            if(i == len(self.rounds) - 1):
                print(f"{round[0].winner.name} won it all!")
                print()
            else:
                for matchup in round:
                    print(f"{matchup.team1.name} vs {matchup.team2.name}")
                    print(f"{matchup.predicted_winner} is favored to win with a {matchup.predicted_win_percentage:.2f}% chance and is expected to win by {matchup.point_diff} points.")
                    print(f"- Winner: {matchup.winner.name if matchup.winner else 'TBD'} {"(Roll Clones!)" if matchup.winner.name == "Iowa St." else "" }")
                    print()

if __name__ == "__main__":
    teams = [Team(f"{database.team_names[i]}") for i in range(64)]
    bracket = Bracket(teams)
    bracket.generate_bracket()
    bracket.display_bracket()
    