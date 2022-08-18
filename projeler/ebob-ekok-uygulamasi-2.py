#Adam Asmaca Macallantheroot


birincisayi = int(input("Birinci sayıyıyı giriniz."))
ikincisayi = int(input("İkinci sayıyıyı giriniz."))

if birincisayi > ikincisayi :
    kucuksayi = ikincisayi
else:
    kucuksayi = birincisayi
for i in range(1, kucuksayi+1):
    if(birincisayi % i == 0) and (ikincisayi % i == 0):
        ebob = i
        ekok = (birincisayi * ikincisayi)//ebob
        print("EKOK: " + str(ekok) + "EBOB. " + str(ebob))
        
        
#Tüm sosyal medya adreslerime https://beacons.ai/macallantheroot 'den ulaşabilirsiniz.
