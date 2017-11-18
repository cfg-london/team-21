#identifier = input("Select new identifier ")

#country = input("Select country ")
#year = input("Select year ")
#value = input("Select value ")


import csv
data = []
with open('takedata.csv') as f:
      reader = csv.reader(f)
      for row in reader:
          data.append(row) 
print(data[1][0])
identifier=data[1][0]
with open(identifier+'.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', lineterminator='\n',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Country', 'Survey','Total'])
    x=len(data)
    for i in range(0, x):
        del data[i][0]
    for i in range(1, x):
        filewriter.writerow(data[i])
    
    
    
    #filewriter.writerow([country,year,value])
    #filewriter.writerow(['Steve', 'Software Developer'])
    #filewriter.writerow(['Paul', 'Manager'])