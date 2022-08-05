
m="melisa ateş  "

print(m.upper())#büyük harfe çevirir.
print(m.lower())#küçük harfe çevirir.
print(m.capitalize())#en baştaki harfi büyüğe çevirir sadece.
print(m.title())#tüm kelimelerin baş harflerini büyüğe çevirir.
print(m.center(100))#sağ ve soldan eşit boşluklar bırakarak stringi yerleştirir.
print(m.split())#m.split('.')=>noktalardan ayırır.
x=m.split()
print(m.strip())#baş ve sondaki boşlukları siler.
y='*'.join(m)#splitle ayrılan cümleyi birleştirerek araya yıldız koyar.
print(y)

