from datetime import date,datetime
bugun = date.today()
vize_tarihi= datetime.strptime(input("Vize tarihini girin: (GG.AA.YYYY)"), "%d.%m.%Y").date()
fark = vize_tarihi - bugun
print(f"Vizeye kalan vakit {fark} gun. ")

