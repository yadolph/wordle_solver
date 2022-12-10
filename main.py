import re


def create_word_lst(filename):
    lines_lst = []
    with open(filename, encoding='UTF-8') as f:
        lines = f.read()
        lines_lst = lines.split()
    return [x for x in lines_lst if len(x) == 5]


def game_solver(all_words):
    excl = list(input('Исключения без пробелов:'))
    incl = list(input('Буквы в наличии без пробелов:'))
    corr_mask = list(input('Маска слова с * вместо неизвестных:'))
    wrong_mask = list(input('Маска исключений:'))

    lst_to_excl = []

    for letter in excl:
        lst_to_excl.extend([x for x in all_words if letter in x])
    lst_to_excl = list(set(lst_to_excl))

    lst_after_excl = [x for x in all_words if not x in lst_to_excl]

    lst_after_incl = []
    for word in lst_after_excl:
        if all([char in word for char in incl]):
            lst_after_incl.append(word)

    word_enumerates = {x:0 for x in lst_after_incl}
    words_candidates = []
    corr_mask_letters = [x for x in corr_mask if x != '*']

    for position, symbol in enumerate(corr_mask):
        if not corr_mask_letters:
            words_candidates = lst_after_incl
            break
        if symbol == '*':
            continue
        
        for word in lst_after_incl:
            if re.search(symbol, word[position], re.I):
                word_enumerates[word] += 1
        
        for word, freq in word_enumerates.items():
            if freq == len(corr_mask_letters):
                words_candidates.append(word)
    
    for position, symbol in enumerate(wrong_mask):
        if wrong_mask == ['*','*','*','*','*']:
            break
        if symbol == '*':
            continue
        words_candidates = [
            x for x in words_candidates if not re.search(symbol, x[position], re.I)
        ]

    return(words_candidates)


if __name__ == '__main__':
    all_words = create_word_lst('russian_nouns.txt')
    print('Введите слово "ОСИНА"')
    while True:
        print(game_solver(all_words))