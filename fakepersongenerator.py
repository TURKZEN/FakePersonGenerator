import os

if __name__ == "__main__":
    pass
else:
    print("İmport edilemez")
    print("cannot be imported.")
    quit()

os.system('cls' if os.name=='nt' else 'clear')
try:
    from faker import Faker
except:
    print("""
    
    Faker kütüphanesi yüklü değil.Lütfen önce kütüphaneyi yükleyin.
    Faker library is not installed. Please install the library first.

        pip install Faker
    
    """)
    yuklensin_mi = input("Faker Kütüphanesi otomatik yüklensin mi ? (e/h) : ")
    if yuklensin_mi == "e":
        os.system("pip install Faker")
    else:
        print("""
            Faker kütüphanesi yüklü değil.Lütfen önce kütüphaneyi yükleyin.
            Faker library is not installed. Please install the library first.

                pip install Faker
        """)
        quit()

print(
"""
  ______    _        _____                           _____                           _             
 |  ____|  | |      |  __ \                         / ____|                         | |            
 | |__ __ _| | _____| |__) |__ _ __ ___  ___  _ __ | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 |  __/ _` | |/ / _ \  ___/ _ \ '__/ __|/ _ \| '_ \| | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | | | (_| |   <  __/ |  |  __/ |  \__ \ (_) | | | | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
 |_|  \__,_|_|\_\___|_|   \___|_|  |___/\___/|_| |_|\_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                            
        Sahte Kimlik Oluşturucu - Fake Person Generator 
                Coder : Batuhan Türkarslan 

Choose a language (Bir Dil Seç) :
 [1]English
 [2]Türkçe 

 [q]Exit (Çıkış)
"""
)
lan = input("Your choose (Seçimin) : ")

if lan =="q":
    print("""
    See you again...
    Tekrar görüşeceğiz...
    """)
# English - Start
elif lan == "1":
    while True:
        cho=input("""
        What language should the fake information be created in?
        [1] English
        [2] Turkish

        Your choose :  """)
        if cho=="1":
            fake = Faker(['en_US'])
            print(
                """
                [1] Fake Name
                [2] Fake Adress
                [3]
                [4]
                [5]
                
                Exit[q]
                """)
            choose = input("Your choose : ")

            if choose == "q":
                print("\nwe'll meet Again...")
                break
            elif choose == "1":
                print("""
-----------------------------------------------------
Fake name created : {0}             
-----------------------------------------------------
                """.format(fake.name()))
                con = input("Do you want to continue (y/n) : ")
                if con == "n":
                    print("\nwe'll meet Again...")
                    break
                elif con == "y":
                    continue
                else:
                    print("""
                    
                    Please make the right choice.
                    (y/n) ---> (yes/no)

                    """)
                    break
            elif choose == "2":
                print("""
-----------------------------------------------------
Fake adress created : 

{0}             
-----------------------------------------------------
                """.format(fake.address()))
                
                con = input("Do you want to continue (y/n) : ")
                if con == "n":
                    print("\nwe'll meet Again...")
                    break
                elif con == "y":
                    continue
                else:
                    print("""
                    
                    Please make the right choice.
                    (y/n) ---> (yes/no)

                    """)
                    break
        elif cho =="2":
            fake = Faker(['tr_TR'])
            print(
                """
                [1] Fake Name
                [2] Fake Adress
                [3]
                [4]
                [5]
                
                Exit[q]
                """)
            choose = input("Your choose : ")

            if choose == "q":
                print("\nwe'll meet Again...")
                break
            elif choose == "1":
                print("""
-----------------------------------------------------
Fake name created : {0}             
-----------------------------------------------------
                """.format(fake.name()))
                con = input("Do you want to continue (y/n) : ")
                if con == "n":
                    print("\nwe'll meet Again...")
                    break
                elif con == "y":
                    continue
                else:
                    print("""
                    
                    Please make the right choice.
                    (y/n) ---> (yes/no)

                    """)
                    break
            elif choose == "2":
                print("""
-----------------------------------------------------
Fake adress created : 

{0}             
-----------------------------------------------------
                """.format(fake.address()))
                
                con = input("Do you want to continue (y/n) : ")
                if con == "n":
                    print("\nwe'll meet Again...")
                    break
                elif con == "y":
                    continue
                else:
                    print("""
                    
                    Please make the right choice.
                    (y/n) ---> (yes/no)

                    """)
                    break
        else:
            print("""

        Please make the right choice

        [1] English
        [2] Turkish
            
            """)
            break
