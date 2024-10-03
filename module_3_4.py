
def check(wordB, wordL):
    for i in range(0, len(wordB) - len(wordL)):
        x = 0
        b = False

        for j in range(0, len(wordL)):

            if wordB[i + j] == wordL[j]:
                x += 1
            else:
                x = 0
                
        if x == len(wordL):
            b = True
            break

    return b

def single_root_words(root_word, *other_words):
    same_words = []

    for i in other_words:
        b = 0
        if len(root_word) > len(i):
            b = check(root_word.upper(), i.upper())

        elif root_word.upper() == i.upper():
            same_words.append(i)

        elif len(root_word) < len(i):
            b = check(i.upper(), root_word.upper())

        if b == 1:
            same_words.append(i)

    return same_words

if __name__ == "__main__":
    result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
    result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
    print(result1)
    print(result2)