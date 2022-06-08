import random

uniquesymbols=dict()
symbols = list()


#User inputs amount of words he will give
while True:
    wordsnum = input("How many words will i take for password? ")

    #Input check
    if wordsnum.isdigit() and wordsnum!='0':
        break
    print("Incorrect input, try again!")


print(f"Enter your {wordsnum} word(s) now")

#User enters words
for counter in range(int(wordsnum)):
    word = input(f"Word {counter+1}: ")
    
    #Input checking
    if word.isalpha():
        for char in word:
            uniquesymbols[char]=0

        symbols = symbols+[*word]
    else:
        print("Your word must contain only letters!")


#User inputs amount of possible symbols repeatings (maximum amount of one symbol in password)
while True:
    repeat = input("How many MAXIMUM symbols repeating do you want? ")

    #Input check
    if repeat.isdigit() and repeat!='0':
        break
    print("Incorrect input, try again!")



password = str()

#Password generation
while len(password) < 8 or not set(uniquesymbols.keys()).issubset(set(password)):
    symbol = symbols[random.randint(0, len(symbols) - 1)]
    if uniquesymbols[symbol] < int(repeat):
        uniquesymbols[symbol] +=1
        password = password + symbol

print(f"""Your password is ready, here it is "{password}"\nDon't show it anyone =)""")
