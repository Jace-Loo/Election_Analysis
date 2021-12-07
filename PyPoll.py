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

# open the election results and read the file
with open(file_to_load) as election_data:

    # read the file object with the reader function
    file_reader = csv.reader(election_data)

    # print the header row
    headers = next(file_reader)
    print(headers)
    

###

# # create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # using the with statement open the file as a text file
# with open(file_to_save, "w") as txt_file:

#     # write some data to the file
#     txt_file.write("Hello World")