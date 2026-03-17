#!/bin/bash

echo -e "\033[1;35m[*] SHQ-Tool Kurulumu Başlatılıyor...\033[0m"

# 1. Sistem Paketlerini Güncelle ve Gerekli Araçları Kur
pkg update -y && pkg upgrade -y
pkg install python nmap curl git -y

# 2. Python Kütüphanelerini Kur (En Önemli Kısım)
# Requests: Yeni OSINT motorun için şart
# Holehe: E-posta sorgulama için şart
pip install requests holehe

# 3. Yetkilendirme
chmod +x shqmenu.py

echo -e "\033[1;32m[+] Kurulum Tamamlandı! \033[0m"
echo -e "\033[1;33m[*] Çalıştırmak için: python3 shqmenu.py\033[0m"
