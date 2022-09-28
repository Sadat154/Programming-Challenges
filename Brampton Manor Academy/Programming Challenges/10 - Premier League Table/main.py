import csv
from pathlib import Path

csv_file = Path("Premier 16-17 - Premier 16-17.csv")


def check_file_exists(csv_file):
    return csv_file.is_file()


def read_csv(csv_file):
    csv_contents = []
    if check_file_exists(csv_file):
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            next(reader)  ###   skip first row (header)
            for row in reader:
                csv_contents.append(row)
    return csv_contents

def referree(rows):
    startingVal = rows
    referreeDict = {}

    counter = 0

    for row in rows:
        teams = startingVal[counter]
        referreeDict[teams[6]] = 0

        counter += 1

    counter = 0

    for row in rows:
        teams = startingVal[counter]
        if int(teams[15]) > 0:
            referreeDict[teams[6]] += int(teams[15])
        if int(teams[16]) > 0:
            referreeDict[teams[6]] += int(teams[16])
        if int(teams[17]) > 0:
            referreeDict[teams[6]] += (int(teams[17]) * 3)
        if int(teams[18]) > 0:
            referreeDict[teams[6]] += (int(teams[18]) * 3)
        counter +=1
    listedRefereeNames = sorted(referreeDict.items(), key=lambda x: x[1], reverse=True)
    return listedRefereeNames

def process_results(rows):
    originalVal = rows
    team_name_dictionary = {}

    counter = 0

    for row in rows:
        teams = originalVal[counter]

        team_name_dictionary[teams[1]] = [0,0,0,0,0,0,0,0,0,0,0,0] # 5 = goals scored, 6 = goals conceded, 7 = Total Shot,3 = goal difference, 8 =shots on target, 9 is for shot/on targer

#10 = fouls #11 = fouls per game
        counter += 1



    counter = 0

    for row in rows:
        teams = originalVal[counter]

        if teams[5] == "H": #4 = total points,3 = goal dif, 2 = losses, 1 = draws, 0 = wins
            team_name_dictionary[teams[1]][4] += 3 # adds 3 to total point
            team_name_dictionary[teams[1]][0] += 1 # adds 1 to win
            team_name_dictionary[teams[2]][2] += 1 # adds 1 to loss of away team





        elif teams[5] == "A":
            team_name_dictionary[teams[2]][4] += 3
            team_name_dictionary[teams[2]][0] += 1
            team_name_dictionary[teams[1]][2] += 1




        else:
            team_name_dictionary[teams[1]][4] += 1
            team_name_dictionary[teams[1]][1] += 1


            team_name_dictionary[teams[2]][4] += 1
            team_name_dictionary[teams[2]][1] += 1




        team_name_dictionary[teams[1]][5] += (int(teams[3])) # goals of home team if home team wins
        team_name_dictionary[teams[2]][5] += (int(teams[4])) # goals of away team if home team wins

        team_name_dictionary[teams[1]][6] += int(teams[4]) # goals of home team if away team wins
        team_name_dictionary[teams[2]][6] += int(teams[3]) # goals of away team if away team wins


        team_name_dictionary[teams[1]][7] += int(teams[7]) # Stores shots taken by home tean
        team_name_dictionary[teams[2]][7] += int(teams[8]) # Stores shots taken by away team

        team_name_dictionary[teams[1]][8] += int(teams[9])  # Stores shots on target taken by home team
        team_name_dictionary[teams[2]][8] += int(teams[10])  # Stores shots on target taken by away team
        # 9 is skipped for reason stated above
        team_name_dictionary[teams[1]][10] += int(teams[11])
        team_name_dictionary[teams[2]][10] += int(teams[12])



        counter +=1



    listedTeamNames = sorted(team_name_dictionary.items(), key=lambda x: x[1], reverse=True)
    return(listedTeamNames)





if __name__ == "__main__":
    file_contents = read_csv(csv_file)
    teamName = process_results(file_contents)
    print(f"{'':<10} {'Team Name':<20} {'Wins':<10} {'Draws':<10} {'Losses':<10} {'Goal Difference':<20} {'Total Points':<10}")


    for key in teamName:
        key[1][3] = (key[1][5]-key[1][6]) # Goals Conceded


        print(f"{key[0]:>20}{key[1][0]:>15}{key[1][1]:>11}{key[1][2]:>12}{(key[1][3]):>15}{key[1][4]:>20}")



        key[1][9] = key[1][7] / key[1][8] 
        key[1][11] = key[1][10] / 38

    accurateTeamList = sorted(teamName, key=lambda x: x[1][9], reverse=True)
    foulsTeamList = sorted(teamName, key=lambda x: x[1][11], reverse=True)
    
    #print(teamName[0])
    print("\nSingle Statistics:\n")
    print(f"a. Most accurate team (Total shots on target / total shots) = {accurateTeamList[0][0]}")
    print(f"b. Least accurate team (Total shots on target / total shots) = {accurateTeamList[-1][0]}")
    print(f"c. Dirtiest team (most fouls per game) = {foulsTeamList[0][0]}")
    print(f"d. Cleanest team (least fouls per game) = {foulsTeamList[-1][0]}")
    print(f"e. Referee with highest card average per game (Yellows +1, Red+2) = {referree(read_csv(csv_file))[0][0]}")
    print(f"f. Referee with lowest card average per game (Yellows +1, Red+2) = {referree(read_csv(csv_file))[-1][0]}")
