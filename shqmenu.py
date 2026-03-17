import os, time, sys, shqlib

# Renkler
RED    = '\033[1;31m'
GREEN  = '\033[1;32m'
YELLOW = '\033[1;33m'
CYAN   = '\033[1;36m'
RESET  = '\033[0m'

def yasal_uyari():
    os.system('clear')
    print(f"""{RED}
  [ ! ] YASAL UYARI [ ! ]
  --------------------------------------------------
  Bu araç sadece eğitim ve test amaçlıdır.
  İzinsiz kullanımda tüm sorumluluk kullanıcıya aittir.
  SHQ TEAM sorumluluk kabul etmez.
  --------------------------------------------------
  {RESET}""")
    print(f"{YELLOW}Sistem başlatılıyor...{RESET}")
    time.sleep(2)

def banner():
    os.system('clear')
    # Kaçış dizisi hatası almamak için raw string (r"") kullanıyoruz
    print(r" " + RED + r"""
   ____  _   _   ___     _____ _____  _    __  __ 
  / ___|| | | | / _ \   |_   _| ____|/ \  |  \/  |
  \___ \| |_| || | | |    | | |  _| / _ \ | |\/| |
   ___) |  _  || |_| |    | | | |__/ ___ \| |  | |
  |____/|_| |_| \__\_\    |_| |____/_/   \_\_|  |_|
""" + RESET + f"""
 {RED}--------------------------------------------------{RESET}
 {YELLOW}[ SHQ-Tool v1.5 - OSINT Edition ]{RESET}
 {CYAN}Geliştirici: B. Ç. & Siameox | 2026{RESET}
 {RED}--------------------------------------------------{RESET}""")
    
    items = [
        "Port Tarayıcı (Hızlı)", 
        "IP / Domain İz Sürücü", 
        "Yerel Ağ Bilgileri", 
        "Web Header Analizi", 
        "Phishing & URL Kontrol", 
        "E-Posta İstihbaratı", 
        "Nmap Derin Tarama",
        "Kullanıcı Adı Tarayıcı (Sherlock)"
    ]
    
    for i, item in enumerate(items, 1):
        print(f" {GREEN}[{i}]{RESET} {item}")
    print(f" {RED}[0]{RESET} Çıkış\n{RED}--------------------------------------------------{RESET}")

def main():
    yasal_uyari()
    while True:
        banner()
        try:
            secim = input(f"{YELLOW} Seçiminiz >> {RESET}")
            if secim == '0': 
                print(f"\n{RED}[!] SHQ TEAM Kapatılıyor...{RESET}")
                sys.exit()
            
            if secim in '1245678':
                hedef = input(f"\n{CYAN}Hedef Girin: {RESET}")
                if secim == '1': shqlib.port_taramasi(hedef)
                elif secim == '2': shqlib.ip_iz_sur(hedef)
                elif secim == '4': shqlib.web_header(hedef)
                elif secim == '5': shqlib.phish_kontrol(hedef)
                elif secim == '6': shqlib.eposta_sorgu(hedef)
                elif secim == '7': shqlib.derin_nmap(hedef)
                elif secim == '8': shqlib.kullanici_tara(hedef)
            elif secim == '3':
                shqlib.yerel_ag()
            else:
                print(f"\n{RED}[!] Hatalı Seçim!{RESET}")
                time.sleep(1)
                continue
                
            input(f"\n{YELLOW}Menüye dönmek için Enter'a basın...{RESET}")
        except KeyboardInterrupt:
            sys.exit()

if __name__ == "__main__":
    main()
