import random

class Student:
    def __init__(self,name):
        self.name=name
        self.gradness=50
        self.progress=0
        self.alive=True
        self.money=0

    def to_study(self):
        print("Time to study")
        self.progress +=0.12
        self.gradness-=3

    def to_sleep(self):
        print('I will sleep')
        self.gradness +=3

    def to_chill(self):
      if self.money>=10:
        print("Rest time")
        self.gradness +=5
        self.progress -=0.1
        self.money-=10
      else:
          print("Not enough money to chill.You must work")
          self.to_work

    def to_work(self):
        print("Time to work")
        self.money +=20
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
        if self.progress < -0.3:
            print('You need to study better')
        elif self.progress > 1:
            print('you need sleep')

    def end_of_day(self):
        print(f'Gladness = {self.gradness}')
        print(f'Progress = {round(self.progress, 2)}')
        print(f"Money = {self.money}")

    def live(self,day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f'{day:=^50}')
        print('1 - to study')
        print('2 - to sleep')
        print('3 - to chill')
        print('4 - to work')
        live_cube = (input('Enter your choice'))
        if live_cube == '1':
            print('You entered 1 variant(study)')
            self.to_study()
        elif  live_cube == '2':
            print('You entered 2 variant(sleep)')
            self.to_sleep()
        elif  live_cube == '3':
            print('You entered 3 variant(chill)')
            self.to_chill()
        elif live_cube == '4':
            print('You entered 4 variant(work)')
            self.to_work()
        else:
            print('Not correct choice.You can enter only 1 or 2 or 3 or 4')
        self.end_of_day()
        self.is_alive()

nick=Student(name='Nick')
for day in range (365):
    if nick.alive==False:
        print('Student lose')
        break
    nick.live(day)