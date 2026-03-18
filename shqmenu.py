import os, time, sys, shqlib

# Renk Paleti
G, C, R, Y, M, W, RS = '\033[92m', '\033[96m', '\033[91m', '\033[93m', '\033[95m', '\033[97m', '\033[0m'

def yasal_uyari():
    os.system("clear")
    print(f"{R}╔══════════════════════════════════════════════════════╗{RS}")
    print(f"{R}║             [!] KRİTİK YASAL UYARI [!]               ║{RS}")
    print(f"{R}╠══════════════════════════════════════════════════════╣{RS}")
    print(f"{W}║ Bu yazılım sadece eğitim amaçlıdır. Sorumluluk       ║")
    print(f"║ tamamen B. Ç & SİAMEOX kullanıcılarına aittir.       ║")
    print(f"{R}╠══════════════════════════════════════════════════════╣{RS}")
    print(f"{C}║      Developer Team: B. Ç & SİAMEOX                  ║{RS}")
    print(f"{R}╚══════════════════════════════════════════════════════╝{RS}")
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
    print(f"       {W}--- {C}SHQ INTELLIGENCE TEAM {W}---{RS}")
    print(f"{R}──────────────────────────────────────────────────────────{RS}")
    print(f"{W}Sürüm: {G}v8.6 {W}| Sahibi: {M}B. Ç & SİAMEOX {W}| Durum: {G}Aktif{RS}")
    print(f"{R}──────────────────────────────────────────────────────────{RS}")

def main():
    yasal_uyari()
    while True:
        banner()
        print(f" {G}[01]{RS} {W}📡 IP İz Sürme         {C}» {Y}Lokasyon Analizi{RS}")
        print(f" {G}[02]{RS} {W}🌐 Yerel Ağ Bilgisi    {C}» {Y}İç IP & Cihaz{RS}")
        print(f" {G}[03]{RS} {W}🛡️  Web Header Analizi  {C}» {Y}Sunucu Tespiti{RS}")
        print(f" {G}[04]{RS} {W}🎣 Phishing Kontrolü   {C}» {Y}Link Taraması{RS}")
        print(f" {G}[05]{RS} {W}📧 E-Posta İz Sürme    {C}» {Y}Holehe OSINT{RS}")
        print(f" {G}[06]{RS} {W}🔍 Hızlı Port Taraması {C}» {Y}Nmap Analizi{RS}")
        print(f" {G}[07]{RS} {W}👤 Sosyal Medya Bulucu {C}» {Y}Kullanıcı Tarama{RS}")
        print(f" {G}[08]{RS} {W}🕵️  Sizi Kontrolü       {C}» {Y}Güvenlik Testi{RS}")
        print(f" {G}[09]{RS} {W}🗃️  Veri Sızıntısı     {C}» {Y}Database Sorgu{RS}")
        print(f"\n {R}[00]{RS} {W}🚪 Sistemi Kapat (Çıkış){RS}")
        print(f"{R}──────────────────────────────────────────────────────────{RS}")
        
        try:
            secim = input(f"{C}┌──({G}B.Ç & SİAMEOX{C})─[{W}shq-team{C}]\n└─{G}$ {RS}")
            
            if secim == "1" or secim == "01":
                h = input(f"{C}Hedef IP: {RS}"); shqlib.ip_iz_sur(h)
            elif secim == "2" or secim == "02":
                shqlib.yerel_ag()
            elif secim == "3" or secim == "03":
                u = input(f"{C}Hedef URL: {RS}"); shqlib.web_header(u)
            elif secim == "4" or secim == "04":
                u = input(f"{C}URL: {RS}"); shqlib.phish_kontrol(u)
            elif secim == "5" or secim == "05":
                e = input(f"{C}E-Posta: {RS}"); shqlib.eposta_sorgu(e)
            elif secim == "6" or secim == "06":
                h = input(f"{C}Hedef Host: {RS}"); shqlib.derin_nmap(h)
            elif secim == "7" or secim == "07":
                u = input(f"{C}Kullanıcı: {RS}"); shqlib.kullanici_tara(u)
            elif secim == "8" or secim == "08" or secim == "9" or secim == "09":
                e = input(f"{C}E-Posta: {RS}"); shqlib.sizi_kontrol(e)
            elif secim == "0" or secim == "00":
                print(f"\n{R}[!] Sistem Kapatılıyor...{RS}"); sys.exit()
            
            input(f"\n{Y}Menüye dönmek için [ENTER] basın...{RS}")
        except KeyboardInterrupt:
            print(f"\n{R}[!] İşlem iptal edildi.{RS}"); break

if __name__ == "__main__":
    main()
