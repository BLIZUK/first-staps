#  binary_code_v1.0
#  Калькулятор двоичного кода (Туда-сюда)
#  Расширил его до взаимообратного
#  !!! Научить его работать с дробными сислами и словами !!!

#  Основная функция
def main():
    print("| Вас приветствует binary_calculator_v1.0")
    while True:
        counting_system = input('| Введите систему исчисления: ->10<- -- десятичная; ->2<- -- двоичная: ').lower()
        #  Проверка на ввод необрабатываемых значений
        if counting_system[0] in '1234567890':
            if int(counting_system) != 10 and int(counting_system) != 2:
                if counting_system != 'десятичная' and counting_system != 'двоичная':
                    print('!!! Ввод неверной системы счисления !!!')
                    continue
        else:
            if counting_system != 'десятичная' and counting_system != 'двоичная':
                print('!!! Ввод неверной системы счисления !!!')
                continue
        check = 'д'
        #  Проверка на продолжение работы в приделах одной системы
        while check == 'д' or check == 'l':
            #  Вызов функции перевода 10-ки в 2-ку
            if counting_system == '10':
                print("-->", ten_two())
                check = input('| Продолжить? | д / l - да, н / y - нет, c - смена системы исчисления --> ').lower()
            #  Вызов функции перевода 2-ки в 10-ку
            else:
                print("-->", two_ten())
                check = input('| Продолжить? | д / l - да, н / y - нет, c - смена системы исчисления --> ').lower()
        #  Проверка на завершение работы программы
        if check == 'н' or check == 'y':
            print('... До новых встреч!')
            break
        #  Проверка на смену системы исчисления
        elif check == 'c' or check == 'с':
            continue


#  Перевод из 10-ой в 2-ую
def ten_two():
    num_input = int(input("| Введите число: "))
    num_reverse = ''
    num_output = ''
    while num_input > 0:
        num_reverse += str(num_input % 2)
        num_input = num_input // 2
    #  Число получется перевернутым, этот цикл его разворачивает в нормальное положение
    for i in range(len(num_reverse) - 1, 0 - 1, -1):
        num_output += num_reverse[i]
    return num_output


#  Перевод из 2-ой в 10-ую
def two_ten():
    num_input = input("| Введите число: ")
    num_output = []
    for count in range(len(num_input)):
        #  Формула перевода в 10-ку:  число[i] x 2^(количество цифр в числе(на 1 меньше) по убыванию до 0 )
        num_output.append(int(num_input[count]) * (2 ** (len(num_input) - (count + 1))))
    return sum(num_output)


if __name__ == '__main__':
    main()
