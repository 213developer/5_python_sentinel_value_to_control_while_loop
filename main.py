"""
MovieGuide.py

This program allows each theater patron to enter a value from
0 to 4 indicating the number of stars that the patron awards
to the Guide's featured movie of the week. The program
executes continuously until the theater manager enters a
negative number to quit. At the end of the program, the
average star rating for the movie is displayed.
"""

# Initialize variables.
totalStars = 0  # total of star ratings.
numPatrons = 0  # keep track of number of patrons
averageStars = 0
numStars = 0
# Get input.
numStarsString = input("Enter rating for featured movie: ")

# Convert to double.
numStars = float(numStarsString)

# Write while loop here
while numStars >= 0 and numStars <= 4:
    numPatrons = numPatrons + 1 #incrementer
    totalStars = totalStars + numStars
    # Get input.
    numStarsString = input("Enter rating for featured movie: ")

    # Convert to double.
    numStars = float(numStarsString)

# Calculate average star rating
averageStars = totalStars / numPatrons

print("Average Star Value: " + str(averageStars))
