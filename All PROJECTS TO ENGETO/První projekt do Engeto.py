"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Adam Kušnir
email: adamkushnir@outlook.cz
discord: Adam K. ASYPRO_AK#2480
"""
text = {1: '''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
2: '''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
3: '''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
}
dash = ("-" * 40)
star = "*"
dash1 = "|"

word = []
indexLetter = 0
UpperLatter = 0
LowLetter = 0
titlecase = 0
UppercaseWords = 0
LowWords = 0

numbersList = []
numbers = ''
num_list = []

IndexWorlds = []

SequenceOfNumbers = 1
LenWords = 0

LenWordList = []
FinishLIST1 = []
FinishLIST2 = []


USERS = {"bob":"123","ann":"pass123", "mike":"password123","liz":"pass123"}

userName = input("Username: ")
if not userName in USERS.keys():
    print("unregistered user.")
    quit()

Password = input("Password: ")
if Password != USERS[userName]:
    print("wrong password, try again")
    quit()

print(dash)
print("Welcome to the app,", userName)
print("We have 3 texts to be analyzed.")
print(dash)


TextNumber = int (input("Enter a number btw. 1 and 3 to select: "))

for words in text[TextNumber].split():
    word.append (words.lower())
    IndexWorlds.append (len(words))
    if words.isnumeric():
        num_list.append(int(words))
        suma = sum(num_list)

    
    for letter in words.strip(",.:;'/\|<>^=0123456789"):
        if letter == letter.upper():
            if indexLetter == 0:titlecase += 1
            
            UpperLatter += 1

        elif letter == letter.lower():
          LowLetter += 1

        indexLetter += 1
    
    if UpperLatter == indexLetter and indexLetter != 0:
        UppercaseWords += 1
    elif LowLetter == indexLetter and indexLetter != 0:
        LowWords += 1

# kazde nove slovo vynuluje a zacne index pocitat znova, patri to k for letter
    indexLetter = 0
    LowLetter = 0
    UpperLatter = 0

print(dash)
print(f"There are {len(word)} words in the selected text.")
print(f"There are {titlecase} titlecase words.")
print(f"There are {UppercaseWords} uppercase words.")
print(f"There are {LowWords} lowercase words.")
print(f"There are {len(num_list)} numeric strings.")
print(f"The sum of all the numbers {suma}")
print(dash)
print("""LEN|  OCCURENCES         |NR.""")

IndexWorlds.sort()

for number1 in IndexWorlds:
    if number1 == SequenceOfNumbers:
        LenWords += 1
    else:
        FinishLIST1.append(SequenceOfNumbers)
        FinishLIST2.append(LenWords)
        LenWords = 0
        SequenceOfNumbers += 1

        if number1 == SequenceOfNumbers:
            LenWords += 1

FinishLIST1.append(SequenceOfNumbers)
FinishLIST2.append(LenWords)

for alignment in range(len(FinishLIST1)):
    alignment_FinishLIST2 = FinishLIST2[alignment]
    print(f"{FinishLIST1[alignment]:<{2}} | {alignment_FinishLIST2 * star:<{20}}|{FinishLIST2[alignment]:>{0}} ")


