# Генератор случайных паролей update_v0.8->1.0
from random import *

#  Внесение требуемых параметров
def mane():
    next = 'д'
    while next == 'д' or next == 'l':
        count = int(input('| Введите количество паролей ->  '))
        length = int(input('| Введите длину пароля ->  '))
        num = input('| Включать ли цифры 0123456789? | д - да, н - нет -> ').lower()
        up = input('| Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? | д - да, н - нет -> ').lower()
        low = input('| Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? | д - да, н - нет ->  ').lower()
        punct = input('| Включать ли символы !#$%&*+-=?@^_?: | д - да, н - нет -> ').lower()
        #  similar_symbols = input('Исключать ли неоднозначные символы il1Lo0O? д - да, н - нет. ').lower()
        chars = ''
        if num == 'д' or num == 'l':
            digits = '0123456789'
            chars += digits
        if low == 'д' or num == 'l':
            lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
            chars += lowercase_letters
        if up == 'д' or num == 'l':
            uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            chars += uppercase_letters
        if punct == 'д' or num == 'l':
            punctuation = '!#$%&*+-=?@^_'
            chars += punctuation
        for i in range(count):
            print('---->', password(length, chars), '<----')
        next = input('| Хотите продолжить? | д - да, н - нет:').lower()
    print('\n...До новых встреч!')

# Создание пароля
def password(length, chars):
    pasw = ''
    for j in range(length):
        pasw += choice(chars)
    return pasw


if __name__ == '__main__':
    mane()

