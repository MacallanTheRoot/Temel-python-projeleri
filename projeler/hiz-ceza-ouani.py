#Hızla ceza puanı alma uygulaması Macallantheroot


cezapuani = 0
i = 1
while i == 1:
    hiz = int(input("Hızınızı Girin: "))
    if hiz > 120 :
        cezapuani += 4
        print("Ceza puanınınza 4 puan eklenmiştir")
    elif hiz > 100:
        cezapuani += 2
        print("Ceza puanınınza 2 puan eklenmiştir")
    if cezapuani > 6 :
        print("Ceza Puanınınz 6 olmuştur ve")
        print("Ehliyetinize el konulmuştur.")
        break
        
        #Tüm sosyal medya adreslerime https://beacons.ai/macallantheroot 'den ulaşabilirsiniz.
