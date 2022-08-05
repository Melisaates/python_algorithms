
num=[9,8,7,6,5,4,5]
print(len(num))#Dizinin uzunluğunu gösterir.
print(num.count(5))#5 sayısından kaç tane olduğunu verir.
print(num)
num.insert(0,89)#0.indise 89 rakamını ekler.
num.pop()#son indisteki yeri siler.
num.append(25)#25i sona ekler.
num.sort()#sıralama yapar.
num.reverse()#ters sıralar.
num.remove(9)#9u siler.
num.insert(len(num),9005)#son indise koyar 9005i.
print(num)
print(num.index(4))#4 rakamının indisini verir.
print(max(num))
print(min(num))
print(num[2,4])
