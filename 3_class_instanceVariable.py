class Hero:
    # class Variabel
    jumlahHero = 0
    def __init__(self, namaHero, power):# __init akan di eksekusi pertama kali saat object di buat, self  ini sebenarnya adalah sebagai sebuah variabel saja yang yang menyatakan kelas itu sendiri.
        # Instance Variable
        self.name = namaHero
        self.power = power
        print('Membuat hero dengan nama' + self.name)
        print('Membuat hero dengan power' + self.power)
        print('jumlah Hero yang telah dibuat ')
        Hero.jumlahHero += 1
        

hero1 = Hero('eudora','lightning')
hero2 = Hero('vale','wind')

print(hero1.__dict__)
print(Hero.jumlahHero)
print(hero2.__dict__)   
print(Hero.jumlahHero)