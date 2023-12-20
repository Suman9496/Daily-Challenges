# Write a simple python program to Print the count of each letter in a given sentence
sentence = input("Enter a sentence: ")
letter_count = {}

for letter in sentence:
    if letter.isalpha():
        letter = letter.lower()  # Convert to lowercase to treat 'A' and 'a' as the same letter
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

for letter, count in letter_count.items():
    print(f"'{letter}': {count}")


# Using Function
# def count_letters(sentence):
#     letter_count = {}

#     for letter in sentence:
#         if letter.isalpha():
#             letter = letter.lower()  # Convert to lowercase to treat 'A' and 'a' as the same letter
#             if letter in letter_count:
#                 letter_count[letter] += 1
#             else:
#                 letter_count[letter] = 1

#     return letter_count

# input_sentence = input("Enter a sentence: ")
# result = count_letters(input_sentence)

# for letter, count in result.items():
#     print(f"'{letter}': {count}")
