#Whatsapp Mesaj Uygulaması Macallantheroot


#çalıştırmadan önce aşşağıdaki yorum satırındaki kodu komut istemcisi/terminalinize yapzın 
#pip install pywhatkit

import pywhatkit
import datetime

num = input("Gönderenin WhatsApp Numarasını Girin (Ülke Kodu ile beraber +90) : ")
msg = input("Mesajınızı Girin : ")
time = input("Tarihini girin (HH:MM): ")
if len(time) != 5:
    print("Geçersiz. Lütfen fazladan boşluk bırakmadan HH: MM formatının takip edildiğinden emin olun (yalnızca 5 karakter dahil)")
    exit(1)
h = int(time[0]+time[1])
m = int(time[3]+time[4])
if (h<0 or h>23):
    print("Geçersiz")
    exit(1)
if (m<0 or m>59):
    print("Geçersiz")
    exit(1)

pywhatkit.sendwhatmsg(f"{num}", f"{msg}", h, m)






#Tüm sosyal medya adreslerime https://beacons.ai/macallantheroot 'den ulaşabilirsiniz.