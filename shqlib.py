import os, socket, requests, json, time

# Renk Kodları (B. Ç & SİAMEOX Özel Serisi)
G = '\033[92m'  # Yeşil
C = '\033[96m'  # Turkuaz
R = '\033[91m'  # Kırmızı
Y = '\033[93m'  # Sarı
M = '\033[95m'  # Mor
RS = '\033[0m'  # Reset

def ip_iz_sur(hedef):
    print(f"\n{C}[*] IP Lokasyon Sorgulanıyor: {hedef}{RS}")
    os.system(f"curl -s 'http://ip-api.com/json/{hedef}'")

def yerel_ag():
    print(f"\n{G}[*] Ağ Bilgileri Analiz Ediliyor...{RS}")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        print(f"{C}Yerel IP Adresiniz: {ip}{RS}")
    except: 
        print(f"{R}[!] Ağ bilgisi alınamadı.{RS}")

def web_header(url):
    print(f"\n{C}[*] Sunucu Bilgileri Çekiliyor: {url}{RS}")
    if not url.startswith("http"): url = "http://" + url
    os.system(f"curl -I -L -s {url} | grep -E 'Server|Content-Type|X-Powered-By'")

def phish_kontrol(url):
    print(f"\n{Y}[*] Phishing Kontrolü: {url}{RS}")
    os.system(f"curl -s https://openphish.com/feed.txt | grep '{url}'")

def holehe_sorgu(target):
    """Hem E-Posta hem Telefon Numarası sorgulayabilir"""
    print(f"\n{M}[*] Holehe OSINT Başlatılıyor: {target}{RS}")
    print(f"{Y}[!] Bu işlem biraz zaman alabilir, lütfen bekleyin...{RS}")
    os.system(f"holehe {target}")

def derin_nmap(hedef):
    print(f"\n{R}[*] Port Taraması (Hızlı Mod): {hedef}{RS}")
    os.system(f"nmap -F -Pn {hedef}")

def kullanici_tara(username):
    print(f"\n{M}[*] Sosyal Medya Araması: {username}{RS}")
    platforms = {
        "Instagram": "https://www.instagram.com/",
        "Twitter": "https://twitter.com/",
        "TikTok": "https://www.tiktok.com/@",
        "GitHub": "https://github.com/",
        "YouTube": "https://www.youtube.com/@"
    }
    for p, u in platforms.items():
        try:
            r = requests.get(u + username, timeout=5, headers={'User-Agent': 'Mozilla/5.0'})
            if r.status_code == 200: 
                print(f"{G}[+] Bulundu: {p} ({u}{username}){RS}")
            else: 
                print(f"{Y}[-] Yok: {p}{RS}")
        except: 
            pass

def sizi_kontrol(email):
    print(f"\n{M}[*] Veri Sızıntısı Araması: {email}{RS}")
    url = f"https://api.proxynova.com/comb?query={email}"
    try:
        r = requests.get(url, timeout=10)
        data = r.json()
        if data.get("results"):
            print(f"{R}[!] Sızıntı bulundu!{RS}")
            for res in data['results'][:3]: 
                print(f"  >> {res}")
        else: 
            print(f"{G}[+] Temiz.{RS}")
    except: 
        print(f"{R}[!] API Hatası.{RS}")
