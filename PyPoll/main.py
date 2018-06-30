import os
import csv

csvpath = 'election_data.csv'
output = 'output.txt'

with open(csvpath, newline = '') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')

   csv_header = next(csvreader)

   row_count = sum(1 for row in csvreader)



with open(csvpath, newline = '') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')

   csv_header = next(csvreader)

   candidates = []

   for row in csvreader:
       candidate = row[2].split()
       for word in candidate:
           if word not in candidates:
               candidates.append(word)

with open(csvpath, newline = '') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')

   csv_header = next(csvreader)
   canone = 0
   cantwo = 0
   canthree = 0
   canfour = 0
   for row in csvreader:
       if candidates[0] == row[2]:
           canone = canone + 1
       if candidates[1] == row[2]:
           cantwo = cantwo + 1
       if candidates[2] == row[2]:
           canthree = canthree + 1
       if candidates[3] == row[2]:
           canfour = canfour + 1
canvotes = [canone, cantwo, canthree, canfour]
winnerfinder = canvotes.index(max(canvotes))
winner = candidates[winnerfinder]

print ("Election Results")
print ("---------------------------")
print ("Total Votes: " + str(row_count))
print ("---------------------------")
print (candidates[0] + ":" + " {0:.0%} ".format(canone/row_count) + "(" + str(canone) + ")")
print (candidates[1] + ":" + " {0:.0%} ".format(cantwo/row_count) + "(" + str(cantwo) + ")")
print (candidates[2] + ":" + " {0:.0%} ".format(canthree/row_count) + "(" + str(canthree) + ")")
print (candidates[3] + ":" + " {0:.0%} ".format(canfour/row_count) + "(" + str(canfour) + ")")
print ("---------------------------")
print ("Winner: " + winner)
print ("---------------------------")

with open('output.txt', 'w') as text_file:

   print ("Election Results", file = text_file)
   print ("---------------------------", file = text_file)
   print ("Total Votes: " + str(row_count), file = text_file)
   print ("---------------------------", file = text_file)
   print (candidates[0] + ":" + " {0:.0%} ".format(canone/row_count) + "(" + str(canone) + ")", file = text_file)
   print (candidates[1] + ":" + " {0:.0%} ".format(cantwo/row_count) + "(" + str(cantwo) + ")", file = text_file)
   print (candidates[2] + ":" + " {0:.0%} ".format(canthree/row_count) + "(" + str(canthree) + ")", file = text_file)
   print (candidates[3] + ":" + " {0:.0%} ".format(canfour/row_count) + "(" + str(canfour) + ")", file = text_file)
   print ("---------------------------", file = text_file)
   print ("Winner: " + winner, file = text_file)
   print ("---------------------------", file = text_file)