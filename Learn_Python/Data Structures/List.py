word ="Milliways"

vowels = ['a', 'e', 'i', 'o', 'u']

for letter in word:
 if letter in vowels:
   print(letter)

found = []
len(found)

found.append('a')
len(found)

if 'u' not in found:
 found.append('u')

vowels = ['a', 'e', 'i', 'o', 'u']
word = "Milliways"
found = []
for letter in word:
 if letter in vowels:
  if letter not in found:
   found.append(letter)
for vowel in found:
 print(vowel)


