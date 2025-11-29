import math

def hesap_makinesi():

    print("-----HESAP MAKİNESİ-----")
    print("Hoşgeldiniz, lütfen yapmak istediğiniz işlemi seçiniz:")
    print("1-Toplama")
    print("2-Çıkarma")
    print("3-Çarpma")
    print("4-Bölme")
    print("5-Üst alma")
    print("6-Mod alma")
    print("7-Karekök alma")
    print("8-Mutlak değer")
    print("9-Faktöriyel")
    print("----------------------")

    x = int(input("Kullanıcı x değerini girsin: "))

  
    sonuc = None

    if x == 1:
        print("\n>>>Toplama işlemi seçildi.")
        a = float(input("a sayısını giriniz: "))
        b = float(input("b sayısını giriniz: "))
        sonuc = a + b

    elif x == 2:
        print("\n>>>Çıkarma işlemi seçildi.")
        a = float(input("a sayısını giriniz: "))
        b = float(input("b sayısını giriniz: "))
        sonuc = a - b

    elif x == 3:
        print("\n>>>Çarpma işlemi seçildi.")
        a = float(input("a sayısını giriniz: "))
        b = float(input("b sayısını giriniz: "))
        sonuc = a * b

    elif x == 4:
        print("\n>>>Bölme işlemi seçildi.")
        a = float(input("a sayısını giriniz: "))
        b = float(input("b sayısını giriniz: "))
        if b == 0:
            print("!HATA: 0'a bölme yapılamaz.")
        else:
            sonuc = a / b

    elif x == 5:
        print("\n>>>Üst alma işlemi seçildi.")
        a = float(input("a sayısını giriniz: "))
        b = float(input("b sayısını giriniz: "))
        sonuc = a ** b

    elif x == 6:
        print("\n>>>Mod alma işlemi seçildi.")
        a = float(input("a sayısını giriniz: "))
        b = float(input("b sayısını giriniz: "))
        sonuc = a % b

    elif x == 7:
        print("\n>>>Karekök alma işlemi seçildi.")
        a = float(input("a sayısını giriniz: "))
        sonuc = math.sqrt(a)

    elif x == 8:
        print("\n>>>Mutlak değer işlemi seçildi.")
        a = float(input("a sayısını giriniz: "))
        sonuc = abs(a)

    elif x == 9:
        print("\n>>>Faktöriyel işlemi seçildi.")
        a = int(input("a sayısını giriniz: "))
        if a < 0:
            print("!HATA: Negatif sayının faktöriyeli yok.")
        else:
            sonuc = math.factorial(a)

    else:
        print("Hatalı işlem seçtiniz.")

    print("\nSONUÇ:", sonuc)

    
    tekrar = input("\nYeni bir işlem yapmak ister misiniz? (e/h): ")
    if tekrar.lower() == "e":
        hesap_makinesi()
    else:
        print("Program sonlandırıldı.")


hesap_makinesi()
