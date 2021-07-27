class Car():

    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def zaveden(self):
        print('Автомобиль заведен')
    def zaglushen(self):
        print('Автомобиль заглушен')
    def god_vypuska(self):
        print(f'Автомоюиль {self.year}-го года выпуска')
    def tipe(self):
        print(f'Автомобиль типа {self.type}')
    def cvet(self):
        print(f'Автомобиль {self.color} цвета')
car = Car('Синего','Седан','2004')
car.tipe()
car.cvet()
car.god_vypuska()
