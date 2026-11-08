import random

a=random.randint(1,100)
i=0
while i != a:
    i=int(input("Tahmininizi girin:"))
    if i<a:
        print("YUKARI CIK")
        print()
    elif i>a:
        print("ASAGI IN")
        print()
    else:
        break        

print("Dogru tahmin ettiniz.")