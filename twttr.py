def main():
    text = input("Input: ")
    strip_vowels(text)

def strip_vowels(text):
    result = ""             #creates final answer and initializes it as blank
    for letter in text:     #iterate over every letter in the string
        letter.lower()
        if (letter == "a") or (letter == "e") or (letter == "i") or  (letter == "o") or (letter == "u"):            #checks to see if letter is a lower-case vowel
            removed_letter = letter.replace(letter, "")                                                             #if yes, replace letter with "" (removes letter)
            result += removed_letter
        elif (letter == "A") or (letter == "E") or (letter == "I") or  (letter == "O") or (letter == "U"):          #checks to see if letter is an upper-case vowel
            removed_letter = letter.replace(letter, "")                                                             #if yes, replace letter with "" (removes letter)
            result += removed_letter
        else:
            result += letter
    print(f"{result}")

main()
