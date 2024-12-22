from functions import *

if __name__ == "__main__":
    clear_terminal()
    load_data()
    while True:
        try:
            user_selection =  Actions(int(menu()))
        except ValueError:
            clear_terminal()
            print("Fuck you!")
            continue
        clear_terminal()
        if user_selection is Actions.EXIT:exit()
        elif user_selection is Actions.ADD_CAR:add_car()
        elif user_selection is Actions.DISPLAY_CARS:dispay_cars()
        elif user_selection is Actions.DELETE_CAR:delete_car()
        elif user_selection is Actions.FIND_CAR:find_car()
        
