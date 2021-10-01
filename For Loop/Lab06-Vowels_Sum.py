word = input()

word_length = len(word)

total_sum = 0

for curr_index in range(0, word_length):
    if word[curr_index] == "a":
        total_sum += 1
    elif word[curr_index] == "e":
        total_sum += 2
    elif word[curr_index] == "i":
        total_sum += 3
    elif word[curr_index] == "o":
        total_sum += 4
    elif word[curr_index] == "u":
        total_sum += 5

print(total_sum)