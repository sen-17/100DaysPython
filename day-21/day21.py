# Class Inheritence
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale" , "Exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Doing this underwater")

    def swim(self):
        print("Moving in water")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)

# How to slice lists and tuples
piano_keys = ["a" , "b" , "c" , "d" , "e", "f" , 'g']
piano_keys[2:5] # slicing from position 2 to 5, Output : ['c , 'd , 'e]
piano_keys[2:5:2] # Output : ['c', 'e']
piano_keys[::2] # skip every second one
piano_keys[::-1] # reversing a list