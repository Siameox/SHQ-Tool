import os, time, sys, shqlib 

# Renk Paleti (B. Ç & SİAMEOX Özel Serisi)
G = '\033[92m'  # Yeşil
C = '\033[96m'  # Turkuaz
R = '\033[91m'  # Kırmızı
Y = '\033[93m'  # Sarı
M = '\033[95m'  # Mor
W = '\033[97m'  # Beyaz
RS = '\033[0m'  # Reset

def yasal_uyari():
    os.system("clear")
    print(f"{R}╔══════════════════════════════════════════════════╗")
    print(f"{R}║             [!] KRİTİK YASAL UYARI [!]           ║")
    print(f"{R}╠══════════════════════════════════════════════════╣")
    print(f"{W}║ Bu yazılım sadece eğitim amaçlıdır. Sorumluluk   ║")
    print(f"║ tamamen B. Ç & SİAMEOX kullanıcılarına aittir.   ║")
    print(f"{R}╠══════════════════════════════════════════════════╣")
    print(f"{C}║      Developer Team: B. Ç & SİAMEOX              ║")
    print(f"{R}╚══════════════════════════════════════════════════╝")
    time.sleep(2)

def banner():
    os.system("clear")
    print(f"{R}")
    print("  ██████╗ ██╗  ██╗  ██████╗ ")
    print("  ██╔════╝ ██║  ██║ ██╔═══██╗")
    print("  ╚█████╗  ███████║ ██║   ██║")
    print("   ╚═══██╗ ██╔══██║ ██║   ██║")
    print("  ██████╔╝ ██║  ██║ ╚██████╔╝")
    print("  ╚═════╝  ╚═╝  ╚═╝  ╚═════╝ ")
    print(f"       {W}--- {C}SHQ INTELLIGENCE TEAM {W}---")
    print(f"{R}────────────────────────────────────────────────────")
    print(f"{W}Sürüm: {G}v8.8 {W}| Sahibi: {M}B. Ç & SİAMEOX")
    print(f"{R}────────────────────────────────────────────────────")

def main():
    yasal_uyari()
    while True:
        banner()
        print(f" {G}[01]{RS} {W}📡 IP İz Sürme")
        print(f" {G}[02]{RS} {W}🌐 Yerel Ağ Bilgisi")
        print(f" {G}[03]{RS} {W}🛡️  Web Header Analizi")
        print(f" {G}[04]{RS} {W}🎣 Phishing Kontrolü")
        print(f" {G}[05]{RS} {W}📧 OSINT (E-Posta & Numara)")
        print(f" {G}[06]{RS} {W}🔍 Hızlı Port Taraması (Nmap)")
        print(f" {G}[07]{RS} {W}👤 Sosyal Medya Tarayıcı")
        print(f" {G}[08]{RS} {W}🕵️  Sizi Kontrolü")
        print(f" {G}[09]{RS} {W}🗃️  Veri Sızıntısı (COMB)")
        print(f"\n {R}[00]{RS} {W}🚪 Sistemi Kapat (Çıkış)")
        print(f"{R}────────────────────────────────────────────────────")

        try:
            secim = input(f"{C}┌──({G}B.Ç & SİAMEOX{C})─[{W}Menu{C}]\n└─> {RS}")

            if secim in ["1", "01"]:
                h = input(f"{C}Hedef IP: {RS}"); shqlib.ip_iz_sur(h)
            elif secim in ["2", "02"]:
                shqlib.yerel_ag()
            elif secim in ["3", "03"]:
                u = input(f"{C}URL: {RS}"); shqlib.web_header(u)
            elif secim in ["4", "04"]:
                u = input(f"{C}URL: {RS}"); shqlib.phish_kontrol(u)
            elif secim in ["5", "05"]:
                t = input(f"{C}Hedef: {RS}"); shqlib.holehe_sorgu(t)
            elif secim in ["6", "06"]:
                h = input(f"{C}Hedef: {RS}"); shqlib.derin_nmap(h)
            elif secim in ["7", "07"]:
                u = input(f"{C}Kullanıcı Adı: {RS}"); shqlib.kullanici_tara(u)
            elif secim in ["8", "08"]:
                e = input(f"{C}E-Posta: {RS}"); shqlib.sizi_kontrol(e)
            elif secim in ["9", "09"]:
                e = input(f"{C}E-Posta: {RS}"); shqlib.sizi_kontrol(e)
            elif secim in ["0", "00"]:
                print(f"{G}Güle Güle...{RS}"); sys.exit()
            else:
                print(f"{R}[!] Geçersiz Seçim!{RS}")
            
            input(f"\n{Y}Menüye dönmek için Enter'a basın...{RS}")
        except KeyboardInterrupt:
            print(f"\n{R}[!] İşlem iptal edildi.{RS}"); break

if __name__ == "__main__":
    main()
