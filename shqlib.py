import os, socket, requests, json, time

# Renk Kodları (B. Ç & SİAMEOX Özel Serisi)
G, C, R, Y, M, RS = '\033[92m', '\033[96m', '\033[91m', '\033[93m', '\033[95m', '\033[0m'

def ip_iz_sur(hedef):
    print(f"\n{C}[*] IP Lokasyon Sorgulanıyor: {hedef}{RS}")
    os.system(f"curl -s 'http://ip-api.com/json/{hedef}' | python3 -m json.tool")

def yerel_ag():
    print(f"\n{G}[*] Ağ Bilgileri Analiz Ediliyor...{RS}")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        print(f"{C}Yerel IP Adresiniz: {ip}{RS}\n{C}Cihaz Adı: {socket.gethostname()}{RS}")
    except: print(f"{R}[!] Ağ bilgisi alınamadı.{RS}")

def web_header(url):
    print(f"\n{C}[*] Sunucu Bilgileri Çekiliyor: {url}{RS}")
    if not url.startswith("http"): url = "http://" + url
    os.system(f"curl -I -L -s {url} | grep -E 'Server|Content-Type|X-Powered-By'")

def phish_kontrol(url):
    print(f"\n{Y}[*] Phishing Kontrolü: {url}{RS}")
    os.system(f"curl -s https://openphish.com/feed.txt | grep {url} || echo -e '{G}Temiz: Kayıt bulunamadı.{RS}'")

def eposta_sorgu(email):
    print(f"\n{M}[*] Holehe Başlatılıyor: {email}{RS}")
    os.system(f"holehe {email}")

def derin_nmap(hedef):
    print(f"\n{R}[*] Port Taraması (Hızlı Mod): {hedef}{RS}")
    os.system(f"nmap -F -Pn {hedef}")

def kullanici_tara(username):
    print(f"\n{M}[*] Sosyal Medya Araması: {username}{RS}")
    platforms = {"Instagram": "https://www.instagram.com/", "GitHub": "https://www.github.com/", "Telegram": "https://t.me/", "YouTube": "https://www.youtube.com/@"}
    for p, u in platforms.items():
        try:
            r = requests.get(u + username, timeout=5)
            if r.status_code == 200: print(f"{G}[+] Bulundu: {p}{RS}")
            else: print(f"{Y}[-] Yok: {p}{RS}")
        except: pass

def sizi_kontrol(email):
    print(f"\n{M}[*] Veri Sızıntısı Araması: {email}{RS}")
    url = f"https://api.proxynova.com/comb?query={email}"
    try:
        r = requests.get(url, timeout=10)
        data = r.json()
        if data.get("results"):
            print(f"{R}[!] Sızıntı bulundu!{RS}")
            for res in data['results'][:3]: print(f"  > {res}")
        else: print(f"{G}[+] Temiz.{RS}")
    except: print(f"{R}[!] API Hatası.{RS}")
