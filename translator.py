# Originally from codecademy.com with minor additions from Nxtstep101

pyg = 'ay'
print 'Python Pyglatin Translator - Codeacademy and Nxtstep101'
user_input = raw_input('Enter a word:')
if len(user_input) > 0 and user_input.isalpha():
    word = user_input.lower()
    first = word[0]
    transl = word[1:] + first + pyg
    print 'Translated: %s' % transl
else:
    print 'Please enter a proper word'
