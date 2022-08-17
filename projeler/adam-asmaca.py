#Adam Asmaca Macallantheroot

import random

def hangman():
    kelime = random.choice(["kalem","elbise","asker","süpermen","robot","telefon","bilgisayar","kitap","insan","hayvan"])
    # print(kelime)
    alfabe = "abcçdefgğhiıjklmnoöprsştuüvyz"
    chance = 10
    misafir_made = ""

    while len(kelime) > 0:
        main = ""
        for harf in kelime:
            if harf in misafir_made:
                main += harf
            else:
                main = main +"_"+" "

        if main == kelime:
            print("Cevap: "+ main)
            print("Kazandın! ")
            break

        misafir = input("Kelimeyi Tahmin Et! "+ main)

        if misafir in alfabe:
            misafir_made = misafir_made + misafir
        else:
            misafir = input("Geçerli karakteri girin: ")

        if misafir not in kelime:
            chance -= 1

            if chance == 9:
                print("9 hakkın kaldı")
                print("\n---------------------------- ")

            if chance == 8:
                print("9 hakkın kaldı")
                print("\n---------------------------- ")
                print("      O     ")
            if chance == 7:
                print("7 hakkın kaldı")
                print("\n---------------------------- ")
                print("      O     ")
                print("      |      ")
            if chance == 6:
                print("6 hakkın kaldı")
                print("\n---------------------------- ")
                print("      O     ")
                print("      |      ")
                print("     /       ")
            if chance == 5:
                print("5 hakkın kaldı")
                print("\n---------------------------- ")
                print("      O     ")
                print("      |      ")
                print("     / \     ")
            if chance == 4:
                print("4 hakkın kaldı")
                print("\n---------------------------- ")
                print("     \O     ")
                print("      |      ")
                print("     / \     ")
            if chance == 3:
                print("3 hakkın kaldı")
                print("\n---------------------------- ")
                print("     \O/   ")
                print("      |      ")
                print("     / \     ")
            if chance == 2:
                print("2 hakkın kaldı")
                print("\n---------------------------- ")
                print("     \O/  |  ")
                print("      |      ")
                print("     / \     ")
            if chance == 1:
                print("1 hakkın kaldı")
                print("Son hakkın...")
                print("\n---------------------------- ")
                print("     \O/ __|  ")
                print("      |      ")
                print("     / \     ")

            if chance == 0:
                print("Öldü")
                print("Oyun bitti.")
                print("      O____|  ")
                print("     /|\      ")
                print("     / \     ")

                break



name = input("Hoş Geldin! İsmin ne?: ")
print(name+" Hadi oyun oynayalım!")
print("\n--------------------------------------\n")
hangman()

#Tüm sosyal medya adreslerime https://beacons.ai/macallantheroot 'den ulaşabilirsiniz.
