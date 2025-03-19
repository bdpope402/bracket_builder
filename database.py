import csv
team_names = [
    "Auburn",
    "Alabama St.",
    "Louisville",
    "Creighton",
    "Michigan",
    "UC San Diego",
    "Texas A&M",
    "Yale",
    "Ole Miss",
    "TBD",
    "Iowa St.",
    "Lipscomb",
    "Marquette",
    "New Mexico",
    "Michigan St.",
    "Bryant",
    "Florida",
    "Norfolk St.",
    "UConn",
    "Oklahoma",
    "Memphis",
    "Colorado St.",
    "Maryland",
    "Grand Canyon",
    "Missouri",
    "Drake",
    "Texas Tech",
    "UNC Wilminton",
    "Kansas",
    "Arkansas",
    "St. John's",
    "Omaha",
    "Duke",
    "TBD2",
    "Mississippi St.",
    "Baylor",
    "Oregon",
    "Liberty",
    "Arizona",
    "Akron",
    "BYU",
    "VCU",
    "Wisconsin",
    "Montana",
    "Saint Mary's",
    "Vanderbilt",
    "Alabama",
    "Robert Morris",
    "Houston",
    "SIU Edwardsville",
    "Gonzaga",
    "Georgia",
    "Clemson",
    "McNeese",
    "Purdue",
    "High Point",
    "Illinois",
    "TBD3",
    "Kentucky",
    "Troy",
    "UCLA",
    "Utah St.",
    "Tenessee",
    "Wofford"
]

teamlist = {}
bad_row = "Season, TeamName, Tempo, RankTempo, AdjTempo, RankAdjTempo, OE, RankOE, AdjOE, RankAdjOE, DE, RankDE, AdjDE, RankAdjDE, AdjEM, RankAdjEM"
class team_stat:
    def __init__(self, adj_tempo, adj_of, adj_def, adj_em):
        self.adj_tempo = adj_tempo
        self.adj_off_efficiency = adj_of
        self.adj_def_efficiency = adj_def
        self.adj_em = adj_em

def import_dataset(path):
    with open(path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        first_row = True
        for row in spamreader:
            if( first_row ):
                first_row = False
                continue
            i = 0
            valid = False
            for item in row:
                if( i == 1):
                    team_name = item
                    if(team_name not in team_names):
                        print(f"{team_name} didn't make the tournament (womp womp)")
                        break
                    else:
                        valid = True
                elif( i == 4):
                    adj_tempo = float(item)
                elif( i == 8):
                    adjoe = float(item)
                elif(i == 12):
                    adjde = float(item)
                elif(i == 14):
                    adjem = float(item)
                i = i + 1
            if(valid):
                teamlist[team_name] = team_stat(adj_tempo, adjoe, adjde, adjem )
        return teamlist

if __name__ == "__main__":
    import_dataset(r'C:\Users\Bryan\Downloads\summary25.csv')