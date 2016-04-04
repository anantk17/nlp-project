import re
from collections import Counter

def read_stopwords(stop_file):
    """
    Read stop words from stop_file into a list
    """
    stopwords = []
    for sline in open(stop_file):
        for sword in sline.split():
            stopwords.append(sword)

    return stopwords

def remove_stop_words(data_file,stopwords_file,out_file,):
    """
    Reads data_file line by line, removes stop words from each line, writes line to out_file
    """
    #data_lines = []
    l = ""
    stopwords = read_stopwords(stopwords_file)
    
    regex = r'([+-])\s([\s\S]*)\n'
    url_regex = r'(((https?:\/\/)?(www\.)?)?([-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6})\b([-a-zA-Z0-9@:%_\+.~#?&//=]*))'

    with open(out_file,'w') as writeFile:
        for line in open(data_file):
            m = re.match(regex,line)
            sign = m.group(1)
            l = sign + "\t"
            line = m.group(2)
            line = re.sub(url_regex,' ',line)
            line = re.sub('[~`^=!@#$,\.\)\(\:\;?\-\+0-9%&*\/_\{\}\[\]<>]', ' ', line)
            line = re.sub('[\"\']','',line)
            line = re.sub('wi\sfi','wifi',line,flags=re.I)
            line = re.sub(r'[^\x00-\x7F]+',' ', line)
            for word in line.split():
                if word.lower() not in set(stopwords):
                    l = l + word.lower() + " "

            l = l + "\n"
            writeFile.write(l)
        #data_lines.append(l)

            l = "" 
    
    #return data_lines


def gen_vocab_list(data_file):
    """
    Generates list of words in vocabulary from data file
    """

    regex = r'([+-])\s([\s\S]*)\n'
    words = []
    for line in open(data_file):
        m = re.match(regex,line)
        line = m.group(2)
        words += line.split()

    c = Counter(words)
    vocabulary = []
    for key,value in c.items():
        if len(key) > 1 and value >= 2 :
                vocabulary.append(key)
                #outfile.write(key+"\n")

    return vocabulary

def get_dict_words():
    """
    Gets list of words from dictionary 
    (Currently default list of words available on any linux distro is used)
    """
    dictionary = []
    for sline in open("/usr/share/dict/words"):
        for sword in sline.split():
            dictionary.append(sword)
    
    return dictionary

def dict_split(s,dictionary):
    """
    Splits a word not existing in the dictionary into a list of words that are present in it
    """

    if s in dictionary or s.capitalize() in dictionary:
        return s
    else:
        temp = ""
        i = len(s) - 1
        while i >= 0:
            #print s[:i],i
            if s[:i] in dictionary or s[:i].capitalize() in dictionary:
                temp = s[:i] + " " + dict_split(s[i:],dictionary)
                return temp
            i = i - 1
        
        return s

def extract_clubbed_words(data_file,vwords,dictionary,out_file):
    """
    Dataset was found to contain words which clubbed important words together like
    'horribleconsno',etc.. 
    The words 'horrible', 'cons', 'no' seemed to be important for our task.
    Given a  data file, dictionary and vocabulary generated from the data_file, we split words in
    data_file which are not present in vocabulary and also not present in dictionary into a sequence
    of words that are present in the dictionary
    """

    #final_data = []
    regex = r'([+-])\s([\s\S]*)\n'
    
    #dictionary = get_dict_words()

    with open(out_file,'w') as outFile:
        for line in open(data_file):
            m = re.match(regex,line)
            sign = m.group(1)
            l = sign + "\t"
            line = m.group(2)
            for word in line.split():
                if word in vwords:
                    l += word + " "
                else:
                    l = l + dict_split(word,dictionary) + " "
            #print(l)
            l = l + "\n"
            outFile.write(l)

        #final_data.append(l)
            l = "" 

remove_stop_words('data.txt','english','data-final-1-stop.txt')
vocab = gen_vocab_list('data-final-1-stop.txt')
dictionary = get_dict_words()
extract_clubbed_words('data-final-1-stop.txt',vocab,dictionary,'data-final-2-stop.txt')
remove_stop_words('data-final-2-stop.txt','english','data-final-stop.txt')


