#  Генератор случайных чисел. Угадайка_v1.2
from random import randint
from colorama import init
from colorama import Fore, Back, Style

init()
print(Fore.GREEN)


def choice_lvl():  #  выбор уровня сложности: задаем нужный диапазон
    print("1-Легкий", "2-Нормальный", "3-Сложный", '4-НУ ОЧЕНЬ СЛОЖНЫЙ  ' + Fore.RED + " 5-Самоубийство" + Fore.GREEN)
    a = input('Выберите уровень сложности:')
    for i in range(len(a)):
        if a[i] not in '1234567890':
            print(Fore.RED + 'Тут должна была быть ошибка, ведь ты ввел не правильные значения.')
            print(Fore.GREEN + 'ВВЕДИ ЧИСЛО ВКЛЮЧИТЕЛЬНО С 1 ДО 5, ( 1,2,3,4,5 )  -->')
            return choice_lvl()
        if int(a) in range(1, 6):
            continue
        print('Выбор состоит только из этих вариантов: 1, 2, 3, 4, 5 ')
        return choice_lvl()
    a = int(a)
    return a
    
    
def randomizer():  #  создание загаданного числа в заданном диапазоне 
    lvls = [10, 100, 1000, 9999, 1000001]
    result = str(randint(1, lvls[select_lvl - 1] + 1))
    return result


print('Приветствую тебя, я - УГАДАЙКА(M. род.). Сможешь ли ты отгдать задуманное мной число? ')
ask = input('Если да, то напиши - Y: ')
if ask.lower() != 'y':  # проверка на продолжение программы, если ответ 'n' - программа завершается
    print('Я пошутил, выбора у тебя тут НЕТ.  "ХА-ХА-ХА" (иронично-роботический смех) ')
ask = 'y'
while True:  #  проверки введеных нами чисел до победного
    if ask == 'y':
        select_lvl = choice_lvl()
        rand_num = randomizer()
        count = 0
        while True:
            num = input('Скажи число: ')
            count += 1
            if num == rand_num and count == 1:
                print("Ты отгадал с первого раза!!!", "ПОЗДРАВЛЯЮ!!! GODLIKE")
                print('Это и правда большая редкость, если чисел в списке больше 10...')
                ask = input("загадываем новое число? 'Y' - да, 'N' - нет. Тут выбор и правда настоящий  ")
                if ask.lower() == 'y':
                    break                    
            elif num == rand_num:
                print('Отлично', 'Попыток потребовалось всего : ' + Fore.RED + str(count) + Fore.GREEN + '.', sep='\n')
                ask = input("Хочешь новое число? 'Y' - да, 'N' - нет. Выбор тут очевиден  ")
                break              
            elif num != rand_num:
                print(Fore.RED + 'НЕ верно ' + Fore.GREEN)
                if num > rand_num:
                    print('Число будет чуть поменьше)')
                elif num < rand_num:
                    print('Число будет побольше')
    elif ask.lower() == 'n':
        print('До новых встреч!')
        break
    else:
        print(Fore.RED + 'Ай-АЙ-АЙ' + ' что за девиантное поведение?, ВАШ РАЗРАБОТЧИК ЯВНО ОСТАВИЛ МНОГО БАГОВ.')
        ask = input(Fore.GREEN + 'Выбор тут Y or N, третьего не дано! Выбор:  ')
input()
