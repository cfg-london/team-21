
import csv



def getvalue(indicator, country, year, group):
    goodcountry = []
    goodcountry_and_year =[]
    goodgroupid = 0
    data = []
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
        newanswer = answer
    return newanswer


