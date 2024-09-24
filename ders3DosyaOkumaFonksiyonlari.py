with open("c:/users/lenovo/desktop/dosya.txt","r",encoding="utf-8") as file:
    content=file.read()
    print(content)
    print(file.tell()) #cursor konumunu gosterir
    file.seek(15)
    print(file.tell())
