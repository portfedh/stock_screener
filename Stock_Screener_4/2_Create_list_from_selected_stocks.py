# Create a list of the stocks that passed the second test
# For futher analysis

# Imports
import os
import json
import csv

# Path where selected stocks are found
path = "./output/1.Blue"
print("Files found in path:'", path,)

# List all the files
dir_list = os.listdir(path)
print(dir_list)
# All files files have a .png extention

# Clean the list
output_list = []
for ticker in dir_list:
    # Remove .png extention
    new = os.path.splitext(ticker)[0]
    # Save element in new variable
    output_list.append(new)

# Sort list alphabetically
output_list.sort()

# Eliminate '.DS_St' from list
output_list.pop(0)

# Save list as JSON file
with open("CF_blue_list.json", "w") as f:
    json.dump(output_list, f, indent=2)
    # indent=2 makes the file human-readable

# Save list as CSV file
with open(output_list, 'w') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(rows)


# Print list in terminal
print("Number of stocks in list: ", len(output_list), "\n")
print(output_list)
