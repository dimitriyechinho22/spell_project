import re
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


def reading(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        words_dict = {}
        for line in lines:
            if ':' in line:
                key, value = line.split(':', 1)
                words_dict[key.strip()] = value.strip()
        return words_dict


def reviewing(path):
    main_dict = reading(path=path)
    user_input = input('Введите сообщение: ')
    user_input = re.sub(r'[^\w\s]', '', user_input.lower())
    match_ratio = 70
    matched_keys = []
    for key in main_dict.keys():
        ratio = fuzz.ratio(user_input, key.lower())
        if ratio >= match_ratio:
            matched_keys.append(key)
    if matched_keys:
        matched_key = process.extractOne(user_input, matched_keys)[0]
        print(main_dict[matched_key])
    else:
        with open(path, 'a', encoding='utf-8') as file:
            file.write(f'\n{user_input}: ')
        print('Ответ не найден, но добавлен в словарь.')


reviewing('text')


