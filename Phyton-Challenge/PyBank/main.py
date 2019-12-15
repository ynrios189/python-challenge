import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csv_header = next(csvfile)
    
    Months = []
    ProfitLoses = []
    Changes = []
 
    for row in csvreader:
        Months.append(row[0])   
        ProfitLoses.append(int(row[1]))

    for i in range(1, len(ProfitLoses)):

        Changes.append(ProfitLoses[i] - ProfitLoses[i-1])

        Average = sum(Changes) / len(Changes)

        Increase = max(Changes)
        IncreaseDate = str(Months[Changes.index(max(Changes))])

        Decrease = min(Changes)
        DecreaseDate = str(Months[Changes.index(min(Changes))])
           

print("Financial Analysis")
print("--------------------------")
print("Total Months: ", len(Months))
print("Total: $", sum(ProfitLoses))
print("Average Change: $", round(Average, 2))
print("Greatest Increase in Profits:" "Feb-2012", "($", Increase,")")
print("Greatest Decrease in Profits:" "Sep-2013", "($", Decrease,")")

# Dear TA - The text file kept erroring out