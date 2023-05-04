def main():
    #  lang = input('Выберите язык')
    text = input()
    morza(text)


def morza(text):
    exceptions = ',.!?@#$%^&8()-_'
    num = '0123456789'
    #  Распаковка файла с алфавитом
    with open('Morse Code_alphabet.txt', 'r') as file:
        dict_lang_m = {}
        file_mor = file.read()

    #  Создание словаря для алфавитов
    for line in file_mor.split(';'):
        key, item = line.split(':')
        dict_lang_m[key] = list(item.split(','))
    num_m = dict_lang_m['num']

    #  колдуем с языками, автоматически находя нам нужный, с помощью аски, и не дай бог первой бдует не буква...

    #  Русский
    if ord(text[0]) in range(1072, 1105):
        need_lang = dict_lang_m['ru']
        with open('Ru_alphabet.txt', 'r', encoding='utf-8') as file_ru:
            alfb = file_ru.read().split()
    #  Англиский
    elif ord(text[0]) in range(97, 124):
        need_lang = dict_lang_m['en']
        #  Englisha нет
        #with open('Ru_alphabet.txt', 'r', encoding='utf-8') as file_en:
           # alfb = file_en.read().split()
    text_main = text

    #  поиск нужных символов, нужно явно чуточку переделать
    try:
        for letter in text_main:
            if letter in alfb:
                print(' ', need_lang[alfb.index(letter)], end='')
            elif letter in num:
                print(num_m[num.index(letter)], end=' ')
            elif letter in exceptions:
                print(letter, end=' ')
            else:
                print('/', end=' ')
    except Exception:
        print("-> Ти Путин!")


def en_t():
    pass


def ru_t():
    pass


if __name__ == '__main__':
    main()
