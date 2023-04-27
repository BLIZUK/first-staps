def main():
    rus_upper = [chr(i) for i in range(1040, 1072)]
    rus_lover = [chr(i) for i in range(1072, 1104)]

    en_upper = [chr(i) for i in range(65, 91)]
    en_lover = [chr(i) for i in range(97, 123)]
    text = input().lower()
    key = 3
    print(encoder(text, en_lover))
    #  print(*rus_lover, sep='\n')


def encoder(text, en_lover):
    key = 3
    text_output = ''
    for letter in text:
        if letter in en_lover:
            text_output += lambda let: chr(ord(letter) + 3)
    return text_output


def decoder():
    pass


if __name__ == '__main__':
    main()
    
