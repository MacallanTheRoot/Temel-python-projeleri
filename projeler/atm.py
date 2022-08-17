#The Bank ATM Uygulaması Macallantheroot

bakiye = 1000;

while True:
    print("----------------------------------")
    print("The Bank ATM'ye Hoşgeldiniz...")
    print("----------------------------------")

    print("Bakiye görüntülemek için lütfen '1' Tuşuna basınız.")
    print("Hesabınıza para çekmek için lütfen '2' Tuşuna basınız.")
    print("Hesabınıza para yatırmak için lütfen '3' Tuşuna basınız.")
    print("ATM'den çıkmak için lütfen '4' Tuşuna basınız.")
    islem = input("Yapmak istediğiniz işlemi seçiniz: ")
    

    if islem == "1":
        print("Bakiyeniz: ", bakiye)
        
    elif islem == "2":
        miktar = int(input("Çekmek istediğiniz miktarı giriniz: "))
        if miktar > bakiye:
            print("Bakiyeniz yetersizdir. Lütfen daha sonra tekrar deneyin.")
        else:
            bakiye -= miktar
            print("Para çekme işlemi başarılı.")
            print("Bakiyeniz: ",bakiye)

    elif islem == "3":
        miktar = int(input("Yatırmak istediğiniz para miktarını giriniz: "))
        bakiye += miktar
        print("Para yatırma işlemi başarılı.")
        print("Hesap Bakiyeniz: ",bakiye)

    elif islem == "4":
        print("Çıkış Yaptınız... Yine Bekleriz.")
        break


    #Tüm sosyal medya adreslerime https://beacons.ai/macallantheroot 'den ulaşabilirsiniz.