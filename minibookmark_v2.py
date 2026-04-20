import os

# --- V2 HEDEFLERİ ---
# 1. 'last' komutu: En son eklenen kaydı gösterir.
# 2. 'search' komutu: Kitap ismine göre arama yapar.
# 3. 'delete' komutu: Kayıt dosyasını temizler.

DB_PATH = ".bookmarks/marks.dat"

def init_system():
    if not os.path.exists(".bookmarks"):
        os.makedirs(".bookmarks")
    if not os.path.exists(DB_PATH):
        with open(DB_PATH, "w") as f:
            pass
    print("Sistem hazır.")

def add_bookmark(name, page):
    # V1'deki Sayı Kontrolü
    if not page.isdigit():
        print(f"HATA: '{page}' geçerli bir sayfa numarası değil!")
        return
    
    with open(DB_PATH, "a") as f:
        f.write(f"{name} | Sayfa: {page}\n")
    print(f"BAŞARIYLA KAYDEDİLDİ: {name} (Sayfa: {page})")

def list_bookmarks():
    if not os.path.exists(DB_PATH) or os.stat(DB_PATH).st_size == 0:
        print("Listeniz şu an boş. Önce bir kitap ekleyin.")
        return
    
    print("--- GÜNCEL KİTAP LİSTENİZ ---")
    with open(DB_PATH, "r") as f:
        print(f.read())

# --- V2 YENİ ÖZELLİKLER ---

def show_last(): # Hedef 1
    with open(DB_PATH, "r") as f:
        lines = f.readlines()
        if lines:
            print(f"En son eklenen: {lines[-1].strip()}")
        else:
            print("Kayıt bulunamadı.")

def search_bookmark(query): # Hedef 2
    with open(DB_PATH, "r") as f:
        lines = f.readlines()
        found = False
        for line in lines:
            if query.lower() in line.lower():
                print(f"Bulundu: {line.strip()}")
                found = True
        if not found:
            print(f"'{query}' ile ilgili bir kayıt bulunamadı.")

# --- ANA PROGRAM DÖNGÜSÜ ---
init_system()
while True:
    islem = input("\n[add, list, last, search, delete, q]: ").lower()
    
    if islem == 'add':
        n = input("Kitap adı: ")
        p = input("Sayfa: ")
        add_bookmark(n, p)
    elif islem == 'list':
        list_bookmarks()
    elif islem == 'last':
        show_last()
    elif islem == 'search':
        q = input("Aranacak kitap adı: ")
        search_bookmark(q)
    elif islem == 'delete':
        with open(DB_PATH, "w") as f: pass # Dosyayı boşaltır
        print("Tüm liste temizlendi!")
    elif islem == 'q':
        break