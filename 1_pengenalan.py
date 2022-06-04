class Hero: #template
    pass
hero1 = Hero() #Object / INstance
hero2 = Hero()

hero1.nama      = 'eudora'  
hero1.health    = 10000
hero1.power     = 'thunder'

hero2.name      ='vale'        
hero2.health    = 100
hero2.power     ='wind'

print(hero1) #mencetak object
print(hero1.nama) #mencetak isi object
print(hero1.__dict__)