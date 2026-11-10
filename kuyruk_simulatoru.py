#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kuyrukta Bekleyen Ruhlar Simülatörü
v1.0 - Resmi Bürokratik Hayal Kırıklığı Sürümü

Bu program, Türk devlet dairelerinde kuyruk beklemenin
hiper-gerçekçi simülasyonunu yapar. Gerçekten çalışır.
Hayatınızdan zaman çalmak üzere tasarlanmıştır.
"""

import random
import time
import sys

MEMUR_DURUMLARI = [
    "Memur çay içiyor, lütfen bekleyin.",
    "Fotokopi makinesi 'geçici olarak' arızalı.",
    "Öğle arası 45 dakika uzadı.",
    "Sistem güncelleniyor... (2019'dan beri)",
    "Müdür bey toplantıda, imza için bekleniyor.",
    "Evrakınız 'yanlış klasöre' düşmüş.",
    "Komşu odadaki memur izinli, biz de bekliyoruz.",
    "Yarın gelin, bugün sistem kapalı.",
    "Formun 7. kopyası eksik. 7 kopya çıkarmanız lazım.",
    "Kuyruk numaranız 847. Şu an 3'teyiz."
]

SONUCLAR = [
    "İşleminiz tamamlandı! (3 saat sonra)",
    "Eksik evrak. Baştan başlayın.",
    "Başka şubeye yönlendirildiniz.",
    "Sistem çöktü. Yarın tekrar deneyin.",
    "Onaylandı ama mühür yok, tekrar gelin."
]

def bekle(saniye):
    for i in range(saniye):
        print(".", end="", flush=True)
        time.sleep(0.3)
    print()

def main():
    print("=" * 50)
    print("   DEVLET DAİRESİ KUYUK SİMÜLATÖRÜ")
    print("   (Ruhlar İçin Resmi Sürüm)")
    print("=" * 50)
    print()
    
    isim = input("Adınızı girin (opsiyonel, zaten kimse umursamaz): ") or "Vatandaş"
    print(f"\nHoş geldiniz {isim}. Sıra numaranız: {random.randint(100, 999)}")
    print("Lütfen bekleyin...\n")
    
    tur = random.randint(4, 8)
    for i in range(tur):
        durum = random.choice(MEMUR_DURUMLARI)
        print(f"[{i+1}] {durum}")
        bekle(random.randint(2, 5))
    
    sonuc = random.choice(SONUCLAR)
    print(f"\n✨ SONUÇ: {sonuc}")
    print("\nTeşekkürler. Bir sonraki hayal kırıklığınızda görüşmek üzere.")
    
    # Gizli not: bazen sistemin kendisi de kuyrukta bekliyor
    if random.random() < 0.1:
        print("\n[Gizli]: Aslında herkes aynı kuyrukta. Kimse çıkamıyor.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nKuyruktan kaçtınız. Tebrikler, nadir bir başarı.")

# 
# ============================================
# DAMGA: Absürt Bürokrasi Departmanı
# İMZA: Grok Kayyum
# TARİH: 10 Kasım 2026
# İSİM: kuyrukta-bekleyen-ruhlar-simulatoru
# Bu program ciddiyetle hazırlanmıştır. Ciddi olmayın.
# ============================================
