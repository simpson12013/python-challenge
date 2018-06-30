#import dependencies
import os
import csv



csvpath = 'budget_data.csv'
output = 'output.txt'


#COUNT OF ROWS
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV HEADER: {csv_header}")

    #for row in csvreader:
    #    print(row)




        #list comprehesion THIS ONE
    row_count = sum(1 for row in csvreader)
    #print (row_count)

        #.append()
    # row_count = []
    # for row in csvreader:
    #     row_count.append(row)

        #list()
    # rows = list(csvreader)
    # row_count = len(rows)
    # for row in rows:
    #     print (row_count)

#TOTAL NET
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    csv_header = next(csvreader)

        #net.append()
    # net=[]
    # for row in csvreader:
    #     net.append(2)
    # print (net)
    # nettotal = sum(net)
    # print (nettotal)

        #list comprehension
    net = sum(int(row[1]) for row in csvreader)
    #print (net)

#Average Change
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    csv_header = next(csvreader)

        #net.append()
    # net=[]
    # for row in csvreader:
    #     net.append(2)
    # print (net)
    # nettotal = sum(net)
    # print (nettotal)

        #list comprehension
    change = []
    changem = []
    d = 1
    for row in csvreader:
        if d == 1:
            i = row[1]
            changem.append(row[0])
            d = d + 1
        else:
            change.append(int(row[1])-int(i))
            i = row[1]
            changem.append(row[0])

    avgchange = (sum(change)/len(change))
    
    maxchange = max(change)
    maxchangeindex = change.index(maxchange)
    maxmonth = changem[maxchangeindex + 1]
    
    minchange = min(change)
    minchangeindex = change.index(minchange)
    minmonth = changem[minchangeindex + 1]
    
    print ("Financial Analysis")
    print ("--------------------------")
    print ("Total Months: " + str(row_count))
    print ("Total Profit/Losses: $" + str(net))
    print ("Average Change: $" + str(avgchange))
    print ("Greatest Increase in Profits: " + maxmonth + " ($" + str(maxchange) + ")")
    print ("Greatest Decrease in Profits: " + minmonth + " ($" + str(minchange) + ")")

with open('output.txt','w') as text_file:

   print ("Financial Analysis", file = text_file)
   print ("--------------------------", file = text_file)
   print ("Total Months: " + str(row_count), file = text_file)
   print ("Total Profit/Losses: $" + str(net), file = text_file)
   print ("Average Change: $" + str(avgchange), file = text_file)
   print ("Greatest Increase in Profits: " + maxmonth + " ($" + str(maxchange) + ")", file = text_file)
   print ("Greatest Decrease in Profits: " + minmonth + " ($" + str(minchange) + ")", file = text_file)