import time

from termcolor import cprint
from termcolor import colored
from location import Location 


def move_human(location1, location2):
    if location1.humans == 0:
        return
    location1.decrease_human()
    location2.increase_human()


def move_monster(location1, location2):
    if location1.monsters == 0:
        return
    location1.decrease_monster()
    location2.increase_monster()


def best_choice(location1, location2, choice):
    if choice == 1:
        if (location1.humans-1) >= location1.monsters or location1.humans-1 == 0:
            return "h"
        else:
            return "m"
    else:
        if (location1.humans+1) >= location1.monsters and location2.humans > 0:
            return "h"
        else:
            return "m"


def fill_boat(location1, location2, mode_of_transport):
    if mode_of_transport.size() == mode_of_transport.capacity:
        return
    elif location1.size() == 0:
        move_human(mode_of_transport, location2)
        move_monster(mode_of_transport, location2)
    else:
        if best_choice(location1, location2, 1) == "h":
            move_human(location1, mode_of_transport)
            fill_boat(location1, location2, mode_of_transport)
        else:
            move_monster(location1, mode_of_transport)
            fill_boat(location1, location2, mode_of_transport)


def transverse_boat(location1, mode_of_transport):
    if best_choice(location1, mode_of_transport, 2) == "m":
        move_monster(mode_of_transport, location1)
    else:
        move_human(mode_of_transport, location1)


def return_boat(location1, location2, mode_of_transport):
    print("L1:", location1.str())
    print("L2", location2.str())
    print("B", mode_of_transport.str())


def print_instance(location1, location2, mode_of_transport):
    m = "M"
    h = "H"
    cprint(location1.name, "cyan")
    cprint(m * location1.monsters, "red")
    cprint(h * location1.humans, "green")
    cprint(mode_of_transport.name, "cyan")
    cprint(m * mode_of_transport.monsters, "red")
    cprint(h * mode_of_transport.humans, "green")
    cprint(location2.name, "cyan")
    cprint(m * location2.monsters, "red")
    cprint(h * location2.humans, "green")

    cprint("-------------------------------------------------------------------------", "white")


def start_movement(location1, location2, mode_of_transport, i):
    if location1.size() == mode_of_transport.size() == 0:
        print(i)
    else:
        i += 1
        time.sleep(1)
        fill_boat(location1, location2, mode_of_transport)
        transverse_boat(location2, mode_of_transport)
        print_instance(location1, location2, mode_of_transport)
        # return_boat(location1, location2, mode_of_transport)
        start_movement(location1, location2, mode_of_transport, i)


def move_all(location1, location2, mode_of_transport):
    start_movement(location1, location2, mode_of_transport, 0)


def begin():
    text = colored("Welcome to Missionary and Cannibal simulation", "red", attrs=["reverse", "blink"])
    print(text)
    while True:
        try:
            number_of_missionary = int(input("Enter the number of Missionaries you want to transport:"))
            number_of_cannibal = int(input("Enter the number of Cannibals you want to transport:"))
        except:
            cprint("Please enter a single positive non-zero integer","red")
        else:
            break        
    while number_of_cannibal > number_of_missionary:
        cprint("The given inputs are not valid.", "red")
        cprint("Please make sure missionaries count is greater than or equal to cannibals count.", "red")
        number_of_missionary = int(input("Enter the number of Missionaries you want to transport:"))
        number_of_cannibal = int(input("Enter the number of Cannibals you want to transport:"))
    total_count = number_of_cannibal + number_of_missionary
    location1 = Location("Shore1", number_of_missionary, number_of_cannibal, total_count)
    location2 = Location("Shore2", 0, 0, total_count)
    boat = Location("Boat", 0, 0, 2)
    # return_boat(L1, L2, B)
    cprint("-------------------------------------------------------------------------", "white")
    print_instance(location1, location2, boat)
    move_all(location1, location2, boat)


# driver code
begin()
