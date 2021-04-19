# Inheritance method (single-lvl inheritance)
class animal:
    def eat(self):
        print("eating")

class dog(animal):
    def bark(self):
        print("barking")
d=dog()
d.bark()
d.eat()


# Inheritance method (multi-lvl inheritance)
class animal:
    def eat(self):
        print("eating")

class dog(animal):
    def bark(self):
        print("barking")

class puppy(dog):
    def scream(self):
        print("screaming")


opuppy=puppy()
opuppy.scream()
opuppy.eat()
opuppy.bark()

# Inheritance method (multiple inheritance)
class landanimal:
    def jumps_land(self):
     print("This is a land animal")
class wateranimal:
    def dip_water(self):
     print("This is water animal")
class frog(landanimal,wateranimal):
    def jump(self):
        print("Jumps from land into water")

ofrog=frog()
ofrog.jumps_land()
ofrog.dip_water()
ofrog.jump()
