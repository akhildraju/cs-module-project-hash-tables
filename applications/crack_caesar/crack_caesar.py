# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

import os

#read the contents of the file
input_file = open(f"{os.getcwd()}/applications/crack_caesar/ciphertext.txt")

text = input_file.read()

count_map = {}

count  = 0

#count all uppercase characters and how many times  they appear
#also count total number of uppercase charactersß
for c in text:

    if not c.isupper():
        continue

    count += 1
    if c not in count_map:
        count_map[c] = 1
    else:
        count_map[c] += 1

print (count_map)
print (count)

# Creating a dict  of the frequency of uppercase characters.
freq_map = {}
for c in count_map.keys():
    freq_map[c] = round((count_map[c]/count) * 100, 2)

print (freq_map)

reverse_letter_map  = {11.53: 'E', 9.75: 'T', 8.46: 'A', 8.08: 'O', 7.71: 'H', 
                       6.73:   'N', 6.29: 'R', 5.84: 'I', 5.56: 'S', 4.74: 'D', 
                       3.92:   'L', 3.08: 'W', 2.59: 'U', 2.48: 'G', 2.42: 'F', 
                       2.19:   'B', 2.18: 'M', 2.02: 'Y', 1.58: 'C', 1.08: 'P', 
                       0.84: 'K', 0.59: 'V', 0.17: 'Q', 0.07: 'X', 0.03: 'Z'}

output = 'S'

# based on the frequencies decipher the character.
for c in text:

    if not c.isupper():
        output += c
        continue

    freq =  freq_map[c]
    decipher = reverse_letter_map[freq]
    output += decipher


print(output)

