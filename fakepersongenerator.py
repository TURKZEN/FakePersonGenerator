from faker import Faker
from time import sleep
from os import name,system


def menu():
    print("""
    
    Sahte bilgiler hangi dilde oluşturulsun ?

    [1] İngilizce
    [2] Türkçe

    [99] Çıkış
    
    """)
    
    lang = input("Seçiminiz : ")
    
    if lang == "1":
        EN()
    elif lang == "2":
        TR()
    elif lang == "99":
        Exit()
    else:
        print("Lütfen doğru bir seçim yapınız !")
        sleep(2)
        clean()
        Main()

def menu2():
    print("""
    
    Ne oluşturulsun ?

    [1] Sahte İsim
    [2] Sahte Adres
    
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
    
    elif choose == "99":
        Exit()
    
    else:
        print("Lütfen doğru bir seçim yapınız ! ")
        sleep(2)
        clean()
        Main()
def EN():
    global fake
    fake = Faker(['en_US'])
    menu2()

def TR():
    global fake
    fake = Faker(['tr_TR'])
    menu2()

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
    