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

def process_results(rows):
    originalVal = rows
    team_name_dictionary = {}
    counter = 0

    for row in rows:

        teams = originalVal[counter]

        team_name_dictionary[teams[1]] = 0


        counter +=1

    counter = 0
    for row in rows:
        teams = originalVal[counter]


        if teams[5] == "H":
            team_name_dictionary[teams[1]] += 3
        elif teams[5] == "A":
            team_name_dictionary[teams[2]] += 3
        else:
            team_name_dictionary[teams[1]] += 1
            team_name_dictionary[teams[2]] += 1
        counter += 1

        

    teamName = sorted(team_name_dictionary.items(), key=lambda x: x[1], reverse=True)
    print(teamName)






    return teamName



print(f"{'Place':<10} {'Team Name':<20} {'Wins':<10} {'Draws':<10} {'Losses':<10} {'Goal Difference':<20} {'Total Points':<10}")




if __name__ == "__main__":
    file_contents = read_csv(csv_file)
    teamName = process_results(file_contents)


    for key in teamName:
        print(f"{key[0]:>20}{key[1]:>69}")
