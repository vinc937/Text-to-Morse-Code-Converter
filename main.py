morse_code_dict = {
    'A': '.-', 'Ä': '.-.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'Ö': '---.', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'Ü': '..--',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '\'': '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}


def convert_txt_to_morse(text):
    morse_code = ""
    text = text.upper()
    for char in text:
        if char == " ":
            morse_code += "  "
            continue
        if char not in morse_code_dict:
            return False
        morse_code += f"{morse_code_dict[char]} "
    return morse_code


print("Hello and welcome to Text to Morse Code Converter.")
while True:
    user_text = input("Write the text you want to be converted to morse code: ")

    result = convert_txt_to_morse(user_text)
    if not result:
        print("\nYou used a character that is not used in Morse Code. Please try again.")
        continue

    print("\nYour morse code is:", result)

    convert_again = input("\nWould you like to convert a new text? (Y/N): ").lower()
    if convert_again in ["y", "yes"]:
        continue
    else:
        print("Goodbye.")
        break
