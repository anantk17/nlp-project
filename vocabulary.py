from collections import Counter
import re

regex = r'([+-])\s([\s\S]*)\n'
words = []
for line in open("data_stop3.txt"):
    m = re.match(regex,line)
    line = m.group(2)
    words += line.split()

c = Counter(words)
print c
vocabulary = []
print c.items()
with open('vocabulary3.txt','w') as outfile:
    for key,value in c.items():
        print key, value
        if len(key) > 1 and value >= 2 :
            vocabulary.append(key)
            outfile.write(key+"\n")

