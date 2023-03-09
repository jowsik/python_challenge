import os
import csv

#reading csv
budgetcsv = os.path.join('Resources','budget_data.csv')
with open(budgetcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvreader)
    
    #Setting initial value of the counter = 0
    rowcount = 0
    total = 0
    #lists to store data
    dates = []
    profitLoss = []
    change = []
    
    #iterating through the file to count the rows and add to the total
    for row in csvreader:
        rowcount+=1
        total = total + int(row[1])
        dates.append(row[0])
        profitLoss.append(int(row[1]))
    
    #find change in profit/loss each month
    for n in range(1, len(profitLoss)):
        change.append(profitLoss[n] - profitLoss[n-1])
    
    #find average, max, min
    avgChange = round((sum(change)/len(change)),2)
    greatInc = max(change)
    greatDec = min(change)
    
    #index of greatInc
    i = change.index(greatInc)
    d = change.index(greatDec)
    
    #generate month of greatest inc/dec
    monthGreatInc = dates[i+1]
    monthGreatDec = dates[d+1]
    
    #Print statements
    print(rowcount)
    print(total)
    print(avgChange)
    print(greatInc)
    print(greatDec)
    print(monthGreatInc)
    print(monthGreatDec)
    
#write text file
output_file = os.path.join("analysis", "budget_data.txt")
with open(output_file, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("---------------------------------\n")
    txtfile.write(f"Total Months: {str(rowcount)}\n")
    txtfile.write(f"Total: ${str(total)}\n")
    txtfile.write(f"Average Change: ${str(avgChange)}\n")
    txtfile.write(f"Greatest Increase in Profits: {str(monthGreatInc)} (${str(greatInc)})\n")
    txtfile.write(f"Greatest Decrease in Profits: {str(monthGreatDec)} (${str(greatDec)})\n")
    
    
    