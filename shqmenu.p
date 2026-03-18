import os, time, sys, shqlib

# Renkler
G, C, R, Y, M, RS = '\033[92m', '\033[96m', '\033[91m', '\033[93m', '\033[95m', '\033[0m'

def yasal_uyari():
    os.system("clear")
    print(f"{R}[!] YASAL UYARI [!]{RS}")
    print(f"{Y}Bu araç sadece eğitim ve savunma amaçlıdır.")
    print(f"Kullanımdan doğacak sorumluluk kullanıcıya aittir.")
    print(f"{C}SHQ İstihbarat Timi - 2026{RS}")
    time.sleep(2) # O meşhur 2 saniyelik bekletme

def banner():
    os.system("clear")
    print(f"""{R}
     ██████╗██╗  ██╗ ██████╗ 
    ██╔════╝██║  ██║██╔═══██╗
    ╚█████╗ ███████║██║   ██║
     ╚═══██╗██╔══██║██║   ██║
    ██████╔╝██║  ██║╚██████╔╝
    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ 
    {C}--- SHQ OSINT ISTIHBARAT TOOL ---{RS}
    """)

def main():
    yasal_uyari()
    while True:
        banner()
        print(f"{G}[1]{RS} IP Iz Sürme")
        print(f"{G}[2]{RS} Yerel Ag Bilgisi")
        print(f"{G}[3]{RS} Web Header Analizi")
        print(f"{G}[4]{RS} Phishing Kontrolü")
        print(f"{G}[5]{RS} E-Posta Iz Sürme (Holehe)")
        print(f"{G}[6]{RS} Hizli Port Taraması (Nmap)")
        print(f"{G}[7]{RS} Sosyal Medya Tarayıcı")
        print(f"{G}[8]{RS} Sizi Kontrolü (Email Sorgu)")
        print(f"{G}[9]{RS} Veri Sızıntısı Sorgula (COMB)")
        print(f"{R}[0]{RS} Çıkış\n")
        
        secim = input(f"{Y}Seçiminiz >> {RS}")
        
        if secim == "1":
            h = input("Hedef IP: "); shqlib.ip_iz_sur(h)
        elif secim == "2":
            shqlib.yerel_ag()
        elif secim == "3":
            u = input("URL: "); shqlib.web_header(u)
        elif secim == "4":
            u = input("URL: "); shqlib.phish_kontrol(u)
        elif secim == "5":
            e = input("E-Posta: "); shqlib.eposta_sorgu(e)
        elif secim == "6":
            h = input("Hedef: "); shqlib.derin_nmap(h)
        elif secim == "7":
            u = input("Kullanıcı Adı: "); shqlib.kullanici_tara(u)
        elif secim == "8":
            e = input("E-Posta: "); shqlib.sizi_kontrol(e) # Eski libdeki basit kontrol
        elif secim == "9":
            e = input("E-Posta: "); shqlib.sizi_kontrol(e) # Yeni libdeki detaylı sorgu
        elif secim == "0":
            print(f"{G}Güle Güle...{RS}"); sys.exit()
        
        input(f"\n{Y}Menüye dönmek için Enter'a basın...{RS}")

if __name__ == "__main__":
    main()

