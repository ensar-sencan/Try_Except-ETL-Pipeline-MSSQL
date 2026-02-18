@echo off
:: 1. ADIM: Proje Klasörüne Git
cd /d "C:\Users\Ensar\veri_muhendisligi_yolculugum\TRY-EXCEPT"

:: 2. ADIM: Log Dosyasının Yerini Belirle
set LOG_FILE=etl_gunlugu.txt

:: 3. ADIM: KRİTİK AYAR - Emojileri Destekle (UTF-8)
set PYTHONIOENCODING=utf-8

echo --------------------------------------------------- >> %LOG_FILE%
echo [BASLANGIC] Tarih: %date% Saat: %time% >> %LOG_FILE%

:: 4. ADIM: Python'ı Çalıştır
"C:\Users\Ensar\anaconda3\python.exe" "etl_pro.py" >> %LOG_FILE% 2>&1

:: Hata Kontrolü
if %ERRORLEVEL% EQU 0 (
    echo [DURUM] BASARILI! >> %LOG_FILE%
) else (
    echo [DURUM] HATA OLUSTU! Kod: %ERRORLEVEL% >> %LOG_FILE%
)

echo [BITIS] Tarih: %date% Saat: %time% >> %LOG_FILE%
echo --------------------------------------------------- >> %LOG_FILE%

:: Ekranda görmek için bekle
timeout /t 5