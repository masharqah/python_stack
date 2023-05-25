class Animal:
    def __init__(self, name, age, health, happiness):
        self.name= name
        self.age= age
        self.health= health
        self.happiness=happiness

    def display_info(self):
        print(f"Name: {self.name}\n Age: {self.age} \n Health: {self.health} \n Happiness: {self.happiness}")

    def feed(self):
        self.happiness += 10
        self.health += 10

class Lion(Animal):
    def __init__(self, name, age ):
        super().__init__(name, age, health=70, happiness=70)
        self.color_of_hair= "brown"

    def play_catch(self):
        print(f"Lion Played catch, what an animal")

class Tiger(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health=40, happiness=30)
        self.attitude= True
    
    def paly_run(self):
        print("Tiger is runnig!")

class Bear(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health=20, happiness=10)
        self.weight= 500
    
    def paly_dance(self):
        print("Bear is dancing")

class Zoo:
    def __init__(self, title):
        self.title= title
        self.animals=[]

    def add_animal(self, animal):
        self.animals.append(Animal)
        print(f"{animal.name} added")



lion1= Lion("simba", 9)
print(f"{lion1.name} has health level of {lion1.happiness}")
lion1.feed()
print(f"{lion1.name} has health level of {lion1.health} and Happiness of {lion1.happiness}")
zoo=Zoo("Qalqilia")
zoo.add_animal(lion1)c



    

