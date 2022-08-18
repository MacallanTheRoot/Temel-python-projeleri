# Ebob Ekok Uygulaması Macallantheroot

def ebob_bulma(sayı1 , sayı2):
    i = 1
    ebob = 1
    while (i <= sayı1 and i <= sayı2):
        if not sayı1 % i and not sayı2 % i :
            ebob = i
        i += 1

    return ebob

def ekok_bulma(sayı1, sayı2):
    return sayı1 * sayı2 / ebob_bulma(sayı1,sayı2)

sayı1 = int(input("Sayı1: "))
sayı2 = int(input("Sayı2: "))

print("Ebob: ",ebob_bulma(sayı1,sayı2))
print("Ekok: ",ekok_bulma(sayı1,sayı2))

#Tüm sosyal medya adreslerime https://beacons.ai/macallantheroot 'den ulaşabilirsiniz.
