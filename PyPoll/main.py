import csv

# Initialize variables
total_votes = 0
candidates = {}
winner = ['', 0]

# Read the CSV file
with open('election_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    # Process each row
    for row in csvreader:
        total_votes += 1

        # Check if this candidate is already in the dictionary
        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

        # Check if this candidate has more votes than the current winner
        if candidates[row[2]] > winner[1]:
            winner[0] = row[2]
            winner[1] = candidates[row[2]]

# Print the results
print(f'Total Votes: {total_votes}')
print('Candidates:')
for candidate, votes in candidates.items():
    print(f'{candidate}: {votes} votes ({votes/total_votes*100:.3f}%)')
print(f'Winner: {winner[0]}')