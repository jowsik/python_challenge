import os
import csv

#reading csv
electioncsv = os.path.join('Resources','election_data.csv')
with open(electioncsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvreader)
    
    #Setting initial value of the counter = 0
    votes = 0
    total = 0
    #lists to store data
    ballot_ID= []
    county = []
    candidate = []
    unique = []

#iterating through the file to count the rows and add to the total
    for row in csvreader:
        votes+=1
        ballot_ID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
    
    #iterating through file to create a list of each unique candidate
    for x in candidate:
        if x not in unique:
            unique.append(x)
    
    #calculating the number of votes for each candidate
    casperTotal = candidate.count("Charles Casper Stockham")
    dianaTotal = candidate.count("Diana DeGette")
    raymonTotal = candidate.count("Raymon Anthony Doane")
    
    #calculating the percent of the vote for each candidate
    casperPercent = round(((casperTotal/votes)*100),3)
    dianaPercent = round(((dianaTotal/votes)*100),3)
    raymonPercent = round(((raymonTotal/votes)*100),3)

    #determine winner
    if casperTotal > dianaTotal and casperTotal > raymonTotal:
        winner = "Charles Casper Stockham"
    elif dianaTotal > casperTotal and dianaTotal > raymonTotal:
        winner = "Diana DeGette"
    else:
        winner = "Raymon Anthony Doane"

#print results
print(casperPercent)
print(dianaPercent)
print(raymonPercent)
print(unique)
print(votes)
print(winner)    

#write text file
output_file = os.path.join("analysis", "election_analysis.txt")
with open(output_file, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("---------------------------------\n")
    txtfile.write(f"Total Votes: {str(votes)}\n")
    txtfile.write("---------------------------------\n")
    txtfile.write(f"Charles Casper Stockham: {str(casperPercent)} ({str(casperTotal)})\n")
    txtfile.write(f"Diana DeGette: {str(dianaPercent)} ({str(dianaTotal)})\n")
    txtfile.write(f"Raymon Anthony Doane: {str(raymonPercent)} ({str(raymonTotal)})\n")
    txtfile.write("---------------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("---------------------------------")