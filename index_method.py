"""Index Method Practice #1
Find and display on the screen which character occupies the fifth position within the following word:

"computer"""""

word = "computer"
result = word[4]
print(result)

"""Index Method Practice #2
Find and display the index of the first occurrence of the word "practice" in the following sentence:



"In theory, theory and practice are the same. In practice, they are not.""""

sentence = "In theory, theory and practice are the same. In practice, they are not."
result = sentence.index("p")
print(result)

'''Index Method Practice #3
Find and display the index of the last occurrence of the word "practice" in the following sentence:



"In theory, theory and practice are the same. In practice, they are not."'''

sentence = "In theory, theory and practice are the same. In practice, they are not."
result = sentence.rindex("p")
print(result)