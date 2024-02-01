#Import dependencies 
import pandas as pd
import csv


# Loading election data csv
file_to_load = ("c:/Users/llman/Downloads/Starter_Code (26)/Starter_Code/PyPoll/Resources/election_data.csv")
file_to_text = "election_data.txt"

#Store Data
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0

#Read CSV and convert to dictionaries
with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)

    #Each row
    for row in reader:
        #Total votes
        total_votes = total_votes + 1
        #Extract candidate name per row
        candidate_name = row["Candidate"]

        #Other candidates
        if candidate_name not in candidate_options:
            #Add new candidates
            candidate_options.append(candidate_name)
            #Add other candidate's votes
            candidate_votes[candidate_name] = 0
        #Adding votes to the candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

#Print election results and export data to text file
with open(file_to_text, "w") as txt_file:
    #Print vote count
    election_results = (
        f"\nElection Results\n"
        f"\n----------------------\n"
        f"\nTotal Votes: {total_votes}\n"
        f"\n----------------------\n"
    )
    #Print and save to txt file
    print(election_results)
    txt_file.write(election_results)

    #Determine the winner by looping
    for candidate in candidate_votes:
        #Vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        #Determine winning candidate with most votes
        if(votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
        
        #Print each candidate's count, percentage, and save to text
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output)
        txt_file.write(voter_output)

    #Print winner
    winner = (
    f"\n----------------------\n"
    f"\nWinner: {winning_candidate}\n"
    f"\n-----------------------\n"
        )
    #Print and save to txt file
    print(winner)
    txt_file.write(winner)
