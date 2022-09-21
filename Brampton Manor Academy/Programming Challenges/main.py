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
        team_name_dictionary[teams[1]] = None
        counter +=1



    return team_name_dictionary



print(f"{'Place':<10} {'Team Name':<20} {'Wins':<10} {'Draws':<10} {'Losses':<10} {'Goal Difference':<20} {'Total Points':<10}")




if __name__ == "__main__":
    file_contents = read_csv(csv_file)
    teamName = dict(sorted(process_results(file_contents).items()))

    for key in teamName:
        print(key)
    print(file_contents)
    print(process_results(file_contents))