The following is the source code for the classical Vacuum Machine cleaning problem:

import sys
import time

import numpy as np


# this function is for finding the size of the location
def prod(given_list):
    given_list = np.ravel(given_list)
    product = 1
    for i in given_list:
        product *= i
    return product


class VacuumMachine:
    def __init__(self, name):
        self.name = name


class Location:
    location = np.array([])

    def __init__(self, name, shape, given_arr):
        self.name = name
        self.shape = shape
        self.size = prod(shape)
        self.location = np.array(given_arr)

    def display(self):
        print(self.location)

    def __str__(self):
        return "The name of the location is " + self.name + " with size " + str(self.size)


def clean(vm, location):
    location.display()
    for i in range(location.shape[0]):
        for j in range(location.shape[1]):
            if location.location[i][j] == 1:
                print(str(i) + "," + str(j) + " is dirty")
                print(vm.name + " is cleaning.")
                time.sleep(1)
                print("Cleaning is on process")
                time.sleep(3)
                print("Sorry, it's taking longer than usual, the cleaning will be finished soon")
                time.sleep(1)
                print(vm.name, "has cleaned your room")
                location.location[i][j] = 0
                ans = input("Do you want me to clean the next room?")
                if ans.lower() == "yes":
                    continue
                else:
                    print("Alright.")
                    sys.exit()

    location.display()


def begin():
    vm_name = input("Enter the name of the Vacuum Machine: ")
    location_name = input("Enter the location of the name: ")
    print("Enter the shape of the location: ")
    size = tuple(int(i) for i in input().split(","))
    while len(size) != 2:
        print("Sorry, the size should be entered only through 2 numbers(like 2,2 or 3,4 ")
        size = tuple(int(i) for i in input().split(","))
    print("Please enter a " + str(size) + " sized array with 1 being dirty and 0 being clear")
    arr = []
    for i in range(size[1]):
        arr.append([int(i) for i in input().split()])
    location1 = Location(location_name, size, arr)
    vm1 = VacuumMachine(vm_name)
    clean(vm1, location1)


# driver code
begin()


The following is the output for the above code:

Enter the name of the Vacuum Machine: Mini
Enter the location of the name: Hall
Enter the shape of the location:
3 3
Please enter a (3, 3) sized array with 1 being dirty and 0 being clear
0 1 1
1 1 1
1 0 1
[[0 1 1]
 [1 1 1]
 [1 0 1]]
0,1 is dirty
Mini is cleaning.
0,2 is dirty
Mini is cleaning.
1,0 is dirty
Mini is cleaning.
1,1 is dirty
Mini is cleaning.
1,2 is dirty
Mini is cleaning.
2,0 is dirty
Mini is cleaning.
2,2 is dirty
Mini is cleaning.
[[0 0 0]
 [0 0 0]
 [0 0 0]]
