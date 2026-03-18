import os, time, sys, shqlib

# Renkler
G, C, R, Y, M, RS = '\033[92m', '\033[96m', '\033[91m', '\033[93m', '\033[95m', '\033[0m'

def yasal_uyari():
    os.system("clear")
    print(f"{R}──────────────────────────────────────────────────────────{RS}")
    print(f"{R}[!] YASAL UYARI [!]{RS}")
    print(f"{Y}Bu araç sadece eğitim ve savunma amaçlıdır.")
    print(f"Kullanımdan doğacak her türlü sorumluluk kullanıcıya aittir.")
    print(f"{C}Sahibi: B. Ç & SİAMEOX{RS}")
    print(f"{R}──────────────────────────────────────────────────────────{RS}")
    time.sleep(2) # O beklenen 2 saniyelik profesyonel duruş

def banner():
    os.system("clear")
    print(f"""{R}
     ██████╗██╗  ██╗ ██████╗ 
    ██╔════╝██║  ██║██╔═══██╗
    ╚█████╗ ███████║██║   ██║
     ╚═══██╗██╔══██║██║   ██║
    ██████╔╝██║  ██║╚██████╔╝
    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ 
    {C}--- SHQ OSINT ISTİHBARAT TOOL ---{RS}
    {Y}Geliştirici & Sahibi: {G}B. Ç & SİAMEOX{RS}
    """)

def main():
    yasal_uyari()
    while True:
        banner()
        print(f"{G}[1]{RS} IP İz Sürme")
        print(f"{G}[2]{RS} Yerel Ağ Bilgisi")
        print(f"{G}[3]{RS} Web Header Analizi")
        print(f"{G}[4]{RS} Phishing Kontrolü")
        print(f"{G}[5]{RS} E-Posta İz Sürme (Holehe)")
        print(f"{G}[6]{RS} Hızlı Port Taraması (Nmap)")
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
            e = input("E-Posta: "); shqlib.sizi_kontrol(e)
        elif secim == "9":
            e = input("E-Posta: "); shqlib.sizi_kontrol(e)
        elif secim == "0":
            print(f"{G}Güle Güle...{RS}"); sys.exit()
        
        input(f"\n{Y}Menüye dönmek için Enter'a basın...{RS}")

if __name__ == "__main__":
    main()
