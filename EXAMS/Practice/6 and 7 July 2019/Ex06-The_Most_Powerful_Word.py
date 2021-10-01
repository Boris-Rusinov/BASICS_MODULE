from math import floor
from sys import maxsize

curr_word = input()
curr_word_length = len(curr_word)
curr_word_score = 0
largest_word_score = -maxsize
strongest_word = ""

while curr_word != "End of words":
    for index in range(0, curr_word_length):
        curr_word_score += ord(curr_word[index])

    if curr_word[0] == "a" or curr_word[0] == "e" or curr_word[0] == "i" or curr_word[0] == "o" or curr_word[0] == "u" or curr_word[0] == "y" or curr_word[0] == "A" or curr_word[0] == "E" or curr_word[0] == "I" or curr_word[0] == "O" or curr_word[0] == "U" or curr_word[0] == "Y":
        curr_word_score *= curr_word_length
    else:
        curr_word_score = floor(curr_word_score / curr_word_length)

    if curr_word_score > largest_word_score:
        largest_word_score = curr_word_score
        strongest_word = curr_word

    curr_word = input()
    curr_word_score = 0
    curr_word_length = len(curr_word)

print(f"The most powerful word is {strongest_word} - {largest_word_score}")