import csv

experienced = []
inexperienced = []
teams = {}


def read_and_sort():
    with open("soccer_players.csv",'r') as csvfile: #newline = '',) as csvfile:
        rosterreader = csv.DictReader(csvfile, delimiter = ',')
        rows = list(rosterreader)
        
        for row in rows:
            #print(row)
            if row['Soccer Experience'] == "YES":
                #print(row[0]), #code tester line
                experienced.append(row['Name'])
            else:
                inexperienced.append(row['Name'])
        #inexperienced.remove('Name')
        #print(experienced)
        #print(inexperienced)
            #print(row["Name"])

            
def team_roster(iter1, iter2):
    #for index, player in enumerate(experienced):
        #if index in [0, 2, 4]:
            #dragons.append(player)
    third = len(iter1)//3 
    sixth = (2*len(iter1))//3
    
    teams["Dragons"] = iter1[:third] + iter2[:third]
    teams["Sharks"] = iter1[third:sixth] + iter2[third:sixth]
    teams["Raptors"] = iter1[sixth:] + iter2[sixth:]
    
    print(teams)

            
def print_team(team):
    result = ""
    for player in team: 
        result += "\n\nName: \n" + player 
                  #"Soccer Experience: " + player[2] + 
                  #"Parents: " + player[3] + "\n"
    return result


def write_to_file(team):
    with open("teams.txt", "w") as file:
        file.write("*********", team, "*********\n")
        file.write(print_team(teams.get(team)))
    
    
def write():
    with open('teams1.txt', 'w') as csvfile:
        fieldnames = teams.keys()
        teamswriter = csv.DictWriter(csvfile, fieldnames = fieldnames)
        
        teamswriter.writeheader()
        teamswriter.writerow(teams)




if __name__ == '__main__':
    read_and_sort()
    team_roster(experienced, inexperienced)
    write_to_file("Sharks")
    
    

