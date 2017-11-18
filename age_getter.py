import csv


def get_num_ages(indicator, country):
    indicator = indicator + ".csv"
    data = []
    goodcountry= []
    ages = []
    with open(indicator) as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
        for row in data:
            if row[0] == country:
                  goodcountry.append(row)

        num_ages = len(data[0]) - 2

        for j in range(len(data[0])-2):
            ages.append(data[0][j+2])

    return ages

