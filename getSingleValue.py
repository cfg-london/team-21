
import csv



def getvalue(indicator, country, year, group):
    goodcountry = []
    goodcountry_and_year =[]
    goodgroupid = 0
    data = []
    indicator = indicator + ".csv"
    with open(indicator) as f:
      reader = csv.reader(f)
      for row in reader:
          data.append(row)
          
      for row in data:
          if row[0] == country:
              goodcountry.append(row)
      for row in goodcountry:
          if row[1][:4] == year:
              goodcountry_and_year.append(row)
      for j in data[0]:
          if j == group:
              break
          else:
              goodgroupid=goodgroupid+1
    
    answer = goodcountry_and_year[0][goodgroupid]          
    if answer == "":
        newanswer = "N/A"
    else:
        newanswer = float(answer)
    
    return newanswer

def possibleyear(indicator, country):
    indicator = indicator + ".csv"
    data = []
    pyear= []
    with open(indicator) as f:
      reader = csv.reader(f)
      for row in reader:
          data.append(row)
    for row in data:
        if row[0] == country:
            pyear.append(row[1][:4])
    return pyear

def possiblegroup(indicator,country, year):
    indicator = indicator + ".csv"
    data = []
    pgroup = []
    with open(indicator) as f:
      reader = csv.reader(f)
      for row in reader:
          data.append(row)
    for i in data[0]:
        if i!="Country" and i!="Survey":
            pgroup.append(i)
    return pgroup




#print(getvalue("Married women currently using any modern method of contraception","Colombia","2015","15-19"))
#print(possiblegroup("Married women currently using any modern method of contraception","Colombia","2005"))
