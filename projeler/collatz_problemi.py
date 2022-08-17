#Collatz Problemi Macallantheroot

# Collatz problemi https://tr.wikipedia.org/wiki/Collatz_san%C4%B1s%C4%B1


import sys


def main():
    print('Collatz Problemi', '-' * 17, sep='\n')
    while True:
        try:
            sayı = int(input('Bir pozitif tam sayı giriniz: '))
            if sayı < 1:
                print('Pozitif bir değer vermelisiniz.')
                continue
        except:
            print('Pozitif bir tam sayı vermelisiniz.')
            continue

        adımlar = 0
        while True:
            n = collatz(sayı)
            if n > 1:
                print(n, end=' -> ')
            else:
                print(n)
            sayı = n
            adımlar += 1
            if sayı == 1:
                break

        print('\nToplam adım:', adımlar)
        continue_ = input('\Yeniden denemek ister misiniz? [evet :y hayır: n] ')
        if continue_.lower() == 'n':
            print('\Bir daha bekleriz!')
            sys.exit()

def collatz(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1

if __name__ == '__main__':
    main()



#Tüm sosyal medya adreslerime https://beacons.ai/macallantheroot 'den ulaşabilirsiniz.