#L: Sustitución de Liskov. Los objetos de una subclase deben poder reemplazar a los objetos de su superclase sin alterar el programa.
class Bird:
    def fly(self):
        return "I can fly"

class Sparrow(Bird): #Sparrow hereda de Bird. Bird es su Superclase. Todos los Birds deberían volar.
    def fly(self):
        return "Sparrow flying"

class Penguin(Bird):
    def fly(self):
        # el penguin no vuela, no cumple el principio
        raise Exception("I fly not")

def make_bird_fly(bird: Bird):
    print(bird.fly())

sparrow = Sparrow()
make_bird_fly(sparrow) #el sparrow si vuela, cumple el principio

penguin = Penguin()
make_bird_fly(penguin)