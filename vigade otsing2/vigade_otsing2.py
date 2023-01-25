##1
#print("1 Harjutus")
#print()
#a=0
#nimi_list=[] #Создание списка для будущего использования
#for i in range(5):
#    nimi=input("Kirjuta nimi ").title()
#    while nimi.isalpha()==False:
#        nimi=input("Kirjuta õige nimi ")
#    nimi_list.append(nimi) #.append() В конец списка добавляется элемент, в данном случае введеная переменная добавляется в конец списка
#nimi_list.sort() #.sort() Сортировка списка в порядка возрастания
#print(nimi_list)
#print("Viimane nimi on ", nimi)
#print()

##2
#print("2 Harjutus")
#print()
#opilased = ["Juhan","Kati","Maarja","Mario","Mati"]
#print(opilased)
#pos=input("Millist positsiooni tahaksid muuta? ")
#while pos.isdigit()==False or int(pos)>5:
#    pos=input("Kirjuta õige number! Millist positsiooni tahaksid muuta? ")
#nimi=input("Kirjuta uus õpilane ")
#while nimi.isalpha()==False:
#    nimi=input("Kirjuta õige nimi ")
#opilased.pop(int(pos)-1) #.pop(n) удаляет n элемент в списке
#opilased.insert(int(pos)-1,nimi) #.insert(i,n) вставляет в i позицию, элемент n
#print(opilased)
#print()

#3
print("3 Harjutus")
print()
opilased = ["Juhan","Kati","Mario","Mario","Mati","Mati"]
for i in range(10):
    for n in range(0,len(opilased)-1):
        if len(opilased)-1!=n and opilased[len(opilased)-1]==opilased[n]:
            opilased.pop(n)
print(opilased)
