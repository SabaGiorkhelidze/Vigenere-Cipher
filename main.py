from itertools import product
start = input('Do you want to encrypt or decript? -- (e || d): ')

#       _____ encryption _____

def encrypt():
    letters = 'abcdefghijklmnopqrstuvwxyz'

    char_to_index = dict(zip(letters, range(len(letters))))
    index_to_char = dict(zip(range(len(letters)), letters))


    word = input('enter word to encript: ').split(' ')
    final_word = ''
    for i in word:
        final_word += i
        
    
    key_word = input('enter key word: ')
    
    
    key = []
    index_in_word = []
    index_in_key = []
    show = []

    # key ==> keyk
    if len(final_word) > len(key_word):
        for key_length in range(len(final_word) - len(key_word)):
            key.append(key_word[key_length % len(key_word)])
        key_word += "" . join(key)
        

        for i in final_word:
            index_in_word.append(int(char_to_index[i]))
        for j in key_word:
            index_in_key.append(int(char_to_index[j]))

        
        for word_length, key_word_length in product(range(len(index_in_word)), range(len(index_in_key))):
            if word_length == key_word_length:
                index = index_in_word[word_length] + index_in_key[key_word_length]
                if index > 25:
                    index -= 26
                    show.append(index_to_char[index])
                else:
                    show.append(index_to_char[index])

        return ''.join(show)
    else:
        for i in final_word:
            index_in_word.append(int(char_to_index[i]))
        for j in key_word:
            index_in_key.append(int(char_to_index[j]))

        for word_length, key_word_length in product(range(len(index_in_word)), range(len(index_in_key))):
            if word_length == key_word_length:
                index = index_in_word[word_length] + index_in_key[key_word_length]
                if index > 25:
                    index -= 26
                    show.append(index_to_char[index])
                else:
                    show.append(index_to_char[index])

        return ''.join(show)





#       _____ decryption _____

def decrypt():
    letters = 'abcdefghijklmnopqrstuvwxyz'

    char_to_index = dict(zip(letters, range(len(letters))))
    index_to_char = dict(zip(range(len(letters)), letters))


    cypher_word = input('enter word to decript: ').split(' ')
    final_word = ''
    for i in cypher_word:
        final_word += i

    key_word = input('enter key word: ')

    key = []
    index_in_word = []
    index_in_key = []
    show = []

    if len(final_word) > len(key_word):
        for key_length in range(len(final_word) - len(key_word)):
            key.append(key_word[key_length % len(key_word)])
        key_word += "" . join(key)
        

        for i in final_word:
            index_in_word.append(int(char_to_index[i]))
        for j in key_word:
            index_in_key.append(int(char_to_index[j]))

        
        for word_length, key_word_length in product(range(len(index_in_word)), range(len(index_in_key))):
            if word_length == key_word_length:
                index = index_in_word[word_length] - index_in_key[key_word_length]
                if index < 0:
                    index += 26
                    show.append(index_to_char[index])
                else:
                    show.append(index_to_char[index])

        return ''.join(show)

    else:
        for i in final_word:
            index_in_word.append(int(char_to_index[i]))
        for j in key_word:
            index_in_key.append(int(char_to_index[j]))

        for word_length, key_word_length in product(range(len(index_in_word)), range(len(index_in_key))):
            if word_length == key_word_length:
                index = index_in_word[word_length] - index_in_key[key_word_length]
                if index < 0:
                    index += 26
                    show.append(index_to_char[index])
                else:
                    show.append(index_to_char[index])

        return ''.join(show)




    
if start == 'e':
    print(encrypt())
elif start == 'd':
    print(decrypt())
else:
    print('error')