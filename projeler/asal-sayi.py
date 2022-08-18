#Asal Sayı Bulucu Uygulaması Macallantheroot 


sayi=int(input("Sayıyı Girin : "))
if sayi > 1:
   
   for i in range(2,sayi):
       if (sayi % i) == 0:
           print(sayi," Asal Sayı Değildir.")
           break
   else:
       print(sayi," Asal Sayıdır.")

else:
   print(sayi," Asal Sayı Değildir.")

#Tüm sosyal medya adreslerime https://beacons.ai/macallantheroot 'den ulaşabilirsiniz.
