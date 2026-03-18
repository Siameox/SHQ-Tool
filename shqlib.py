import os
import socket
import requests

# Renk kodlarını (Eğer üstte tanımlı değilse hata vermemesi için buraya da ekledim)
GREEN = '\033[92m'
CYAN = '\033[96m'
RED = '\033[91m'
YELLOW = '\033[93m'
MAGENTA = '\033[95m'
RESET = '\033[0m'

def ip_iz_sur(hedef):
    print(f"\n{CYAN}[*] IP Lokasyon İstihbaratı...{RESET}")
    os.system(f"curl -s 'http://ip-api.com/json/{hedef}'")

def yerel_ag():
    print(f"\n{GREEN}[*] Yerel IP Bilgisi:{RESET}")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        print(f"{CYAN}IP: {s.getsockname()[0]}{RESET}")
        s.close()
    except: 
        print(f"{RED}[!] Bağlantı yok.{RESET}")

def web_header(url):
    os.system(f"curl -I -L -s {url} | grep -E 'Server|Content-Type|X-Frame-Options'")

def phish_kontrol(url):
    os.system(f"curl -s https://openphish.com/feed.txt | grep '{url}'")

def eposta_sorgu(email):
    os.system(f"holehe {email}")

def derin_nmap(hedef):
    os.system(f"nmap -A -T4 -Pn {hedef}")

# --- YENİ VE HATASIZ OSINT MOTORU ---
def kullanici_tara(username):
    print(f"\n{MAGENTA}[*] SHQ OSINT Engine Başlatıldı:{RESET}")
    print(f"{YELLOW}[*] Popüler platformlar taranıyor...{RESET}")

    social_media = {
        "Instagram": f"https://www.instagram.com/{username}",
        "Twitter/X": f"https://www.twitter.com/{username}",
        "GitHub": f"https://www.github.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Telegram": f"https://t.me/{username}",
        "YouTube": f"https://www.youtube.com/@{username}",
        "Twitch": f"https://www.twitch.tv/{username}"
    }

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

    for platform, url in social_media.items():
        try:
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200:
                print(f"{GREEN}[+] {platform}: {url}{RESET}")
        except:
            print(f"{RED}[!] {platform}: Bağlantı hatası.{RESET}")

    print(f"\n{CYAN}[*] Tarama tamamlandı.{RESET}")

# --- V2.0: VERİ SIZINTISI KONTROLÜ (NEW) ---
def sizi_kontrol(email):
    print(f"\n{MAGENTA}[*] Veri Sızıntısı Sorgulanıyor: {YELLOW}{email}{RESET}")
    # Ücretsiz ve güncel bir API üzerinden sorgulama yapar
    url = f"https://api.proxynova.com/comb?query={email}"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if data.get("results"):
            print(f"{RED}[!] TEHLİKE: Bu e-posta {len(data['results'])} sızıntıda bulundu!{RESET}")
            print(f"{YELLOW}[-] Sızan Veri Kaynakları:{RESET}")
            # Çok fazla sonuç varsa ilk 10 tanesini gösterelim ki ekran dolmasın
            for result in data['results'][:10]:
                print(f"  > {result}")
            if len(data['results']) > 10:
                print(f"{CYAN}... ve daha fazlası.{RESET}")
        else:
            print(f"{GREEN}[+] TEMİZ: Bilinen büyük bir sızıntı kaydı bulunamadı.{RESET}")
            
    except Exception as e:
        print(f"{RED}[!] Sorgulama hatası: {e}{RESET}")
