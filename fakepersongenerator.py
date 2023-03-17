# /usr/bin/python
from faker import Faker
from faker.providers import internet
from time import sleep
from os import name,system

def menu():
    fake = Faker(['en_US'])
    print("""
    
    Ne oluşturulsun ?

    [1] Sahte İsim
    [2] Sahte Adres
    [3] Sahte Yazı
    [4] Sahte IP Adresi

    [99] Çıkış
    
    """)

    choose = input("Seçiminiz : ")

    if choose == "1":
        space()
        print("""
Sahte İsim Oluşturuldu !
{}
{}
{}
        """.format("-"*50,fake.name(),"-"*50))

        Continue = input("Devam etmek istiyormusunuz ? (e/h) : ")

        if Continue == "e" or Continue == "E":
            menu()
        elif Continue == "h" or Continue == "H":
            Exit()
        else:
            print("""
            Lütfen doğru bir seçim yapınız !
            
            (e/h) ---> evet / hayır
            
             """)
            sleep(3)
            Exit()

    elif choose == "2":
        space()
        print("""
Sahte Adres Oluşturuldu !
{}
{}
{}
        """.format("-"*50,fake.address(),"-"*50))

        
        Continue = input("Devam etmek istiyormusunuz ? (e/h) : ")

        if Continue == "e" or Continue == "E":
            menu()
        elif Continue == "h" or Continue == "H":
            Exit()
        else:
            print("""
            Lütfen doğru bir seçim yapınız !
            
            (e/h) ---> evet / hayır
            
             """)
            sleep(3)
            Exit()
    
    elif choose == "3":
        space()
        print("""
Sahte Yazı Oluşturuldu !
{}
{}
{}
        """.format("-"*50,fake.text(),"-"*50))

        
        Continue = input("Devam etmek istiyormusunuz ? (e/h) : ")

        if Continue == "e" or Continue == "E":
            menu()
        elif Continue == "h" or Continue == "H":
            Exit()
        else:
            print("""
            Lütfen doğru bir seçim yapınız !
            
            (e/h) ---> evet / hayır
            
             """)
            sleep(3)
            Exit()
    
    elif choose == "4":
        fake = Faker()
        fake.add_provider(internet)
        space()

        print("""
Sahte IP Adresi oluşturuldu !
{}
{}
{}
        """.format("-"*50,fake.ipv4_private(),"-"*50))

        
        Continue = input("Devam etmek istiyormusunuz ? (e/h) : ")

        if Continue == "e" or Continue == "E":
            menu()
        elif Continue == "h" or Continue == "H":
            Exit()
        else:
            print("""
            Lütfen doğru bir seçim yapınız !
            
            (e/h) ---> evet / hayır
            
             """)
            sleep(3)
            Exit()
        
    
    elif choose == "99":
        Exit()
    
    else:
        print("Lütfen doğru bir seçim yapınız ! ")
        sleep(2)
        clean()
        Main()


def banner():
    clean()
    print("""
        
░█▀▀░█▀█░█░█░█▀▀░█▀█░█▀▀░█▀▄░█▀▀░█▀█░█▀█░█▀▀░█▀▀░█▀█░█▀▀░█▀▄░█▀█░▀█▀░█▀█░█▀▄
░█▀▀░█▀█░█▀▄░█▀▀░█▀▀░█▀▀░█▀▄░▀▀█░█░█░█░█░█░█░█▀▀░█░█░█▀▀░█▀▄░█▀█░░█░░█░█░█▀▄
░▀░░░▀░▀░▀░▀░▀▀▀░▀░░░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀░▀░░▀░░▀▀▀░▀░▀

                Author : Batuhan Türkarslan
                GitHub : https://github.com/TURKZEN

    """)
    sleep(0.5)

def Exit():
    space()
    print("Çıkış yapıldı !")

def space():
    print()

def clean():
    if name == "nt":
        system("cls")
    elif name == "posix":
        system("clear")

def Main():
    clean()
    banner()
    menu()


if __name__ == "__main__":
    try:
        Main()
    except KeyboardInterrupt:
        Exit()
    except EOFError:
        Exit()
    except:
        space()
        print("Bilinmeyen Hata !")
        sleep(1)
        Exit()
    