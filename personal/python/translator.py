

def translator (word):
    translation = ""
    for letter in word:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translator(input("Enter a phrase: ")))