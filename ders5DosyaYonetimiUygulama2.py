import re

class bilgiIslem:
    def __init__(self,kullaniciGirisi):
        if(len(kullaniciGirisi)<1):
            raise Exception('girilen deger 1 karakterden kucuk olamaz')
        elif (len(kullaniciGirisi)>1):
             raise Exception('girilen deger 1 karakterden buyuk olamaz')
        elif  re.search("[a-z]",kullaniciGirisi):
             raise Exception("girilen deger sayi icermeli")
        elif(kullaniciGirisi==' '):
            print('lutfen bosluklu karakter kullanmayiniz')
        else:
            self.kullaniciGirisi=kullaniciGirisi
            if (self.kullaniciGirisi=='1'):
                 kisiBilgisiGoster()
            elif (self.kullaniciGirisi=='2'):
                 kisiBilgisiGir()
            else:
                 print('hatali giris yaptiniz')
                 
def kisiBilgisiGir():
        kisiAdi=input('kisi ismini giriniz: ')
        kisiSoyadi=input('kisi soyismini giriniz: ')
        kisiIkametgahi=input('kisi ikametgahini giriniz: ')
        kisiYasi=input('kisi yasini giriniz: ')
        with open("kisi_bilgileri.txt","a",encoding="utf-8") as file:
            file.write(kisiAdi+','+kisiSoyadi+','+kisiIkametgahi+','+kisiYasi+'\n')

def kisiBilgisiGoster():
        with open("kisi_bilgileri.txt","r",encoding="utf-8") as file:
           data=file.readlines()
           for line in data:
                line=line[:-1]
                info=line.split(',')
                isim=info[0]
                soyisim=info[1]
                sehir=info[2]
                yas=info[3]
                print(isim,soyisim,sehir,yas)      

while True:
    try:
        kullaniciGirisi=input('islem secimi yapiniz:\n1-Bilgileri goster\n2-Bilgileri gir\n3-Cikis yap.\n')
        bilgiIslem(kullaniciGirisi)
    except Exception as error:
        print(error)
        continue
    else:
        print('islem basarili sekilde gerceklesti.')
    finally:
        print('islem yapildi.')