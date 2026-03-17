import os
import time
import sys

# Renk Tanımlamaları (Termux uyumlu)
RED = '\033[1;31m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
CYAN = '\033[1;36m'
WHITE = '\033[1;37m'
RESET = '\033[0m'

def banner():
    os.system('clear')
    print(f"""{RED}
    [ S H Q  T E A M ]
    ------------------
    S y s t e m  A n a l y s i s
    {RESET}
    {YELLOW}[ SHQ-Tool v1.1 - Siber Güvenlik Analiz ]{RESET}
    {CYAN}Geliştirici: B. Ç. & Siameox | 2026{RESET}
{RED}--------------------------------------------------{RESET}
 {GREEN}[1]{RESET} Port Tarayıcı (Standart)          {GREEN}[2]{RESET} IP / Domain İz Sürücü
 {GREEN}[3]{RESET} Yerel Ağ Bilgileri (Networker)     {GREEN}[4]{RESET} Web Header Analizi
 {GREEN}[5]{RESET} Phishing Bağlantı Kontrolü        {GREEN}[6]{RESET} E-Posta İstihbaratı
 {GREEN}[7]{RESET} Derin Tarama (Nmap Engine)         {RED}[0]{RESET} Çıkış
{RED}--------------------------------------------------{RESET}
    """)

def main():
    while True:
        banner()
        try:
            secim = input(f"{YELLOW} Seçiminiz >> {RESET}")

            if secim == '1':
                print(f"\n{GREEN}[*] Port Tarayıcı başlatılıyor...{RESET}")
                time.sleep(2)
            elif secim == '2':
                print(f"\n{GREEN}[*] IP İz Sürücü modülü aktif...{RESET}")
                time.sleep(2)
            elif secim == '6':
                print(f"\n{CYAN}[!] E-Posta İstihbaratı (Holehe) başlatılıyor...{RESET}")
                email = input(f"{WHITE} Hedef E-Posta: {RESET}")
                os.system(f"holehe {email}")
                input(f"\n{YELLOW}Devam etmek için Enter'a basın...{RESET}")
            elif secim == '7':
                print(f"\n{RED}[!] Nmap Engine çalıştırılıyor...{RESET}")
                target = input(f"{WHITE} Hedef IP/Domain: {RESET}")
                os.system(f"nmap -A {target}")
                input(f"\n{YELLOW}Devam etmek için Enter'a basın...{RESET}")
            elif secim == '0':
                print(f"\n{RED}[!] SHQ-Tool Kapatılıyor... İyi avlar asker!{RESET}")
                sys.exit()
            else:
                print(f"\n{RED}[!] Geçersiz seçim!{RESET}")
                time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n\n{RED}[!] İşlem kullanıcı tarafından durduruldu.{RESET}")
            sys.exit()

if __name__ == "__main__":
    main()
