import random

class Hat:
    houses = ["Gryffindor","Hufflepuff","Ravenclow","Slytherin"]

    @classmethod
    def sort(cls,name):
        print(name," is in ", random.choice(cls.houses))

Hat.sort("Ron")