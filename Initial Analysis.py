# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The perecntage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

###

# # Assign a variable for the file to load and the path. 
# file_to_load = 'Resources/election_results.csv'

# # open the lection results and read the file
# with open(file_to_load) as election_data:

#     # to do: perform analysis
#     print(election_data)

# # close the file
# election_data.close()

###

# add our dependencies 
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initialize a total vote count
total_votes = 0

# list of candidates (square brackets)
candidate_options = []

# dictionary votes by candidate (curly brackets, key: value)
candidate_votes = {} 

# winning candidate and winning count tracker
winning_candidate = "" # vairable with empty string value
winning_count = 0
winning_percentage = 0 

# open the election results and read the file
with open(file_to_load) as election_data:

    # read the file object with the reader function
    file_reader = csv.reader(election_data)

    # read and print the header row
    headers = next(file_reader)
    for row in file_reader:

        #add to the total vote count
        total_votes += 1

        # retrieve candidate name from each row
        candidate_name = row[2]

        # add candidate name to candidate_options list if unique
        if candidate_name not in candidate_options:            
            candidate_options.append(candidate_name) 
        
            # make each new candidate a key in the candidate_votes dictionary, set vote count to 0
            candidate_votes[candidate_name] = 0 

        # add 1 to vote count
        candidate_votes[candidate_name] += 1

    # save results to our text file
    with open(file_to_save, "w") as txt_file:
        # store content for text file in variables
        election_results = (
        # insert header in the text file
            "\nElection Results\n"
            "-----------------------\n"
            f"Total Votes: {total_votes:,}\n" # ":," is a thousands separator! 
            "-----------------------\n")

        # print text file content
        print(election_results, end="") # ending print with parameter end="" equal to am empty string so the last line is blank

        # save final vote count to text file
        txt_file.write(election_results)
    
        
        # calculate % of votes for each candidate (and add to text file)
        # iterate through candidate list (for each variable in dictionary)
        for candidate_name in candidate_votes:

            # get vote count for candidate (declare variable for number of votes: votes; dictionary_of_votes[value or number of votes])
            votes = candidate_votes[candidate_name]

            # calculate percentage of votes 
            # declare vote_percentage variable, declare number of votes per candidate and number of total votes as floats)
            vote_percentage = float(votes) / float(total_votes) * 100
            # vote_percentage = round(vote_percentage, 1), skill drill to round to 1 decimal place, done later a diff way

            # print the candidate's name and their percentage of votes
            # use print(f) to use code in a string (instead of it being literal) (":.1f" rounds float to 1 decimal place)
            # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            # store content for text file in variable
            candidate_results = (
                f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            
            # print each candidate, their voter count, and percentage to the terminal 
            print(candidate_results)

            # save candidate results to text file
            txt_file.write(candidate_results)  
 

            # Determine winning candidate
            # determine if the votes are greater than the winning count and percentage (start at 0) 
            # this iterates through candidates and replaces the value of the winners each time it encounters someone with higher values
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # if they are greater, 
                # make the new winning count and winning percentage equal to value of votes and vote_percentage for current candidate
                # vote_percentage
                winning_count = votes
                winning_percentage = vote_percentage
                # set current candidate to winning_candidate
                winning_candidate = candidate_name

        # print(winning_count, winning_percentage, winning_candidate) (just using to check winning candidate code)

        # print out summary of winner
        # create a variable to hold info
        winning_candidate_summary = (
            f"----------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n" # ":," means rounded to 0 decimal places??
            f"Winning Percentage: {winning_percentage:.1f}%\n" # rounding the float to 1 decimal place??
            f"----------\n"
        )
        # save winning candidate's summary to text file
        txt_file.write(winning_candidate_summary)

###

# # create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # using the with statement open the file as a text file
# with open(file_to_save, "w") as txt_file:

#     # write some data to the file
#     txt_file.write("Hello World")
