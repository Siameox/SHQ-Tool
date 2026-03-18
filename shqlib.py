import os
import socket
import requests
import json
import urllib.parse
import time

# Renk kodları
GREEN = '\033[92m'
CYAN = '\033[96m'
RED = '\033[91m'
YELLOW = '\033[93m'
MAGENTA = '\033[95m'
RESET = '\033[0m'

# --- SHQ AI ASİSTANI (GELİŞMİŞ HATA YÖNETİMİ V3.2) ---
def shq_ai_asistan(soru):
    print(f"\n{MAGENTA}[*] SHQ AI Veri Hattı Kuruluyor...{RESET}")
    
    encoded_soru = urllib.parse.quote(soru)
    system_msg = urllib.parse.quote("Sen SHQ İstihbarat Timi siber güvenlik asistanısın. Türkçe ve teknik cevap ver.")
    base_url = "https://text.pollinations.ai/"
    final_url = f"{base_url}{encoded_soru}?system={system_msg}"

    try:
        # İlk deneme
        response = requests.get(final_url, timeout=30)
        
        # Eğer hız sınırına takılırsak (Hata 429)
        if response.status_code == 429:
            print(f"{YELLOW}[!] Çok fazla istek gönderildi. 5 saniye bekleniyor...{RESET}")
            time.sleep(5)
            # İkinci deneme
            response = requests.get(final_url, timeout=30)

        if response.status_code == 200:
            cevap = response.text.strip()
            print(f"\n{GREEN}[+] SHQ AI Yanıtı:{RESET}\n{CYAN}{cevap}{RESET}")
        else:
            print(f"{RED}[!] Sunucu Hatası: {response.status_code}. Lütfen 30 saniye sonra tekrar dene.{RESET}")
            
    except requests.exceptions.Timeout:
        print(f"{RED}[!] HATA: Zaman aşımı. İnternet hızın düşük olabilir.{RESET}")
    except Exception as e:
        print(f"{RED}[!] Beklenmedik Hata: {e}{RESET}")

# --- OSINT & TEKNİK ARAÇLAR ---
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
    print(f"\n{CYAN}[*] Header Analizi Yapılıyor...{RESET}")
    os.system(f"curl -I -L -s {url} | grep -E 'Server|Content-Type|X-Powered-By'")

def phish_kontrol(url):
    print(f"\n{YELLOW}[*] Phishing Kontrolü...{RESET}")
    os.system(f"curl -s https://openphish.com/feed.txt | grep {url}")

def eposta_sorgu(email):
    print(f"\n{MAGENTA}[*] Holehe Sorgusu Başlatıldı...{RESET}")
    os.system(f"holehe {email}")

def derin_nmap(hedef):
    print(f"\n{RED}[*] Nmap Taraması Başlatıldı...{RESET}")
    os.system(f"nmap -A -T4 -Pn {hedef}")

def kullanici_tara(username):
    print(f"\n{MAGENTA}[*] SHQ OSINT Engine Başlatıldı...{RESET}")
    social_media = {
        "Instagram": f"https://www.instagram.com/{username}",
        "GitHub": f"https://www.github.com/{username}",
        "Telegram": f"https://t.me/{username}",
        "YouTube": f"https://www.youtube.com/@{username}"
    }
    headers = {"User-Agent": "Mozilla/5.0"}
    for platform, url in social_media.items():
        try:
            res = requests.get(url, headers=headers, timeout=5)
            if res.status_code == 200:
                print(f"{GREEN}[+] {platform}: {url}{RESET}")
        except: pass

def sizi_kontrol(email):
    print(f"\n{MAGENTA}[*] Veri Sızıntısı Sorgulanıyor: {email}{RESET}")
    url = f"https://api.proxynova.com/comb?query={email}"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        if data.get("results"):
            print(f"{RED}[!] TEHLİKE: Sızıntı bulundu!{RESET}")
            for result in data['results'][:5]:
                print(f"  > {result}")
        else:
            print(f"{GREEN}[+] TEMİZ: Bilinen bir sızıntı yok.{RESET}")
    except:
        print(f"{RED}[!] Sorgulama hatası.{RESET}")
