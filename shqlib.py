import os, socket, requests, json

# Renk Kodları
G = '\033[92m'  # Yeşil
C = '\033[96m'  # Turkuaz
R = '\033[91m'  # Kırmızı
Y = '\033[93m'  # Sarı
M = '\033[95m'  # Magenta
RS = '\033[0m'  # Reset

# --- GEMINI İPTAL EDİLDİ (SADECE OSINT ARAÇLARI) ---

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
        print(f"{C}Yerel IP Adresiniz: {ip}{RS}")
        print(f"{C}Cihaz Adı: {socket.gethostname()}{RS}")
    except: print(f"{R}[!] Ağ bilgisi alınamadı.{RS}")

def web_header(url):
    print(f"\n{C}[*] {url} Sunucu Bilgileri Çekiliyor...{RS}")
    # URL başında http yoksa ekle
    if not url.startswith("http"): url = "http://" + url
    os.system(f"curl -I -L -s {url} | grep -E 'Server|Content-Type|X-Powered-By|X-Frame-Options'")

def phish_kontrol(url):
    print(f"\n{Y}[*] Phishing Veritabanı Taranıyor: {url}{RS}")
    os.system(f"curl -s https://openphish.com/feed.txt | grep {url} || echo -e '{G}Temiz: Kayıt bulunamadı.{RS}'")

def eposta_sorgu(email):
    print(f"\n{M}[*] Holehe (E-Posta İz Sürme) Başlatılıyor...{RS}")
    os.system(f"holehe {email}")

def derin_nmap(hedef):
    print(f"\n{R}[*] Nmap Port & Servis Taraması: {hedef}{RS}")
    os.system(f"nmap -T4 -F -Pn {hedef}")

def kullanici_tara(username):
    print(f"\n{M}[*] Sosyal Medya Araması: {username}{RS}")
    platforms = {
        "Instagram": f"https://www.instagram.com/{username}",
        "GitHub": f"https://www.github.com/{username}",
        "Telegram": f"https://t.me/{username}",
        "YouTube": f"https://www.youtube.com/@{username}"
    }
    for p, u in platforms.items():
        try:
            r = requests.get(u, timeout=5)
            if r.status_code == 200: print(f"{G}[+] Bulundu: {p} -> {u}{RS}")
            else: print(f"{Y}[-] Yok: {p}{RS}")
        except: pass

def sizi_kontrol(email):
    print(f"\n{M}[*] Veri Sızıntısı Araması: {email}{RS}")
    url = f"https://api.proxynova.com/comb?query={email}"
    try:
        r = requests.get(url, timeout=15)
        data = r.json()
        if data.get("results"):
            print(f"{R}[!] DİKKAT: Sızıntı bulundu!{RS}")
            for res in data['results'][:5]: print(f"  > {Y}{res}{RS}")
        else: print(f"{G}[+] Temiz: Bilinen sızıntılarda yok.{RS}")
    except: print(f"{R}[!] Servise ulaşılamadı.{RS}")

def shq_ai_asistan(soru):
    # Bu fonksiyon ana menüden çağrılırsa hata vermemesi için boş bıraktık
    print(f"\n{R}[!] Yapay Zeka modülü şu an devre dışı.{RS}")
