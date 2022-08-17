#Zar Uygulaması Macallantheroot

import random       


def roll_dice():
    number = random.randint(1,6)
    if number == 1:
        print("-----------")
        print("|         |")
        print("|    0    |")
        print("|         |")
        print("-----------")

    elif number == 2:
        print("-----------")
        print("|         |")
        print("| 0     0 |")
        print("|         |")
        print("-----------")

    elif number == 3:
        print("-----------")
        print("|    0    |")
        print("|    0    |")
        print("|    0    |")
        print("-----------")

    elif number == 4:
        print("-----------")
        print("| 0     0 |")
        print("|         |")
        print("| 0     0 |")
        print("-----------")

    elif number == 5:
        print("-----------")
        print("| 0     0 |")
        print("|    0    |")
        print("| 0     0 |")
        print("-----------")

    elif number == 6:
        print("-----------")
        print("| 0  0  0 |")
        print("|         |")
        print("| 0  0  0 |")
        print("-----------")


print("                         Zar Uygulaması                  ")
x = 'y'
while x.lower() == "y":
    roll_dice()            
    choice = input("Yeniden oynamak ister misiniz? (y/n): ")

    if choice.lower() == "n":
        exit(0)


        #Tüm sosyal medya adreslerime https://beacons.ai/macallantheroot 'den ulaşabilirsiniz.