# 1
import math

sayi1 = int(input('=> 1.sayıyı girin:   \n'))
sayi2 = int(input('=> 2.sayıyı girin:   \n'))
sayi3 = int(input('=> 3.sayıyı girin:   \n'))

carpim = sayi1 * sayi2 * sayi3
print("3 sayının çarpımı: {}".format(carpim))

# 2
ad = input('adınızı girin:   ')
soyad = input('soyadınızı girin:  ')
no = (input('numaranızı girin:   '))

print("ad: " + ad + "\n" + "soyad: " + soyad + "\n" + "numara: " + no)

# 3
dik_kenar_1 = int(input('=> 1.dik kenar uzunluğunu girin:   \n'))
dik_kenar_2 = int(input('=> 2.dik kenar uzunluğunu girin:   \n'))

hipotenüs = (dik_kenar_1 ** 2 + dik_kenar_2 ** 2) ** 0.5

print("hipotenüs uzunluğu:  {}".format(hipotenüs))

# 4
boy = float(input('=> boyunuzu girin(m):   \n'))
kilo = int(input('=> kilonuzu girin(kg):   \n'))

bmi = (kilo) / (boy ** 2)
print("vücut kitle indeksiniz:  {}".format(bmi))

if bmi > 30:
    print("\nvücut tipiniz: obez")
elif 25 < bmi < 30:
    print("\nvücut tipiniz: fazla kilolu")
elif 18.5 < bmi < 25:
    print("\nvücut tipiniz: normal")
elif bmi < 18.5:
    print("\nvücut tipiniz: zayıf")

# 5
vize1 = int(input('=> 1.vizenizi girin:   \n'))
vize2 = int(input('=> 2.vizenizi girin:   \n'))
final = int(input('=> final notunuzu girin:   \n'))

son_not = ((vize1 * 30) / 100 + (vize2 * 30) / 100 + (final * 40) / 100)

print("dönem sonu notunuz:  {}".format(son_not))

if son_not > 90:
    print("harf notunuz: AA")
elif 90 > son_not >= 85:
    print("harf notunuz: BA")
elif 85 > son_not >= 80:
    print("harf notunuz: BB")
elif 80 > son_not >= 75:
    print("harf notunuz: CB")
elif 75 > son_not >= 70:
    print("harf notunuz: CC")
elif 70 > son_not >= 65:
    print("harf notunuz: DC")
elif 65 > son_not >= 60:
    print("harf notunuz: DD")
elif 60 > son_not >= 55:
    print("harf notunuz: FD")
else:
    print("harf notunuz: FF")

# 6
for a in range(1, 11):
    print("-" * 12)
    for b in range(1, 11):
        print(a, "x", b, "=", a * b)

# 7
toplam = 0
while (1 == 1):
    sayi = input("bir sayı girin: ")
    if sayi == 'q':
        break
    else:
        toplam += int(sayi)
        print("toplam:  {}".format(toplam))

# 8
sayi = int(input("bir sayı girin:"))

toplam = 0

for a in range(1, sayi):
    if (sayi % a == 0):
        toplam += a

if (sayi == toplam):
    print("bu sayı mükemmel bir sayıdır")
else:
    print("bu sayı mükemmel bir sayı değildir")

# 9
sayi1 = int(input("1.sayıyı girin:    "))
sayi2 = int(input("2.sayıyı girin:    "))

if (sayi1 > sayi2):
    kucuksayi = sayi2
else:
    kucuksayi = sayi1

ebob = 1
for a in range(1, kucuksayi + 1):
    if (sayi1 % a == 0) and (sayi2 % a == 0):
        if (a > ebob):
            ebob = a

print("ebob: {}".format(ebob))

# 10
sayi1 = int(input("1.sayıyı girin:    "))
sayi2 = int(input("2.sayıyı girin:    "))

if (sayi1 > sayi2):
    kucuksayi = sayi2
else:
    kucuksayi = sayi1

ebob = 1
for a in range(1, kucuksayi + 1):
    if (sayi1 % a == 0) and (sayi2 % a == 0):
        if (a > ebob):
            ebob = a

ekok = (sayi1 * sayi2) / ebob
print(ekok)


# 11

class Animals():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getWeight(self):
        return self.weight

    def setWeight(self, weight):
        self.weight = weight


class Dogs(Animals):
    def __init__(self, age, name, weight):
        super().__init__(name, age, weight)
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print("woof,woof!")

    def run(self):
        print("run fast!")


class Birds(Animals):
    def __init__(self, age, name, weight):
        super().__init__(name, age, weight)
        self.name = name
        self.age = age
        self.weight = weight

    def sing(self):
        print("quick,quick!")

    def fly(self):
        print("let's fly!")


class Horses(Animals):
    def __init__(self, age, name, weight):
        super().__init__(name, age, weight)
        self.name = name
        self.age = age
        self.weight = weight

    def run(self):
        print("run fast!")
