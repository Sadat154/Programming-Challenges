import csv



def read_csv(csv_file):
    csv_contents = []


    with open(csv_file) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")

        for row in reader:
            csv_contents.append(row)
    return csv_contents


## read the specified csv file just like Challenge 10

def read_html(html_file):
    file = open(html_file, "rt", encoding="utf-8")
    readFile =  file.read()


    return readFile

## read a html file as a regular file

def process(csv, html):


    replacements = ["link","initials","name"]

    counter = -1
    for i in range(len(replacements)):
        counter += 1
        for x in range(5):
            name = replacements[i]+str((x+1))

            newVals = html.replace(name,csv[counter][i])
            html = newVals


            counter +=1
        counter = -1
    return newVals

## replace link1...link5 in html with corresponding values fronm csv
## Similarly do for initials1...intitials5 and name1...name5

def write_html(path, html):
    with open(path, 'w') as f:
        f.write(html)



## write the new contents into an html file


if __name__ == "__main__":
    csv = read_csv("south.csv")


    html = read_html("south.html")

    html = process(csv, html)

    write_html("south_final.html", html)