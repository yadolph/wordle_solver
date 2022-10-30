

if __name__ == "__main__":
    lines_lst = []

    with open('russian_nouns.txt', encoding='UTF-8') as f:
        lines = f.read()
        lines_lst = lines.split()

    lines_lst_filtered = [x for x in lines_lst if len(x) == 5]
    letter_frequency = {
        'о': 0.1097,
        'е': 0.0845,
        'а': 0.0801,
        'и': 0.0735,
        'н': 0.0670,
        'т': 0.0626,
        'с': 0.0547,
        'р': 0.0473,
        'в': 0.0454,
        'л': 0.0440,
        'к': 0.0349,
        'м': 0.0321,
        'д': 0.0298,
        'п': 0.0281,
        'у': 0.0262,
        'я': 0.0201,
    }

    all_words_enumerates = {x: 0 for x in lines_lst_filtered}

    for letter, freq in letter_frequency.items():
        for word in all_words_enumerates.keys():
            if letter in word:
                all_words_enumerates[word] += freq

    all_words_enumerates = {k:round(v, 4) for k,v in all_words_enumerates.items()}

    word_rating = {k:v for k,v in sorted(all_words_enumerates.items(), key=lambda item: item[1])}

    print(word_rating)
