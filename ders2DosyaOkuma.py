file=open("c:/users/lenovo/desktop/newfile.txt","r",encoding="utf-8") #turkce karakter encoding eklendi.

#dosya okumak icin 1.yontem

for i in file:
    print(i)

#file.close()

#dosya okumak icin 2.yontem

icerik=file.read()
print(icerik)
file.close()

file2=open("c:/users/lenovo/desktop/newfile2.txt","r",encoding="utf-8")
icerik2=file2.read(4) #ilk 4 karakter okundu.
print(icerik2)
file2.close()

file3=open("c:/users/lenovo/desktop/newfile3.txt","a",encoding="utf-8")

file3.write("\nayse\n")
file3.write("\nfatma\n")
file3.write("\nada\n")
file3.close()
file3=open("c:/users/lenovo/desktop/newfile3.txt","r",encoding="utf-8")
icerik3=file3.read()
print(icerik3)
file3.close()

file3=open("c:/users/lenovo/desktop/newfile3.txt","r",encoding="utf-8")
icerik4=file3.readline() #tek satirda okuma yapar.
print(icerik4)
file3.close()


file3=open("c:/users/lenovo/desktop/newfile3.txt","r",encoding="utf-8")
icerik5=file3.readlines() #verileri tek tek indeks olarak listeye ekler
print(icerik5)
icerik6=icerik5[0]
print(icerik6)
file3.close()
