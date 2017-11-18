
import csv

popC = [48650000]
popIndia=[1324000000]
popIndo=[261100000]
popK=[48460000]
popS=[15410000]

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
        newanswer = 0
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


def yearexists(indicator, country, year):
    flag=0
    for i in possibleyear(indicator, country):
        if i == year:
            flag=1
    return flag

def comparecountry(indicator,year,group):
    lcountry=["Colombia","India","Indonesia","Kenya","Senegal"]
    lvalue=[]
    if yearexists(indicator,lcountry[0],year) == 1:
        lvalue.append(getvalue(indicator,lcountry[0],year,group))
    else:
        lvalue.append(0)
        
    if yearexists(indicator,lcountry[1],year) == 1:
        lvalue.append(getvalue(indicator,lcountry[1],year,group))
    else:
        lvalue.append(0)
        
    if yearexists(indicator,lcountry[2],year) == 1:
        lvalue.append(getvalue(indicator,lcountry[2],year,group))
    else:
        lvalue.append(0)
        
    if yearexists(indicator,lcountry[3],year) == 1:
        lvalue.append(getvalue(indicator,lcountry[3],year,group))
    else:
        lvalue.append(0)
        
    if yearexists(indicator,lcountry[4],year) == 1:
        lvalue.append(getvalue(indicator,lcountry[4],year,group))
    else:
        lvalue.append(0)
    return lcountry,lvalue


print(getvalue("Married women currently using any modern method of contraception","Colombia","2015","15-19"))

print (yearexists("Married women currently using any modern method of contraception","Colombia","2015"))

print(comparecountry("Married women currently using any modern method of contraception","2015","15-19"))

#print(getvalue("Married women currently using any modern method of contraception","Colombia","2015","15-19"))
#print(possiblegroup("Married women currently using any modern method of contraception","Colombia","2005"))
