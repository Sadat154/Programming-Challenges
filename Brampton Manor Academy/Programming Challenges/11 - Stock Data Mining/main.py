import csv
from pathlib import Path


def read_csv(csv_file):
    csv_contents = []

    with open(csv_file) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        next(reader)  ###   skip first row (header)
        for row in reader:
            csv_contents.append(row)

    return csv_contents

def store_in_storage(sorted_csv_file):

    year_months = []
    container = []
    x = -1
    for i in sorted_csv_file:
        if i[0].split("-")[0:2] not in year_months:
            year_months.append(i[0].split("-")[0:2])
            container.append([0]*3)

            x += 1


        container[x][0] += (float(i[5]) * float(i[6]))
        container[x][1] += int(i[6])
        container[x][2] = (float(container[x][0]) / float(container[x][1]))

        
    list_with_dates = []
    for i in range(len(year_months)):
        list_with_dates.append((year_months[i]) + (container)[i])

        
    return list_with_dates


def calculate_results(list_of_dates):
    top_six = sorted(list_of_dates, key = lambda x:x[4], reverse = True)
    bottom_six = sorted(list_of_dates, key = lambda x:x[4])

    print("The top 6 Year and Month are as follows: ")
    for i in range(6):
        print(f"{i+1}. Year: {top_six[i][0]} Month: {top_six[i][1]} with averages of: {round(top_six[i][4],2)}")

    print("\nThe bottom 6 Year and Month are as follows: ")
    for i in range(6):
        print(f"{i + 1}. Year: {bottom_six[i][0]} Month: {bottom_six[i][1]} with averages of: {round(bottom_six[i][4], 2)}")

        
        
if __name__ == "__main__":
    filecontents = read_csv(Path("AAPL - AAPL.csv"))

    three_index_container = store_in_storage(filecontents)
    calculate_results(three_index_container)
