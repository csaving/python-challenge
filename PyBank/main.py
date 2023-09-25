# Module for creating file paths across operating systems
import os
# Module for reading CSV files
import csv

# Set path for file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Lists to store data
date = []
profit_loss = []
change = []

#Variable to hold previous profit/loss value (intially 0) 
previous_pl = 0

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        #Add data to lists
        date.append(row[0])
        profit_loss.append(int(row[1]))

        #Calculate change (current profit/loss - previous profit/loss)
        #and add to change list
        change.append((int(row[1]))-previous_pl)

        #Set current row's profit/loss as previous profit/loss
        previous_pl = int(row[1])        

#Get number of months from length of date list
total_months = len(date)
#Get net total amount of profit/losses
total = sum(profit_loss)
#Get average change
avg_change = sum(change) / len(change)

#Get greatest increase and decrease in profit/loss
max_change = max(change) 
min_change = min(change)
for i in range(len(change)):
    if change[i] == max(change):
        max_date = date[i]
    elif change[i] == min(change):
        min_date = date[i]

#Create list with output text lines
output_text = ["Financial Analysis", 
               "--------------------------------", 
               f"Total Months: {total_months}",
               f"Total: ${total}",
               f"Average Change: ${round(avg_change,2)}",
               f"Greatest Increase in Profits: {max_date} ${max_change}",
               f"Greatest Decrease in Profits: {min_date} ${min_change}"]
#Print output to terminal
for i in output_text:
    print(i)

# Specify the file to write to
output_path = os.path.join("analysis", "analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as f:

    for i in output_text:
        f.write(i)
        f.write('\n')

 




