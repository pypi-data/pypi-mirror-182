import sys
import time
import random
import numpy as np
from termcolor import cprint


pos_responses = ["yeah", "yes", "yep", "sure", "ok", "sarle poi chesko", "ya", "y"]
neg_responses = ["nope", "nah", "no", "vodhu le Bro", "avathalaki po", "n"]
d_responses = ["d", "dirt", "dirty", "not clean"]
c_responses = ["c", "clean", "cleany", "clea", "not dirty"]


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
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                if self.location[i, j] == 1:
                    cprint("dirty", "red", end=" ")
                else:
                    cprint("clean", "green", end=" ")
            print()

    def __str__(self):
        return "The name of the location is " + self.name + " with size " + str(self.size)


def clean(vm, location):
    print("The given location is")
    location.display()
    for i in range(location.shape[0]):
        for j in range(location.shape[1]):
            if location.location[i, j] == 1:
                p_str = str(i+1) + "," + str(j+1)
                cprint(p_str, "magenta", end=" ")
                print("is", end=" ")
                cprint("dirty", "red")
                print("Do you want", vm.name, "to clean the room?")
                ans = input()
                while (ans.lower() not in neg_responses) and (ans.lower() not in pos_responses):
                    cprint("Sorry I don't understand your response. Can you please answer again.", "red")
                    ans = input()
                if ans.lower() in neg_responses:
                    cprint("OK", "cyan")
                    continue
                print(vm.name + " is cleaning.")
                time.sleep(1)
                print("Cleaning is on process")
                rand_num = random.randint(1, 5)
                if rand_num >= 4:
                    time.sleep(rand_num-2)
                    print("Sorry, it's taking longer than usual, the cleaning will be finished soon")
                    time.sleep(2)
                else:
                    time.sleep(rand_num)
                print(vm.name, "has cleaned your room")
                location.location[i][j] = 0
                ans = input("Do you want me to clean the next room?")
                if ans.lower() in pos_responses:
                    continue
                elif ans.lower() in neg_responses:
                    cprint("Alright.", "cyan")
                    sys.exit()
    cprint("All the rooms are checked.", "blue")
    location.display()


def begin():
    vm_name = input("Enter the name of the Vacuum Machine: ")
    location_name = input("Enter the name of the location: ")
    print("Enter the shape of the location: ")
    while True:
        try:
            size = tuple(int(i) for i in input().split(","))
            break
        except ValueError:
            cprint("Please enter the size using ',' delimiter", "red")
            cprint("Please enter the size as (2,2),(3,3) etc")
    while len(size) != 2:
        cprint("Sorry, the size should be entered only through 2 numbers(like 2,2 or 3,4)", "red")
        size = tuple(int(i) for i in input().split(","))
    arr = np.array([[0] * size[1]]*size[0])
    for i in range(size[0]):
        for j in range(size[1]):
            print("Enter the status of the room", end=" ")
            cprint("-->", "white", end=" ")
            p_str = str(i+1) + " " + str(j+1)
            cprint(p_str, "magenta")
            print("Possible answers are ", end="")
            cprint("dirty", "red", end=" ")
            print("or", end=" ")
            cprint("clean", "green", end="")
            status = input(": ")
            while True:
                if status.lower().strip() in d_responses:
                    arr[i, j] = 1
                    print(arr[i, j])
                    break
                elif status.lower().strip() in c_responses:
                    arr[i, j] = 0
                    print(arr[i, j])
                    break
                else:
                    print("Please enter a valid status")
                    print("The status can be either \"dirty\" or \"clean\"")
                    status = input("Enter the status of the room: ")

    print(arr)
    location1 = Location(location_name, size, arr)
    vm1 = VacuumMachine(vm_name)
    clean(vm1, location1)


# driver code
begin()
