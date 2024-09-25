def notHesapla(satir):
    satir=satir[:-1] 
    liste=satir.split(':')
    ogrenciAdi=liste[0] 
    ogrenciNotu=liste[1]
    not1=int(ogrenciNotu[:2])
    not2=int(ogrenciNotu[3:6])
    ortalama=(not1+not2)/2
    #print(ortalama)

    if (ortalama<=60):
        print(f'ogrenci {ogrenciAdi} not ortalamasi {ortalama} cc den kucuk, kaldiniz.')
    else:
        print(f'ogrenci {ogrenciAdi} not ortalamasi {ortalama} cc den buyuk, gectiniz')

def notlariOku():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(notHesapla(satir))

def notGir():
    ad=input('ogrenci adi: ')
    soyad=input('ogrenci soyadi: ')
    not1=input('not 1 i giriniz: ')
    not2=input('not 1 i giriniz: ')
    with open("sinav_notlari.txt","a",encoding="utf-8") as file:
        file.write(ad+' '+soyad+':'+not1+','+not2+'\n') # ':' ve',' isaretleri verilere ulasmak icin kullanildi.

while True:
    kullaniciGirisi=input('1-Notlari Oku\n2-Not Gir\n3-Cikis Yap\n')

    if (kullaniciGirisi=='1'):
        notlariOku()
    elif (kullaniciGirisi=='2'):
        notGir()
    elif(kullaniciGirisi=='3'):
        break
    else:
        print('Hatali giris yaptiniz!')