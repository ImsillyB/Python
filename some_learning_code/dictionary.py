# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from collections import defaultdict

sentence = "Peter Piper picked a peck of pickled peppers A peck of pickled peppers Peter Piper picked If Peter Piper picked a peck of pickled peppers Wheres the peck of pickled peppers Peter Piper picked"

word_dict = {}

for word in sentence.split():
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1


print(word_dict)





word_dict = defaultdict(int)

for word in sentence.split():
    word_dict[word] +=1
    
print (word_dict)
for key, value in word_dict.items():
    print (key, value)
    



from collections import Counter

words = sentence.split()

word_count = Counter(words)

print (word_count['Peter'])
print (word_dict)