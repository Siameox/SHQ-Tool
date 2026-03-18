#!/bin/bash

# Renkler
GREEN='\033[1;32m'
CYAN='\033[1;36m'
YELLOW='\033[1;33m'
RED='\033[1;31m'
RESET='\033[0m'

clear
echo -e "${CYAN}------------------------------------------"
echo -e "${CYAN}[*] SHQ-Tool V2.7 (AI Edition) Kurulumu"
echo -e "${CYAN}------------------------------------------${RESET}"
sleep 1

# Paket Güncelleme
echo -e "${YELLOW}[1] Sistem paketleri güncelleniyor...${RESET}"
pkg update -y && pkg upgrade -y

# Temel Bağımlılıklar
echo -e "${YELLOW}[2] Sistem araçları yükleniyor...${RESET}"
pkg install python curl nmap -y

# DNS Ayarı (Bağlantı ve Timeout hatalarını önlemek için kritik)
echo -e "${YELLOW}[3] Ağ optimizasyonu yapılıyor...${RESET}"
echo "nameserver 8.8.8.8" > /data/data/com.termux/files/usr/etc/resolv.conf

# Python Kütüphaneleri
echo -e "${YELLOW}[4] Python modülleri kuruluyor...${RESET}"
pip install --upgrade pip
pip install requests urllib3 holehe

# Çalıştırma İzinleri
echo -e "${YELLOW}[5] Dosya izinleri düzenleniyor...${RESET}"
chmod +x shqmenu.py
chmod +x shqlib.py
chmod +x setup.sh

clear
echo -e "${GREEN}------------------------------------------"
echo -e "${GREEN}[+] KURULUM BAŞARIYLA TAMAMLANDI!"
echo -e "${GREEN}------------------------------------------"
echo -e "${CYAN}[*] SHQ AI ve OSINT Modülleri Hazır."
echo -e "${YELLOW}[!] Başlatmak için: ${RESET}python3 shqmenu.py"
echo -e "${GREEN}------------------------------------------${RESET}"
