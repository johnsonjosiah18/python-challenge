import csv

# Initialize variables
total_votes = 0
candidates = {}
winner = ['', 0]

# Read the CSV file
with open('election_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # Read first row
    header = next(csvreader)

    # Count total rows in file
    for row in csvreader:
        total_votes += 1

        # Check for candidate 
        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

        # Check if this candidate has more votes than the current winner
        if candidates[row[2]] > winner[1]:
            winner[0] = row[2]
            winner[1] = candidates[row[2]]

# Write the results to a txt file
with open('PyPoll.txt', 'w') as w:

# Print the financial analysis to a txt file 
    w.write(f'Total Votes: {total_votes}\n')
    w.write('Candidates:\n')
    for candidate, votes in candidates.items():
        w.write(f'{candidate}: {votes} votes ({votes/total_votes*100:.3f}%)\n')
    w.write(f'Winner: {winner[0]}\n')