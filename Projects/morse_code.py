def main():
    letters_en = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
    morse_en = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
             '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---',
             '...--', '....-', '.....', '-....', '--...', '---..', '----.']
    morse_slovar = {letters_en[i]: morse_en[i] for i in range(len(letters))}
    text = input().upper().replace(" ", "")
    for i in text:
        if i in letters_en:
            print(morse_slovar[i], end=' ')


if __name__ == "__main__":
    main()
    
