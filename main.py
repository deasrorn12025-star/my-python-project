import requests

def valyuta_konvertori():
    print("=" * 45)
    print("   AQLLI VALYUTA KONVERTORI (USD <-> UZS)   ")
    print("=" * 45)
    
    # NBU (Milliy bank) API-sidan real vaqtda dollar kursini olish
    url = "https://nbu.uz"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Dollar kursini qidirib topish
        usd_kurs = None
        for currency in data:
            if currency['code'] == 'USD':
                usd_kurs = float(currency['nbu_cell_price'])
                break
        
        if not usd_kurs:
            print("Xatolik: Dollar kursi topilmadi, standart kurs (12800) ishlatiladi.")
            usd_kurs = 12800.0
            
        print(f"Bugungi rasmiy USD kursi: 1 $ = {usd_kurs} so'm\n")
        
    except Exception:
        print("Internetga ulanishda xatolik! Standart kurs (12800) ishlatiladi.")
        usd_kurs = 12800.0

    # Foydalanuvchidan tanlovni so'rash
    print("1. Dollardan So'mga o'girish (USD -> UZS)")
    print("2. So'mdan Dollarga o'girish (UZS -> USD)")
    tanlov = input("\nYo'nalishni tanlang (1 yoki 2): ")

    if tanlov == "1":
        usd = float(input("Dollar miqdorini kiriting ($): "))
        uzs = usd * usd_kurs
        print(f"\nNatija: {usd}$ = {uzs:,.2f} so'm")
    elif tanlov == "2":
        uzs = float(input("So'm miqdorini kiriting (UZS): "))
        usd = uzs / usd_kurs
        print(f"\nNatija: {uzs:,.2f} so'm = {usd:,.2f} $")
    else:
        print("Xato tanlov kiritildi!")

if __name__ == "__main__":
    valyuta_konvertori()
