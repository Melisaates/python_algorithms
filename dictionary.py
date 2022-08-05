#225:şevval
#426:melisa
"""
#list yöntemiyle 
name=['sevval','melisa']
number=[225,426]
x=input("İsminizi giriniz \n")
print(number[name.index(x)])
"""

#dictionary yöntemiyle
number={"melisa":426,"sevval":225}
number["melisa"]=20120205045
number["yusuf"]=000
print(number[input("isminizi giriniz \n")])
print(number)