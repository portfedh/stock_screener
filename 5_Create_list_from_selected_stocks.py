# Create a list of the stocks that passed the first test
# For futher analysis

# Imports
import os
import json

# Get the list of all files
path = "./output/1.Blue"
print("Files found in path:'", path,)
dir_list = os.listdir(path)
# All files files have a .png extention
# Every filename ends in "_BS"
print(dir_list)

# Clean the list
output_list = []
for ticker in dir_list:
    # Remove .png extention
    new = os.path.splitext(ticker)[0]
    # Strip "_BS" from file name
    new = new[:-3]
    # Save element in new variable
    output_list.append(new)

# Sort list alphabetically
output_list.sort()

# Eliminate '.DS_St' from list
output_list.pop(0)

# Save list as JSON file
with open("5y_blue_list.json", "w") as f:
    json.dump(output_list, f, indent=2)
    # indent=2 makes the file human-readable

# Print list in terminal
print("Number of stocks in list: ", len(output_list), "\n")
print(output_list)
