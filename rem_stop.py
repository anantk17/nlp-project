import re

l = ""
stopwords = []
for sline in open("english"):
    for sword in sline.split():
        stopwords.append(sword)

#print stopwords

regex = r'([+-])\s([\s\S]*)\n'
url_regex = r'(((https?:\/\/)?(www\.)?)?([-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6})\b([-a-zA-Z0-9@:%_\+.~#?&//=]*))'

for line in open("data.txt"):
    m = re.match(regex,line)
    sign = m.group(1)
    l = sign + "\t"
    line = m.group(2)
    line = re.sub(url_regex,' ',line)
    line = re.sub('[!@#$,\.\)\(\:\;?\-\+0-9%&*\/_]', ' ', line)
    line = re.sub('[\"\']','',line)
    line = re.sub('wi\sfi','wifi',line,flags=re.I)
    line = re.sub(r'[^\x00-\x7F]+',' ', line)
    for word in line.split():
        if word.lower() not in set(stopwords):
            l = l + word.lower() + " "
    print(l)
    l = "" 
