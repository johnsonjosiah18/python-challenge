import csv

# Initialize variables
totalmonths = 0
nettotal = 0
changes = []
greatestinc = ["", 0]
greatestdec = ["", float('inf')]

# Read the CSV file
with open('budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # Read and store first row 
    header = next(csvreader)
    first_row = next(csvreader)

    # Intialize total calcualtions
    totalmonths += 1
    nettotal += int(first_row[1])
    prevtotal = int(first_row[1])

    # Process each row using for loop
    for row in csvreader:

        # Calculate net totals, net change, and change from the previous total to be used in greatest increase/decrease calculation
        totalmonths += 1
        nettotal += int(row[1])
        netchange = int(row[1]) - prevtotal
        prevtotal = int(row[1])

        # Store changes in the changes list as 'netchange'
        changes.append(netchange)

        # Calculate the greatest increase
        if netchange > greatestinc[1]:
            greatestinc[0] = row[0]
            greatestinc[1] = netchange

        # Calculate the greatest decrease
        if netchange < greatestdec[1]:
            greatestdec[0] = row[0]
            greatestdec[1] = netchange

# Calculate the average change using the list of changes 
average_change = sum(changes) / len(changes)

# Write the results to a txt file
with open('PyBank.txt', 'w') as w:
    

# Print the financial analysis to a txt file 
    w.write("Financial Analysis \n")
    w.write("----------------------------\n")
    w.write(f"Total Months: {totalmonths}\n")
    w.write(f"Total: ${nettotal}\n")
    w.write(f"Average Change: ${average_change:.2f}\n")
    w.write(f"Greatest Increase in Profits: {greatestinc[0]} (${greatestinc[1]})\n")
    w.write(f"Greatest Decrease in Profits: {greatestdec[0]} (${greatestdec[1]})\n")