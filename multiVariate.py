import numpy
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
        newanswer = answer
    return newanswer

#print(getvalue("Married women currently using any modern method of contraception.csv","Colombia","2015","15-19"))




def one_country_over_time(indicator, country, group):
    goodcountry = []
    goodgroupid = 0
    data = []
    x_values = []
    y_values = []
    indicator = indicator + ".csv"
    with open(indicator) as f:
            reader = csv.reader(f)
            for row in reader:
                    data.append(row)
      
            for row in data:
                    if row[0] == country:
                            goodcountry.append(row)
            for row in goodcountry:
                row[1]  = row[1][:4]
            for j in data[0]:
                if j == group:
                    break
                else:
                    goodgroupid=goodgroupid+1
            for k in goodcountry:
                x_values.append(float(k[1]))
                y_values.append(float(k[goodgroupid]))

    return x_values, y_values    







def simple_correlation_w_plot(indicator1, indicator2, country, group):
    a = []
    b = []
    c = []
    a2 = []
    b2 = []
    
    x1s = one_country_over_time(indicator1, country, group)[0]
    y1s = one_country_over_time(indicator1, country, group)[1]

    x2s = one_country_over_time(indicator2, country, group)[0]
    y2s = one_country_over_time(indicator2, country, group)[1]

    print(y1s)
    print(y2s)
    ybar1 = numpy.mean(y1s)
    ybar2 = numpy.mean(y2s)
    print(ybar2)
    for i in range(len(y1s)):
        a.append(y1s[i] - ybar1)
        b.append(y2s[i] - ybar2)
    for j in range(len(y1s)):
        c.append(a[j]*b[j])
        a2.append(a[j]**2)
        b2.append(b[j]**2)
    c_sum = numpy.sum(c)
    a2_sum = numpy.sum(a2)
    b2_sum = numpy.sum(b2)

    corr_coeff = c_sum/(a2_sum*b2_sum)**0.5
        
    return corr_coeff, x1s, y1s, x2s, y2s



#indicator1 = 'Married women currently using any method of contraception'
#indicator2 = 'Married women currently using any modern method of contraception'
#country = 'Colombia'
#group = 'Total'           

