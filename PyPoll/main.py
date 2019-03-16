# import dependencies
import os
import csv
from operator import itemgetter

# set path for textfile
pollData = os.path.join("..", "PyPoll", "election_data.csv")

# set output path for poll analysis
outputFile = "Election Results.txt"

# declare variables
votes = 0
totalCandidates = 0
candidateResults = ['', 0]
candidateOptions = []
candidateVotes = {}
results = {}

# open csv textfile
with open(pollData) as csvfile:
    csvreader = csv.DictReader(csvfile)

    # loop through rows
    for row in csvreader:

        # The total number of votes cast
        votes += 1

        # A complete list of candidates who received votes
        totalCandidates = row["Candidate"]

        if row["Candidate"] not in candidateOptions:
            candidateOptions.append(row["Candidate"])
            candidateVotes[row["Candidate"]] = 1

        else:
            candidateVotes[row["Candidate"]] += 1

    print("")
    print("Election Results")
    print("----------------")
    print("Total Votes: " + str(votes))
    print("----------------")

    # The percentage of votes each candidate won
    # The total number of vots each candidate won
    for candidate in candidateVotes:
        candidateResults = (candidate + " " + str(round(((candidateVotes[candidate]/votes)*100)))
              + "% (" + str(candidateVotes[candidate]) + ")")
        print(candidateResults)
    
# The winner of the election based on popular vote

results = sorted(candidateVotes.items(), key=itemgetter(1), reverse=True)
winner = str(results[0])

print("----------------")
print("Winner: " + (winner))
print("----------------")


# output analysis
with open(outputFile, "w", newline="") as textfile:
    
    textfile.write("\n")
    textfile.write("Election Results\n")
    textfile.write("----------------\n")
    textfile.write("Total Votes: " + str(votes))
    textfile.write("\n")
    textfile.write("----------------\n")
    textfile.write(str(results[0]))
    textfile.write("\n")
    textfile.write(str(results[1]))
    textfile.write("\n")
    textfile.write(str(results[2]))
    textfile.write("\n")
    textfile.write(str(results[3]))
    textfile.write("\n")
    textfile.write("----------------\n")
    textfile.write("Winner: " + str(winner))
    textfile.write("\n")
    textfile.write("----------------")


    

    