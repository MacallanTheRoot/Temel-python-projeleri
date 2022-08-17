#Sayı Tahmini Uygulaması Macallantheroot


from random import randint
rand = randint(1, 100)
sayac = 0
 
while True:
    sayac += 1
    sayi = int(input("1 ile 100 arasında bir değer giriniz (çıkış için 0):"))
    if(sayi == 0):
        print("Yine bekleriz!")
        break
    elif sayi < rand:
        print("Daha Yüksek Bir Sayı Girin.")
        continue
    elif sayi > rand:
        print("Daha Düşük Bir Sayı Girin.")
        continue
    else:
        print("Rastele seçilen sayı:",rand )
        print("Tahmin sayınız:",sayac)



        #Tüm sosyal medya adreslerime https://beacons.ai/macallantheroot 'den ulaşabilirsiniz.