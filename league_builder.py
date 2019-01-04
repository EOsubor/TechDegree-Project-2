import csv
import datetime

# empty lists & dictionary to sort players.
experienced = []
inexperienced = []
teams = {}


def read_and_sort():
    # create function to read file and extract information
    with open("soccer_players.csv", newline = '') as csvfile:
        rosterreader = csv.DictReader(csvfile, delimiter = ',')
        # create group list of rows.
        rows = list(rosterreader)

        # iterate through rows and assign players to experienced or inexperienced list.
        for row in rows:
            #print(row) - tester code line (to check output is correct)
            if row['Soccer Experience'] == "YES":
                #print(row['Name']) - tester code line (to check output is correct)
                #create tuple of list of tuple for individual player info.
                experienced.append(tuple([row['Name'], row['Soccer Experience'], row['Guardian Name(s)']]))
            else:
                inexperienced.append(tuple([row['Name'], row['Soccer Experience'], row['Guardian Name(s)']]))
        #print(experienced) - tester code (to check output is correct)


# Create function to iterate over both lists and divide into 3 equal groups.
def team_roster(iter1, iter2):
    # Automatic index (Assuming both lists are the same length)
    third = len(iter1)//3
    sixth = (2*len(iter1))//3

    # Set dictionary key to slices of iterable.
    teams["Dragons"] = iter1[:third] + iter2[:third]
    teams["Sharks"] = iter1[third:sixth] + iter2[third:sixth]
    teams["Raptors"] = iter1[sixth:] + iter2[sixth:]
    return teams
    # print(teams) - tester code (to check output is correct)


# Create function to return required player information.
def print_team(team):
    result = ""
    # Loop through each tuple containing all player info and concatenate required info.
    for player in team:
        result += "Name: " + player[0] + "  Soccer Experience: " +  player[1] + "  Guardian(s): " + player[2] + "\n\n"
    return result


# Create function to write all player information to text file for specified team.
def write_to_file(team_name):
    # Use 'with' command to save writing a seperate command to close file.
    with open("teams.txt", "a") as file:
        file.write(f"\n\n\t\t\t\t\t ********* {team_name} *********\n\n")
        # Use 'get' method to pull values of given key. In this case, team roster information.
        file.write(print_team(teams.get(team_name)))


# Create function to write a letter to all guardians in specified team.
def write_letter():
    # Loop through key, values using 'items()' method.
    for name, team in teams.items():
        # Loop through and access individual player info stored in values.
        for player in team:
            # Create template for data retrieved from looping to be stored. Write letter.
            with open("{}.txt".format(player[0]), "a") as file:
                file.write(f"""Dear {player[2]},\n
   {player[0][1]} has been drafted into the {name} team for this year’s Youth Soccer League.
   First practice will be on {now.strftime("%Y-%m-%d %H:%M")}.\n
   See you all there!"""
)


# Use Dunder main to prevent code from running as an import.
if __name__ == '__main__':
    read_and_sort()
    team_roster(experienced, inexperienced)
    write_to_file("Dragons")
    write_to_file("Sharks")
    write_to_file("Raptors")
    write_letter()
