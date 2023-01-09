print("*** ИГРЫ С ЧИСЛАМИ ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = (abs(int(input("Введите целое число => ")))) #Lisatud paar sulgu, mis puudusid
        break
    except ValueError:
         print("Это не целое число")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Нет смысла ничего делать с нулём")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Определяем, сколько в числе чётных и сколько нечётных цифр")
    print()
    c=b=a
    paaris=0
    paaritu=0
    #eemaldas topelt võrdse ja jättis tavapärase võrdusseisu
    while b > 0: #kooloni asemel semikoolon
            if b % 2 == 0: #asendas võrrandi kontrolliga, kas osad on võrdsed
                    paaris += 1
            else:
                    paaritu += 1
                    #ümber korraldatud pluss
            b = b // 10 #b on lisaruumi
  
    print("Чётных цифр:",paaris)
    print("Нечётных цифр:",paaritu)
    #teksti järel ei olnud koma, nii et trükis oli muutuja
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Переворачиваем* введённое число")
    print()
    b=0
    while a > 0: #puudu semikoolon
        number = a % 10
        a = a // 10
        b = b * 10
        b +=number #b-l on lisaruum ja pluss on ümber paigutatud
    print("*Перевёрнутое* число", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Проверяем гипотезу Сиракуз") #lisasulgud
    print()
    if c % 2 == 0: #selle asemel, et kontrollida, kas mõlemad osad on võrdsed, oli võrrand
        print("с - чётное число. Делим на 2.")
    else:
        print("с - нечётное число. Умножаем на 3, прибавляем 1 и делим на 2.")
    while c != 1:
            if c % 2 == 0: #selle asemel, et kontrollida, kas mõlemad osad on võrdsed, oli võrrand
                    c = c / 2 #eemaldati võrdsuse kontroll ja määrati võrdsus
            else:
                    c = (3*c + 1) / 2 #eemaldati võrdsuse kontroll ja määrati võrdsus
            print(round(c), end=" ") #teine ​​tsitaat jäeti välja
    print()
    print("Гипотеза верна") #erinevad tsitaadid
