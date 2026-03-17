#!/bin/bash

# Renkler
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
RED='\033[1;31m'
RESET='\033[0m'

echo -e "${YELLOW}[*] SHQ TEAM - Otomatik Kurulum Başlatılıyor...${RESET}"
sleep 2

# Sistem Güncelleme
echo -e "${GREEN}[+] Sistem paketleri güncelleniyor...${RESET}"
pkg update -y && pkg upgrade -y

# Gerekli Paketlerin Kurulumu (Nmap vb.)
echo -e "${GREEN}[+] Nmap ve Python kuruluyor...${RESET}"
pkg install nmap python git -y

# Python Kütüphanelerinin Kurulumu
echo -e "${GREEN}[+] Python modülleri (requests, nmap, holehe) yükleniyor...${RESET}"
pip install --upgrade pip
pip install requests python-nmap holehe

# Yetkilendirme
echo -e "${GREEN}[+] Dosya yetkileri ayarlanıyor...${RESET}"
chmod +x shq_menu.py

echo -e "${YELLOW}====================================================${RESET}"
echo -e "${GREEN}[!] KURULUM TAMAMLANDI!${RESET}"
echo -e "${GREEN}[!] Artık 'python shq_menu.py' yazarak başlayabilirsin.${RESET}"
echo -e "${YELLOW}====================================================${RESET}"
