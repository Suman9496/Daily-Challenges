"""Interactions Between Functions Practice #1
Create a function (throw_dice) that "throws" two random dice and returns its results (the function MUST RETURN TWO VALUES AS A RESULT, both of which must be between 1 and 6, randomly).

Pass the result of these two dice to a function called roll_result (meaning that this second function MUST RECEIVE TWO ARGUMENTS) and return -without printing it- a certain message according to the what the sum of these values results:

If the sum is less than or equal to 6:

"The sum of your dice is {sum_dice}. Unfortunate"

If the sum is greater than 6 and less than 10:

"The sum of your dice is {sum_dice}. You have a good chance"

If the sum is greater than or equal to 10:

"The sum of your dice is {sum_dice}. It looks like a winning roll"

Hint: use the random library's choice or randint method to choose a random value between 1 and 6."""

import random


def throw_dice():
    """Throws two dice and returns their results."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2


def roll_result(die1, die2):
    """Returns a message according to the sum of the two dice."""
    sum_dice = die1 + die2
    if sum_dice <= 6:
        return "The sum of your dice is {}. Unfortunate".format(sum_dice)
    elif 6 < sum_dice < 10:
        return "The sum of your dice is {}. You have a good chance".format(sum_dice)
    else:
        return "The sum of your dice is {}. It looks like a winning roll".format(sum_dice)


die1, die2 = throw_dice()

roll_result_message = roll_result(die1, die2)

print(roll_result_message)
