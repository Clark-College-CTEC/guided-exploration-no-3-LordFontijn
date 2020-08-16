# Guided Exploration No. 3
# Nick Strickland

# imports the random library for use in our program
import random

# creates a list where the imported rap names can be stored
possible_names = []

# opens a new file that stores the names generated
outputFile = open('rap-names-output.txt', 'w')

# opens the rap names file in read-only mode and stores it as a variable
with open('rap-names.txt', 'r') as dataFile:
    # loops through each name/entry in the list of rap names
    for name in dataFile:
        # adds names to the possible names list and cuts off the spacing at the end of each name
        possible_names.append(name.rstrip())
# prompts the user for the number of names to be created
count = int(input('How many rap names would you like to create? '))
# prompts the user for the number of parts each name should have
parts = int(input('How many parts should the name contain? '))
# executes the following code for every rap name user wants generated
for i in range(count):
    # creates a new list to store the randomly generated rap name parts into
    name_parts = []
    # executes the following code for the specified number of parts to each rap name
    for j in range(parts):
        # randomly chooses a name part from the possible_names list, then adds it to the name_parts list
        name_parts.append(possible_names[random.randint(0, len(possible_names)-1)])
# writes the names to rap-names-output.txt by taking the items in name_parts and joining them together, separating with a space and making a new line between each name
    outputFile.write(f"{' '.join(name_parts)}\n")
# prints out the name(s) generated
    print(f"{' '.join(name_parts)}")
# closes the rap-names-output.txt file
outputFile.close()
