ogrenciName=input("Öğrencinin ismini giriniz.")
ogrenciSurname=input("Öğrencinin soyismini giriniz.")
ogrenciNumber=input("Öğrencinim numarasını giriniz.")

ogrenciler.update({
    "ogrenci":{
        "ad":ogrenciName,
        "soyad":ogrenciSurname,
        "no":ogrenciNumber
    }
})
print('*'*50)
ogrno=input("ogr no gir")

print(ogrenciler[ogrenci])