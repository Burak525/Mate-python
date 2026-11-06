def harf_notu_hesapla(v,f):
    ort= ((v*4)+(f*6))/10
    if ort>=90:
     print(f"Ogrencinin ortalamasi {ort} ve harf notu AA")
    elif ort<90 and ort>=80:
     print(f"Ogrencinin ortalamasi {ort} ve harf notu BA")
    elif ort<80 and ort>=70:
     print(f"Ogrencinin ortalamasi {ort} ve harf notu BB")
    elif ort<70 and ort>=60:
     print(f"Ogrencinin ortalamasi {ort} ve harf notu CB")
    elif ort<60 and ort>=50:
     print(f"Ogrencinin ortalamasi {ort} ve harf notu CC")
    elif ort<50 and ort>=45:
     print(f"Ogrencinin ortalamasi {ort} ve harf notu DC")
    elif ort<45 and ort>=40:
     print(f"Ogrencinin ortalamasi {ort} ve harf notu DD")
    else :
     print(f"Ogrencinin ortalamasi {ort} ve harf notu FF")

v = int(input("Vize notunuzu girin:"))
f = int(input("Final notunuzu girin:"))
harf_notu_hesapla(v,f)