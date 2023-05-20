import random

class Student:
    def __init__(self,name):
        self.name=name
        self.gradness=50
        self.progress=0
        self.alive=True

    def to_dtudy(self):
        print("Time to study")
        self.progress +=0.12
        self.gradness-=3

    def to_sleep(self):
        print('I will sleep')
        self.gradness +=3

    def to_chill(self):
        print("Rest time")
        self.gradness +=5
        self.progress -=0.1

    def is_alive(self):
        if self.progress < -0.5:
            print('Cast out...')
            self.alive= False

        elif self.gradness <= 0:
            print('depression...')
            self.alive = False

        elif self.progress > 5:
            print('Passed externally...')
            self.alive=False



