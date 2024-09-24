with open("c:/users/lenovo/desktop/dosya.txt","r+",encoding="utf-8") as file:
    print(file.read())


with open("c:/users/lenovo/desktop/dosya.txt","r+",encoding="utf-8") as file:
    file.seek(20) #20.karakterden itibaren yazi eklendi.
    file.write("satir eklendi.")
    

with open("c:/users/lenovo/desktop/dosya.txt","a",encoding="utf-8") as file:
    file.write("satir en sona eklendi.")


with open("c:/users/lenovo/desktop/dosya.txt","r+",encoding="utf-8") as file:
    file.seek(0) # 0.karakterden itibaren yazi eklendi.
    file.write("en sona satir eklendi.")    

with open("c:/users/lenovo/desktop/dosya.txt","r+",encoding="utf-8") as file:
    list=file.readlines() # liste seklinde yazilar okundu
    list.insert(1,"0 ile 1. i indeks arasina yazi eklendi")
    file.seek(0) #cursor en basa geldi
    file.writelines(list)

with open("c:/users/lenovo/desktop/dosya.txt","r+",encoding="utf-8") as file:
    print(file.read())
    