#Yaşam Süresi Uygulaması Macallantheroot

from datetime import *
dogumtarihi = datetime.strptime(input("Doğum Tarihinizi Giriniz (GÜN.AY.YIL): "),"%d.%m.%Y")
sure = datetime.now() - dogumtarihi

print("Sen {} saniye yaşadın.".format(sure.total_seconds()))




#Tüm sosyal medya adreslerime https://beacons.ai/macallantheroot 'den ulaşabilirsiniz.