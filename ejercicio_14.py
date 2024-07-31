# challenge ---> Polimorfismo: Crea una clase base Animal con un método hacerSonido y una clase derivada Perro que sobrescriba este método.

class Animal:
    def hacer_sonido(self):
        print("El animal hace un sonido")

class Perro(Animal):
    def hacer_sonido(self):
        print("El perro ladra")

animal = Animal()
perro = Perro()

animal.hacer_sonido() 
perro.hacer_sonido()   
