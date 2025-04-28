number = 5
text = 'Hello World'
text = 'Albatross'
shift = 3

#find 
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = '' 
for char in  text.lower():
    index = alphabet.find(char)
    new_index = index + shift

    encrypted_text =encrypted_text +  alphabet[new_index]
    print('char:', char, 'encrypted_text:',encrypted_text)
sentence = 'My brain hurts'



print(number)
print(text)
print(text[6])
print(text[-1])
print(len(text))
print(type(text))
print(shift)
print(type(shift))

alphabet.find('z')
sentence.find('i')


#Caesar cipher
alphabet.find(text[0])

index =alphabet.find(text[0].lower())
shited = alphabet[index]

shited = alphabet[index + shift]


print(index)
print(shited)

