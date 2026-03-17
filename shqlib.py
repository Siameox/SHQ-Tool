import os
import socket
import sys
import requests

# Renkler
RED    = '\033[1;31m'
GREEN  = '\033[1;32m'
YELLOW = '\033[1;33m'
CYAN   = '\033[1;36m'
MAGENTA = '\033[1;35m'
RESET  = '\033[0m'

# DİĞER FONKSİYONLARIN (Nmap, IP, vb.) AYNI KALSIN...
def port_taramasi(hedef):
    print(f"\n{YELLOW}[*] Standart Port Taraması: {hedef}{RESET}")
    os.system(f"nmap -sV --open -T4 {hedef}")

def ip_iz_sur(hedef):
    print(f"\n{CYAN}[*] IP Lokasyon İstihbaratı...{RESET}")
    os.system(f"curl -s 'http://ip-api.com/json/{hedef}?fields=status,country,city,lat,lon,isp,org,as,query'")

def yerel_ag():
    print(f"\n{GREEN}[*] Yerel IP Bilgisi:{RESET}")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.connect(("8.8.8.8", 80))
        print(f"{CYAN}IP: {s.getsockname()[0]}{RESET}"); s.close()
    except: print(f"{RED}[!] Bağlantı yok.{RESET}")

def web_header(url):
    os.system(f"curl -I -L -s {url} | grep -E 'Server|Content-Type'")

def phish_kontrol(url):
    os.system(f"curl -s https://openphish.com/feed.txt | grep {url} && echo '{RED}[!] PHISHING!{RESET}' || echo '{GREEN}[+] Temiz.{RESET}'")

def eposta_sorgu(email):
    os.system(f"holehe {email}")

def derin_nmap(hedef):
    os.system(f"nmap -A -T4 -Pn {hedef}")

# --- YENİ VE HATASIZ OSINT MOTORU ---
def kullanici_tara(username):
    print(f"\n{MAGENTA}[*] SHQ OSINT Engine Başlatıldı: {username}{RESET}")
    print(f"{YELLOW}[*] Popüler platformlar taranıyor...{RESET}\n")

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

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    for platform, url in social_media.items():
        try:
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200:
                print(f"{GREEN}[+] {platform}: {url}{RESET}")
            else:
                pass # Bulunamazsa bir şey yazma, kalabalık olmasın
        except:
            print(f"{RED}[!] {platform}: Bağlantı hatası.{RESET}")

    print(f"\n{CYAN}[*] Tarama tamamlandı.{RESET}")