#English - End

#Turkish - Start
elif lan == "2":
    while True:
        cho=input("""
        Sahte bilgiler hangi dilde oluşturulsun ? 
        [1] İngilizce
        [2] Türkçe

        Seçimin :  """)
        if cho=="1":
            fake = Faker()
            print(
                """
                [1] Sahte İsim
                [2] Sahte Adres
                [3]
                [4]
                [5]
                
                Çıkış[q]
                """)
            choose = input("Seçimin : ")

            if choose == "q":
                print("\nTekrar görüşeceğiz...")
                break
            elif choose == "1":
                print("""
-----------------------------------------------------
Sahte isim oluşturuldu : {0}             
-----------------------------------------------------
                """.format(fake.name()))
                con = input("Devam etmek istiyormusun (e/h) : ")
                if con == "h":
                    print("\nTekrar görüşeceğiz...")
                    break
                elif con == "e":
                    continue
                else:
                    print("""
                    
                    Lütfen doğru seçim yapınız
                    (e/h) ---> (evet/hayır)

                    """)
                    break
            elif choose == "2":
                print("""
-----------------------------------------------------
Sahte adres oluşturuldu : 

{0}             
-----------------------------------------------------
                """.format(fake.address()))
                
                con = input("Devam etmek istiyormusun (e/h) : ")
                if con == "h":
                    print("\nTekrar görüşeceğiz...")
                    break
                elif con == "e":
                    continue
                else:
                    print("""
                    
                    Lütfen doğru seçim yapınız.
                    (e/h) ---> (evet/hayır)

                    """)
                    break
        elif cho =="2":
            fake = Faker(['tr_TR'])
            print(
                """
                [1] Sahte İsim
                [2] Sahte Adres
                [3]
                [4]
                [5]
                
                Exit[q]
                """)
            choose = input("Seçimin : ")

            if choose == "q":
                print("\nTekrar görüşeceğiz...")
                break
            elif choose == "1":
                print("""
-----------------------------------------------------
Sahte isim oluşturuldu : {0}             
-----------------------------------------------------
                """.format(fake.name()))
                con = input("Devam etmek istiyormusun (e/h) : ")
                if con == "h":
                    print("\nTekrar görüşeceğiz...")
                    break
                elif con == "e":
                    continue
                else:
                    print("""
                    
                    Lütfen doğru seçim yapınız
                    (e/h) ---> (evet/hayır)

                    """)
                    break
            elif choose == "2":
                print("""
-----------------------------------------------------
Sahte adres oluşturuldu : 

{0}             
-----------------------------------------------------
                """.format(fake.address()))
                
                con = input("Devam etmek istiyormusunuz (e/h) : ")
                if con == "h":
                    print("\nTekrar görüşeceğiz...")
                    break
                elif con == "e":
                    continue
                else:
                    print("""
                    
                    Lütfen doğru seçimi yapınız
                    (e/h) ---> (evet/hayır)

                    """)
                    break
        else:
            print("""

        Lütfen doğru seçimi yapınız

        [1] İngilizce
        [2] Türkçe
            
            """)
            break
#Turkish - End

else:
    print("""

    Please choose a language

    Lütfen bir dil seç

    English : [EN]
    Türkçe  : [TR]
    """)

    
    
