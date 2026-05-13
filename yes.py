sentence = 'Hello World'

upper = True
sentence2 = ""
for char in sentence:
    if upper:
        char = char.upper()
        upper = False
    else:
        char = char.lower()
        upper = True
    sentence2 += char
print(sentence2)
#HeLlO wOrLd
