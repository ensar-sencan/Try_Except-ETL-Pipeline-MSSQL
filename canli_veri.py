import requests
import pandas as pd
import sqlalchemy
import urllib
import time # Zamanı kontrol etmek için
from datetime import datetime

# --- AYARLAR ---
Server = r'.\SQLEXPRESS05' # Senin sunucu adın
Database = 'DogusStaj'
Driver = 'ODBC Driver 17 for SQL Server'
Tablo_Adi = 'Kripto_Fiyatlari'

# Bağlantı Motorunu Kur (Döngünün dışında 1 kere kurmak yeterli)
conn_str = f'DRIVER={{{Driver}}};SERVER={Server};DATABASE={Database};Trusted_Connection=yes;'
quoted_conn_str = urllib.parse.quote_plus(conn_str)
engine = sqlalchemy.create_engine(f'mssql+pyodbc:///?odbc_connect={quoted_conn_str}')

print("🚀 KRİPTO TAKİP BOTU BAŞLATILIYOR...")
print("Her 5 saniyede bir veri çekecek. Çıkmak için CTRL+C yapabilirsin.\n")

# --- SONSUZ DÖNGÜ (veya Sayılı) ---
for i in range(1, 61): # 60 kere çalışsın (Yaklaşık 5 dakika sürer)
    try:
        # 1. Veriyi Çek
        url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        response = requests.get(url)
        veri = response.json()
        
        # 2. Veriyi Hazırla
        fiyat = float(veri['price'])
        tarih = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        df = pd.DataFrame([{
            'Sembol': veri['symbol'],
            'Fiyat': fiyat,
            'Tarih': tarih
        }])
        
        # 3. SQL'e Bas
        df.to_sql(Tablo_Adi, con=engine, if_exists='append', index=False)
        
        print(f"[{i}/60] ✅ {tarih} - BTC: {fiyat} $ -> Kaydedildi.")
        
        # 4. Bekle (5 Saniye)
        time.sleep(5)
        
    except Exception as e:
        print(f"❌ Hata oluştu: {e}")
        time.sleep(5) # Hata alsa bile 5 saniye bekle, durma

print("\n🏁 GÖREV TAMAMLANDI! Veritabanı veriye doydu.")