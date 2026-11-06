def indirim_hesapla(a,b):
    indirim= a*b/100
    sonuc= a-indirim
    print(f"Indirim tutari {indirim}")
    print(f"Son fiyat {sonuc}")

a = int(input("Urun fiyatini girin:"))
b = int(input("Indirim yuzdesini girin:"))
indirim_hesapla(a,b)