import csv

experienced = []
inexperienced = []
teams = {}


def read_and_sort():
    with open("soccer_players.csv", newline = '') as csvfile:
        rosterreader = csv.DictReader(csvfile, delimiter = ',')
        rows = list(rosterreader)
        
        for row in rows:
            #print(row)
            if row['Soccer Experience'] == "YES":
                #print(row[0]), #code tester line
                experienced.append(tuple([row['Name'], row['Soccer Experience'], row['Guardian Name(s)']]))
            else:
                inexperienced.append(tuple([row['Name'], row['Soccer Experience'], row['Guardian Name(s)']]))
        #print(experienced)
        

            
def team_roster(iter1, iter2):
    third = len(iter1)//3 
    sixth = (2*len(iter1))//3
    
    teams["Dragons"] = iter1[:third] + iter2[:third]
    teams["Sharks"] = iter1[third:sixth] + iter2[third:sixth]
    teams["Raptors"] = iter1[sixth:] + iter2[sixth:]
    
    print(teams)

            
def print_team(team):
    result = ""
    for player in team: 
        result += "Name: " + player[0] + "  Soccer Experience: " +  player[1] + "  Guardian(s): " + player[2] + "\n\n"
    return result


def write_to_file(team_name):
    with open("teams.txt", "a") as file:
        file.write(f"\n\n\t\t\t\t\t ********* {team_name} *********\n\n")
        file.write(print_team(teams.get(team_name)))




if __name__ == '__main__':
    read_and_sort()
    team_roster(experienced, inexperienced)
    write_to_file("Dragons")
    #write_to_file("Sharks")
    #write_to_file("Raptors")
    

