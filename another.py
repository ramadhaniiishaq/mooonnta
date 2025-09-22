class Hero:
    Energi=100
    def __init__(self,value_name, value_power):
        self.name=value_name
        self._power=value_power
    
    def set_health(self,value_health):#setter
        self.__health=value_health
        
    def get_health(self):#getter
        Jinan.set_health(200)
        return self.__health
    
    def menyerang(self,obj_hero):
        
        print(f"{self.name} menyerang {obj_hero.name}")
        obj_hero.kurang_health(self)
        
    def kurang_health(self,obj_hero):
        print(f"Health dari {self.name} tersisa {self.health}")
        
    def tampilkan_data(self):
        print(f"nama : {self.name}") 
        print(f"health : {self.__health}")
        print(f"power : {self._power}")
        
        
class Fighter(Hero):
    def __init__ (self,value_name,value_power,value_damage):
        Hero.__init__(self,value_name,value_power)
        self.damage=value_damage
                
    def tampilkan_data(self):
        print(f"nama: {self.name}") 
        print(f"health: {self.get_health()}")
        print(f"power: {self._power}")
        print(f"dammage: {self.damage}")
        
        
    
Ainun=Fighter("Ainun",100,15)
Jinan=Fighter("Jinan",100,15)
Ainun.set_health(f"150")
print(Ainun.get_health())
Ainun.tampilkan_data()
Jinan.tampilkan_data()