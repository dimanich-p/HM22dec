import json
from enum import Enum
import os
from colorama import Fore, Style


cars = {}       
def load_data():
    global cars
    try:
        with open('cars.json', 'r') as file:
            cars = json.load(file)
            file.close()
    except FileNotFoundError:
        print("File not found")
    except(SyntaxError, ValueError):
         print("File not supported")
    

class FindingAction(Enum):
    BRAND = 1
    MODEL = 2
    COLOR = 3
    ID = 4
    EXIT = 5

class Actions(Enum):
    EXIT = 1
    ADD_CAR = 2
    DISPLAY_CARS = 3
    DELETE_CAR = 4
    FIND_CAR = 5

def menu():
    for act in Actions:
        print(Fore.BLUE + f"{act.value} - {act.name}")
    return input(Fore.GREEN + "Your selection: " + Style.RESET_ALL)

def add_car():
    while True:
        brand = input(f"Enter x to cancel\n{Fore.GREEN}Brand: {Style.RESET_ALL}")
        if brand == "x":
            clear_terminal()
            break
        model = input(f"Enter x to cancel\n{Fore.GREEN}Model: {Style.RESET_ALL}")
        if model == 'x':
            clear_terminal()
            break
        color = input(f"Enter x to cancel\n{Fore.GREEN}Color: {Style.RESET_ALL}")
        if color == 'x':
            clear_terminal()
            break
        cars["mycars"].append({"id":len(cars["mycars"])+1,"brand":brand, "model":model,"color":color})
        save_to_file()
        load_data()
        clear_terminal()
        dispay_cars()
        break

def dispay_cars():
    for car in cars["mycars"]:
        print_car(car)

def delete_car():
    while True:
        try:
            dispay_cars()
            user_selection = int(input(f"{Fore.RED}Enter ID to delete(0 to cancel): {Style.RESET_ALL}"))
            if user_selection == 0:
                clear_terminal()
                break
            for index,car in enumerate(cars["mycars"]):
                valid_id_checker = False
                if user_selection == car["id"]:
                    del cars["mycars"][index]
                    valid_id_checker = True
                    break
            if not valid_id_checker: 
                clear_terminal()
                print(f"{Fore.RED}Enter a valid ID!{Style.RESET_ALL}")
            else:
                for index,car in enumerate(cars["mycars"]):car["id"] = index + 1 
                save_to_file()
                load_data()
                dispay_cars()
                break
            
        except ValueError:
            clear_terminal()
            print("Fuck you!")
            continue

def print_car(car):
    print(f"ID:{car["id"]}  {Fore.YELLOW}brand:{Fore.CYAN}{car["brand"]} {Fore.YELLOW}model:{Fore.CYAN}{car["model"]}, {Fore.YELLOW}color:{Fore.CYAN}{car["color"]}{Style.RESET_ALL}")

def find_menu():
    print(f"{Fore.BLUE}Finding creteria{Style.RESET_ALL}")
    for act in FindingAction:
        print(Fore.BLUE + f"{act.value} - {act.name}")
    return input(Fore.GREEN + "Your selection: " + Style.RESET_ALL)

def clear_terminal():
    os.system("cls")

def save_to_file():
    with open('cars.json', 'w') as file:
        json.dump(cars, file, indent=4)
    file.close()

def find_car():
    while True:
        try:
            user_selection =  FindingAction(int(find_menu()))
        except ValueError:
            clear_terminal()
            print("Fuck you!")
            continue
        if user_selection is FindingAction.EXIT:
            clear_terminal()
            break

        elif user_selection is FindingAction.ID:
            while True:
                try:
                    choosenID = int(input("Enter an ID: "))
                    break
                except ValueError:
                    print(f"{Fore.RED} Enter a number {Style.RESET_ALL}")     
            found = False
            for car in cars["mycars"]:
                if choosenID == car["id"]:
                    found = True
                    print_car(car)
                    break
            if not found:
                print(f"{Fore.RED}Enter a valid ID!{Style.RESET_ALL}")
                continue

        elif user_selection is FindingAction.BRAND:
            choosen_brand = input("Enter a brand: ")
            found = False
            for car in cars["mycars"]:
                if choosen_brand == car["brand"]:
                    found = True
                    print_car(car)
            if not found:print(f"{Fore.RED}Nothing found! {Style.RESET_ALL}")

        elif user_selection is FindingAction.MODEL:
            choosen_model = input("Enter a model: ")
            found = False
            for car in cars["mycars"]:
                if choosen_model == car["model"]:
                    found = True
                    print_car(car)
            if not found:print(f"{Fore.RED}Nothing found! {Style.RESET_ALL}")
        
        elif user_selection is FindingAction.COLOR:
            choosen_color = input("Enter a color: ")
            found = False
            for car in cars["mycars"]:
                if choosen_color == car["color"]:
                    found = True
                    print_car(car)
            if not found:print(f"{Fore.RED}Nothing found! {Style.RESET_ALL}")
        break