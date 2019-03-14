#import modules
import os
import csv

#set path fro datafile
budgetData = os.path.join("..","PyBank","budget_data.csv")

#set the output path of text datafile
outputAnalysis = "Budget Analysis.txt"

#set variables
totalMonths = 0
totalRevenue = 0
revenue = []
previousRevenue = 0
monthOfChange = []
revenueChange = 0
greatestDecrease = ["", 9999999]
greatestIncrease = ["", 0]
revenueChangeList = []
revenueAverage = 0

#open csv datafile
with open("budget_data.csv") as csvfile:
    csvReader = csv.DictReader(csvfile)

    #loop through to datafile
    for row in csvReader:

        #count total months
        totalMonths += 1

        #calculate total revenue over entire period
        totalRevenue = totalRevenue + int(row["Profit/Losses"])

        #calculate average change in revenue between
        #months over entire period
        revenueChange = float(row["Profit/Losses"]) - previousRevenue
        previousRevenue = float(row["Profit/Losses"])
        revenueChangeList = revenueChangeList + [revenueChange]
        monthOfChange = [monthOfChange] + [row["Date"]]

        #greatest increase in revenue(date and amount)
        #over the entire period
        if revenueChange > greatestIncrease[1]:
            greatestIncrease[1] = revenueChange
            greatestIncrease[0] = row["Date"]

        #greatest decrease in revenue(date and amount)
        #over the entire period
        if revenueChange < greatestDecrease[1]:
            greatestDecrease[1] = revenueChange
            greatestDecrease[0] = row["Date"]

        #aver change in "Profit/Losses" over entire period
        revenueAverage = sum(revenueChangeList)/len(revenueChangeList)

#print analysis to console
    print(f"Budget Analysis")
    print(f"--------------------------------------------")
    print(f"Total Months: {str(totalMonths)}")
    print(f"Total Revenue: {str(totalRevenue)}")
    print(f"Average Revenue Change: {str(revenueAverage)}")
    print(f"Greatest Increase in Revenue: {str(greatestIncrease[0])}, {str(greatestIncrease[1])}")
    print(f"Greatest Decrease in Revenue: {str(greatestDecrease[0])}, {str(greatestDecrease[1])}")

#write changes to csv
with open(outputAnalysis, "w", newline="") as datafile:

    datafile.write("Budget Analysis\n")
    datafile.write("-------------------------------------\n")
    datafile.write("Total Months: %d\n" % totalMonths)
    datafile.write("Total Revenue: $%d\n" % totalRevenue)
    datafile.write("Average Revenue Change: $%d\n" % revenueAverage)
    datafile.write("Greatest Increase in Revenue: %s ($%s)\n" % (greatestIncrease[0], greatestIncrease[1]))
    datafile.write("Greatest Decrease in Revenue: %s ($%s)\n" % (greatestDecrease[0], greatestDecrease[1]))
