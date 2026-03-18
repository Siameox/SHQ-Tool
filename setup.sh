#!/bin/bash

# Renkler
GREEN='\033[1;32m'
CYAN='\033[1;36m'
YELLOW='\033[1;33m'
RED='\033[1;31m'
RESET='\033[0m'

echo -e "${CYAN}[*] SHQ-Tool V2.0 Kurulumu Başlatılıyor...${RESET}"
sleep 1

# Paket Güncelleme
echo -e "${YELLOW}[1] Paket listesi güncelleniyor...${RESET}"
pkg update -y && pkg upgrade -y

# Temel Bağımlılıklar
echo -e "${YELLOW}[2] Gerekli araçlar yükleniyor (Python, Curl, Nmap)...${RESET}"
pkg install python -y
pkg install curl -y
pkg install nmap -y

# Python Kütüphaneleri (KRİTİK NOKTA)
echo -e "${YELLOW}[3] Python kütüphaneleri yükleniyor (Requests, Holehe)...${RESET}"
pip install requests
pip install holehe

# Çalıştırma İzinleri
echo -e "${YELLOW}[4] İzinler ayarlanıyor...${RESET}"
chmod +x shqmenu.py
chmod +x shqlib.py

echo -e "${GREEN}--------------------------------------------------${RESET}"
echo -e "${GREEN}[+] Kurulum Başarıyla Tamamlandı!${RESET}"
echo -e "${CYAN}[*] Çalıştırmak için: python3 shqmenu.py${RESET}"
echo -e "${GREEN}--------------------------------------------------${RESET}"
