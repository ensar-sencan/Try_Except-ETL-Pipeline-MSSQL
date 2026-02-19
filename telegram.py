import os

from dotenv import load_dotenv
import requests

# Gizli kasayı (.env) aç
load_dotenv()

# Şifreleri kasadan güvenli bir şekilde çek
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# 2. GÖNDERİLECEK MESAJ
MESAJ = "Python'dan Telegram'a ilk veri füzemiz ulaştı. Sistem aktif! "

# 3. TELEGRAM'IN KAPISINI ÇAL (API İsteği)
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": MESAJ
}

# 4. ATEŞLE!
print(" Telegram'a mesaj gönderiliyor...")
response = requests.post(url, data=payload)

# 5. SONUCU KONTROL ET
if response.status_code == 200:
    print(" BAŞARILI! Telefonuna bak, mesaj geldi mi?")
else:
    print(f" HATA: {response.text}")