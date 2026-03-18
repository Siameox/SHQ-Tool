# ⚡ SHQ-Tool v2.0 - All-in-One OSINT & Pentest Suite

SHQ-Tool, siber güvenlik araştırmacıları ve sızma testi uzmanları için geliştirilmiş, Python tabanlı, modüler bir istihbarat ve analiz aracıdır. Termux ve Linux sistemlerde sorunsuz çalışacak şekilde optimize edilmiştir.

## 🚀 Özellikler (Features)
* **[NEW] Data Breach Checker:** E-posta adreslerinin dünya çapındaki büyük veri sızıntılarında (COMB) yer alıp almadığını sorgular.
* **Native OSINT Engine:** Kullanıcı adından 10+ popüler sosyal medya platformunda (Instagram, GitHub, Telegram vb.) otomatik tarama yapar.
* **Network Analysis:** Nmap entegrasyonu ile hızlı ve derinlemesine port/servis taraması sağlar.
* **IP Intelligence:** IP adresi üzerinden detaylı konum, ISP ve altyapı verisi toplar.
* **Email Hunting:** Holehe motoru ile e-posta adresi üzerinden sosyal medya hesaplarını keşfeder.
* **Web Security:** HTTP Header analizi ile sunucu bilgilerini okur ve Phishing (Oltalama) linklerini kontrol eder.
* **Professional Disclaimer:** Kurumsal standartlarda yasal uyarı ekranı ve 2 saniyelik sistem yükleme simülasyonu.

## 🛠️ Kurulum (Installation)
Projenin tüm bağımlılıklarını (Python, Requests, Nmap, Holehe) tek bir komutla otomatik yüklemek için:

```bash
git clone [https://github.com/Siameox/SHQ-Tool.git](https://github.com/Siameox/SHQ-Tool.git)
cd SHQ-Tool
chmod +x setup.sh
./setup.sh
