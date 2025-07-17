word = "Milliways"  # The word to be checked for vowels

vowels = ['a', 'e', 'i', 'o', 'u']  # List of vowels to check against

# Loop through each letter in the word
for letter in word:
    if letter in vowels:  # Check if the current letter is a vowel
        print(letter)     # Print the vowel found


found = []
len(found)

found.append('a')
len(found)


if 'u' not in found:
 found.append('u')

vowels = ['a', 'e', 'i', 'o', 'u']  # List of vowels
word = "Milliways"                 # Word to extract vowels from
found = []                         # Empty list to hold found vowels

# Iterate over each letter in the word
for letter in word:
    if letter in vowels:             # Check if it's a vowel
        if letter not in found:      # Check if vowel is already recorded
            found.append(letter)     # Add unique vowel to the list

# Print each unique vowel found in the word
for vowel in found:
    print(vowel)






string = "don't panic!"      # Original string
list1 = list(string)         # Convert string into a list of characters

# Remove unnecessary characters by popping at specific indices
for i in [11, 10, 9, 8, 3, 0]:
    list1.pop(i)             # Remove characters at positions to shape the phrase

# At this point, list1 = ['o', 'n', 't', ' ', 'p', 'a']

# Move 'a' (index 5) to index 4
list1.insert(4, list1.pop(5))

# Now list1 = ['o', 'n', 't', ' ', 'a', 'p']

# Move 't' (index 3) to index 2
list1.insert(2, list1.pop(3))

# Final rearranged list: ['o', 'n', ' ', 't', 'a', 'p']

final_string = ' '.join(list1)  # Join the list into a string with spaces between each character
print(final_string)             # Result: 'o n   t a p'
phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)




phrase = "Don't panic!"      # Original phrase
plist = list(phrase)         # Convert the phrase into a list of characters

print(phrase)                # Print original string
print(plist)                 # Print list version

# Extract letters at index 1 and 2 => 'o' and 'n'
new_phrase = ''.join(plist[1:3])

# Add specific characters by their indexes to form "on tap"
# plist[5] = 'p', plist[4] = ' ', plist[7] = 'a', plist[6] = 'n'
new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[7], plist[6]])

# Print intermediate list and final phrase
print(plist)                 # Original list remains unchanged
print(new_phrase)           # Output: 'on pan'




paranoid_android = "Marvin"
letters = list(paranoid_android)
for char in letters:
  print('\t', char)


paranoid_android = "Marvin, the Paranoid Android"
letters = list(paranoid_android)
for char in letters[:6]:
  print('\t', char)
print()
for char in letters[-7:]:
  print('\t'*2, char)
print()
for char in letters[12:20]:
  print('\t'*3, char)

