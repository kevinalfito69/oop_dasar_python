class Hero():
    def __init__(self, namaHero, power):# __init akan di eksekusi pertama kali saat object di buat, self  ini sebenarnya adalah sebagai sebuah variabel saja yang yang menyatakan kelas itu sendiri.
        self.name = namaHero
        self.power = power

hero1 = Hero('eudora','lightning')
hero2 = Hero('vale','wind')

print(hero1.__dict__)
print(hero2.__dict__)   