import os, time, sys, shqlib

# Renkler
RED    = '\033[1;31m'
GREEN  = '\033[1;32m'
YELLOW = '\033[1;33m'
CYAN   = '\033[1;36m'
MAGENTA = '\033[1;35m'
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
    print(f"{YELLOW}SHQ İstihbarat Sistemleri Başlatılıyor...{RESET}")
    time.sleep(2)

def banner():
    os.system('clear')
    print(r" " + RED + r"""
   ____  _   _   ___     _____ _____  _    __  __
  / ___|| | | | / _ \   |_   _| ____|/ \  |  \/  |
  \___ \| |_| || | | |    | | |  _| / _ \ | |\/| |
   ___) |  _  || |_| |    | | | |__/ ___ \| |  | |
  |____/|_| |_| \__\_\    |_| |____/_/   \_\_|  |_|
""" + RESET + f"""
 {RED}------------------------------------------------->
 {YELLOW}[ SHQ-Tool v2.5 - AI & OSINT Edition ]{RESET}
 {CYAN}Geliştirici: Berat & Siameox | 2026{RESET}
 {RED}------------------------------------------------->
""")

    items = [
        "Port Tarayıcı (Hızlı)",
        "IP / Domain İz Sürücü",
        "Yerel Ağ Bilgileri",
        "Web Header Analizi",
        "Phishing & URL Kontrol",
        "E-Posta İstihbaratı",
        "Nmap Derin Tarama",
        "Kullanıcı Adı Tarayıcı (SHQ OSINT)",
        "Veri Sızıntısı Kontrolü (Data Breach)",
        f"{MAGENTA}SHQ AI ASİSTANI (Yapay Zeka){RESET}"
    ]

    for i, item in enumerate(items, 1):
        print(f" {GREEN}[{i}]{RESET} {item}")
    print(f" {RED}[0]{RESET} Çıkış\n{RED}------------------------------------------------->{RESET}")

def main():
    yasal_uyari()
    while True:
        banner()
        try:
            secim = input(f"{YELLOW} Seçiminiz >> {RESET}")

            if secim == '0':
                print(f"\n{RED}[!] SHQ TEAM Kapatılıyor...{RESET}")
                sys.exit()

            # Hedef gerektiren seçenekler
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

            elif secim == '9':
                target_mail = input(f"\n{CYAN}Sorgulanacak E-Posta: {RESET}")
                shqlib.sizi_kontrol(target_mail)

            elif secim == '10':
                print(f"\n{MAGENTA}--- SHQ AI ASİSTANI AKTİF ---{RESET}")
                print(f"{YELLOW}(Çıkmak için 'exit' yazın){RESET}")
                while True:
                    soru = input(f"\n{CYAN}Sorunuz > {RESET}")
                    if soru.lower() == 'exit':
                        break
                    shqlib.shq_ai_asistan(soru)

            else:
                print(f"\n{RED}[!] Hatalı Seçim!{RESET}")
                time.sleep(1)
                continue

            input(f"\n{YELLOW}Menüye dönmek için Enter'a basın...{RESET}")

        except KeyboardInterrupt:
            print(f"\n\n{RED}[!] İşlem kullanıcı tarafından durduruldu.{RESET}")
            sys.exit()

if __name__ == "__main__":
    main()
