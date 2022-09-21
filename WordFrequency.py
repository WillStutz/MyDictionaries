infile = open('sometext.txt','r')

word_count = {}

plain_text = infile.read().replace('.','').replace(',','').lower()

for i in plain_text.split():
    word_count[i] = plain_text.count(i)




print(word_count)

infile.close()