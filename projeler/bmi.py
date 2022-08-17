#BMI (boy kilo endeksi) Uygulaması Macallantheroot


boy = float(input("Boyunuzu giriniz: "))
kilo = float(input("Kilonuzu giriniz: "))
endeks = kilo/(boy**2)

if(endeks<=18.49):
    print("Boy - Kilo Endeks Sonucu: ",endeks,"(Zayıf)")
    
elif((18.49<endeks) and (endeks<25)):
    print("Boy - Kilo Endeks Sonucu: ",endeks,"(İdeal)")
    
elif(endeks>=25):
    print("Boy - Kilo Endeks Sonucu: ",endeks,"(Obez)")


    

#Tüm sosyal medya adreslerime https://beacons.ai/macallantheroot 'den ulaşabilirsiniz.