import re

dictionary = []
for sline in open("/usr/share/dict/words"):
    for sword in sline.split():
        dictionary.append(sword)


l = ""
vwords = []
for vline in open("vocabulary.txt"):
    for vword in vline.split():
        vwords.append(vword)

#print stopwords


def dict_split(s):
    if s in dictionary or s.capitalize() in dictionary:
        return s
    else:
        temp = ""
        i = len(s) - 1
        while i >= 0:
            #print s[:i],i
            if s[:i] in dictionary or s[:i].capitalize() in dictionary:
                temp = s[:i] + " " + dict_split(s[i:])
                return temp
            i = i - 1
        
        return s


regex = r'([+-])\s([\s\S]*)\n'

for line in open("data_stop.txt"):
    m = re.match(regex,line)
    sign = m.group(1)
    l = sign + "\t"
    line = m.group(2)
    for word in line.split():
        if word in vwords:
            l += word + " "
        else:
            
            l = l + dict_split(word) + " "
    print(l)
    l = "" 

