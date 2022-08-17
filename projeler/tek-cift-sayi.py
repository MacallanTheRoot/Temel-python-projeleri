#Tek Çift Sayı Uygulaması Macallantheroot


def main():
    while True:
        num = input("[1-1000] Arasında bir değer giriniz: ")
        num = isnum_1_1000(num)
        if num:
            sonuc = "Bu bir "
            sonuc = "çift" if num%2 == 0 else "tek"
            seguir = input(sonuc + " sayı!\nDevam etmek ister misiniz? [y/n]: ")
            if seguir.lower() == 'n':
                print("Yine bekleriz!")
                break
        else:
            print("1 ile 1000 arasında bir sayı girmeniz gerekiyor")

def isnum_1_1000(n):
    if n.isdigit():
        n = int(n)
        if 1 <= n <= 1000:
            return n
    return None

if __name__ == "__main__":
    main()





#Tüm sosyal medya adreslerime https://beacons.ai/macallantheroot 'den ulaşabilirsiniz.