# 1

import random
from random import shuffle


class Cards:
    def __init__(self):
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suites = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.deck = [j + i for j in values for i in suites]

    def shuffle(self):
        if len(self.deck) != 52:
            print("there're not 52 of cards")
        shuffle(self.deck)


class Deck(Cards):
    def deal(self):
        randomcard = random.choice(self.deck)
        self.deck.remove(randomcard)
        print(randomcard)
        print(self.deck)


d = Deck()
c = Cards()
print(c.deck)
c.shuffle()
print(c.deck)
d.deal()


# 2
class Drone:
    id = 0
    coordinate_x = 0
    coordinate_y = 0
    coordinate_z = 0
    speed = 0
    load = 0
    battery = 0

    def __init__(self, id, coordinate_x, coordinate_y, coordinate_z, speed, load, battery):
        self.id = id
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.coordinate_z = coordinate_z
        self.speed = speed
        self.load = load
        self.battery = battery

    def takeOff(self):
        Drone.coordinate_y = input("enter the height of the drone:  \n")
        print("drone took off!!\ndrone's coordinates are: (", Drone.coordinate_x, ",", Drone.coordinate_y,
              ",", Drone.coordinate_z, ")")

    def returnToLaunch(self):
        Drone.coordinate_y = 0
        Drone.coordinate_x = 0
        Drone.coordinate_z = 0
        print("\ndrone returned to launch!\ndrone's coordinates are ( 0 , 0 , 0 ) now!!")

    def move(self):
        Drone.coordinate_x = input("x coordinates:  ")
        Drone.coordinate_y = input("y coordinates:  ")
        Drone.coordinate_z = input("y coordinates:  ")

        print("\ndrone took off!!\nnow drone's coordinates are \nx: ", Drone.coordinate_x, "\ny: ", Drone.coordinate_y,
              "\nz: ", Drone.coordinate_z)

    def loading(self, given_load):
        Drone.load = given_load + Drone.load
        print("\n", given_load, " load has been loaded, drone's load is: ", Drone.load, " now")

    def unloading(self, given_unload):
        Drone.load = Drone.load - given_unload
        print("\n", given_unload, " load has been unloaded, drone's load is ", Drone.load - given_unload, " now.")

    def distance_to_launch(self, x, y, z):
        distance = (((x ** 2 + y ** 2) + (z ** 2)) ** 0.5)

        print("\ndistance to the launch is", distance, "now")


class Test:
    drone_1 = Drone(887, 0, 0, 0, 50, 0, 69)
    drone_2 = Drone(888, 0, 0, 0, 30, 0, 37)
    drone_3 = Drone(889, 0, 0, 0, 40, 0, 25)
    drone_4 = Drone(890, 0, 0, 0, 70, 0, 100)

    Drone.takeOff(drone_2)
    Drone.returnToLaunch(drone_2)
    Drone.loading(drone_3, 20)
    Drone.distance_to_launch(drone_1, 3, 4, 12)


# 3
import random

randomlist = random.sample(range(1, 100000), 1000)

for i in range(len(randomlist)):
    min = i
    for j in range(i + 1, len(randomlist)):
        if randomlist[min] > randomlist[j]:
            min = j

    randomlist[i], randomlist[min] = randomlist[min], randomlist[i]

print(randomlist)

# 4
import sys


def eggDrop(n, k):
    if k == 1 or k == 0:
        return k
    if n == 1:
        return k

    min = sys.maxsize

    for x in range(1, k + 1):

        res = max(eggDrop(n - 1, x - 1),
                  eggDrop(n, k - x))
        if res < min:
            min = res

    return min + 1


n = 2
k = 10
print("Minimum number of trials in worst case with",
      n, "eggs and", k, "floors is", eggDrop(n, k))

# 5
a = int(input("bir sayı girin:   \n"))
if a % 2 == 1:
    print("girdiğiniz sayı tektir")
else:
    print("girdiğiniz sayı çifttir")
