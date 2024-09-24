#dosya acmak ve olusturmak icin open() fonksiyonu kullanilir.
#kulanimi: open(dosyaAdi,dosyaErismeModu)
#dosyaErismeModu->dosyayi hangi amacl actigimizi belirtir.

#"w": (write) yazma modu. dosyayı konumda olusturur.
file=open("newfile.txt","w") #newfile.txt dosyası .py programinin oldugu klasorde olusturuldu.
## dosya icerigini siler ve yeniden yazar.
file.close() #dosyayi actiktan sonra kapatmak lazim.


file2=open("c:/users/lenovo/desktop/newfile.txt","w") #masaustunde dosya olusturuldu.
file2.write("ahmet yilmaz ayse")
file2.close()

#"a": (append) ekleme modu. dosya konumda yoksa olustur.

file3=open("c:/users/lenovo/desktop/newfile2.txt","a")
file3.write("\nahmet ahmet\n")
file3.close()

#"x": (create) olusturma modu. dosya zaten varsa hata verir.

file4=open("c:/users/lenovo/desktop/newfile2.txt","x")
file4.close()
    