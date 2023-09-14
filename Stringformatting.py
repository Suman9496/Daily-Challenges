"""Strings Formatting Practice #1
We need to print the associate name and number within the following sentence:

"Dear (associate_name), your associate number is: (associate_number)"

Remember that the precision of your answer (spaces, spelling and punctuation)
is very important to arrive at the correct result."""

associate_name = "Jesse Pinkman"
associate_number = 399058

print(f"Dear {associate_name}, your associate number is: {associate_number}")

'''Strings Formatting Practice #2
Tell the user the amount of points earned within the following phrase:

"You have earned (new_points) points! In total, you have accumulated (total_points) points"

Remember that the precision of your answer (spaces, spelling and punctuation)
 is very important to arrive at the correct result.'''

new_points = 350
total_points = 1225
print(f"You have earned {new_points} points! In total, you have accumulated {total_points} points")

'''Strings Formatting Practice #3
Tell the user the amount of points earned within the following phrase:

"You have earned (new_points) points! In total, you have accumulated (total_points) points"

This time, the amount of points accumulated (total_points) will be equal to the previous_points plus the new_points.

Remember that the precision of your answer (spaces, spelling and punctuation) 
is very important to arrive at the correct result.
'''

previous_points = 875
new_points = 350

print(f"You have earned {new_points} points! In total, you have accumulated {previous_points + new_points} points")


