import re


def game_solver(lines_lst_filtered):
    excl = list(input('Исключения без пробелов:'))
    incl = list(input('Буквы в наличии без пробелов:'))
    mask = list(input('Маска слова с * вместо неизвестных:'))
    wrong_mask = list(input('Маска исключений:'))

    lst_to_excl = []

    for word in lines_lst_filtered:
        for letter in excl:
            if letter in word:
                lst_to_excl.append(word)

    lst_after_excl = []
    for word in lines_lst_filtered:
        if not word in lst_to_excl:
            lst_after_excl.append(word)

    lst_after_incl = []
    for word in lst_after_excl:
        counter = 0
        for letter in incl:
            if letter in word:
                counter += 1
        if counter == len(incl):
            lst_after_incl.append(word)

    word_enumerates = {x:0 for x in lst_after_incl}
    words_candidates = []
    mask_letters = [x for x in mask if x != '*']

    for position, symbol in enumerate(mask):
        if mask == ['*','*','*','*','*']:
            words_candidates = lst_after_incl
            break
        if symbol == '*':
            continue
        
        for word in lst_after_incl:
            if re.search(symbol, word[position], re.IGNORECASE):
                word_enumerates[word] += 1
        
        for word, freq in word_enumerates.items():
            if freq == len(mask_letters):
                words_candidates.append(word)
    
    print(wrong_mask)

    for position, symbol in enumerate(wrong_mask):
        if wrong_mask == ['*','*','*','*','*']:
            break
        if symbol == '*':
            continue
        for word in words_candidates:
            if re.search(symbol, word[position], re.IGNORECASE):
                words_candidates.remove(word)

    print(words_candidates)


if __name__ == '__main__':
    lines_lst = []

    with open('russian_nouns.txt', encoding='UTF-8') as f:
        lines = f.read()
        lines_lst = lines.split()

    lines_lst_filtered = [x for x in lines_lst if len(x) == 5]

    print('Введите слово "ОСИНА"')

    while True:
        game_solver(lines_lst_filtered)