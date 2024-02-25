String = 'restart'
# print('restart'.replace('r', '$'))
def dolapo(words: str):
    first_letter = words[0]
    words = words.replace(first_letter, "$")
    return first_letter + words[1:]
