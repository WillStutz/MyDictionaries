infile = open('info_security.txt','r')
outfile = open('encrypted.txt','w')

Encrypt_Key = {' ': ' '}
content = str(infile.read())

letter = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm:."
other = ")(*&^%$#@!-++<>5647382910PoIuYtReWq?!~|LkJhGfDsAmNbVc,"

for i in range(0, len(letter)):
    if letter[i] not in Encrypt_Key:
        Encrypt_Key[letter[i]] = other[i]

Encrypt_Text = ""

for i in content:
    Encrypt_Text += Encrypt_Key[i]

outfile.write(Encrypt_Text)