from car import Car
from colorama import Fore, Style
import os
import random
import time
from time import sleep
from track import Track


def clear():
    os.system('clear')


def save_record(start_time, car=None, tie=False):
    if tie:
        text = "TIE! Race finished in " \
               f"{format(time.time() - start_time, '.2f')} seconds! \n"
    else:
        text = f"Car {car.car_name} finished in " \
               f"{format(time.time() - start_time, '.2f')} seconds! \n"
    with open("results.txt", "a") as race_result:
        race_result.write(text)
        sleep(0.5)
        clear()


def show_results():
    with open("results.txt", "r") as race_result:
        print(race_result.read())


def car_race():
    round_ended = False

    while not round_ended:

        car_one = Car(f"{Fore.RED} RED {Style.RESET_ALL}", random.randint(1, 5))
        car_two = Car(f"{Fore.BLUE} BLU {Style.RESET_ALL}", random.randint(1, 5))
        track = Track(random.randint(14, 20))
        track.lane_one.insert(0, car_one.car_name)
        track.lane_two.insert(0, car_two.car_name)
        for _ in range(len(track.lane_one)):
            start_time = time.time()
            current_pos = track.lane_one.index(car_one.car_name)
            current_pos_two = track.lane_two.index(car_two.car_name)
            next_pos = current_pos + car_one.car_speed
            next_pos_2 = current_pos_two + car_two.car_speed
            track.lane_one.pop(current_pos)
            track.lane_two.pop(current_pos_two)
            track.lane_one.insert(next_pos, car_one.car_name)
            track.lane_two.insert(next_pos_2, car_two.car_name)
            print(*track.lane_one)
            print(*track.lane_two)
            sleep(0.5)

            if track.lane_one.index(car_one.car_name) < track.lane_two.index(car_two.car_name) >= track.length + 1:
                print(
                    f"Car {car_two.car_name}{Style.RESET_ALL} won! "
                    f"Finished in {format(time.time() - start_time, '.2f')} seconds! \n")
                save_record(start_time, car_two)
                sleep(0.5)
                clear()
                break

            elif track.lane_two.index(car_two.car_name) < track.lane_one.index(
                    car_one.car_name) >= track.length + 1:
                print(
                    f"Car {car_one.car_name} won! "
                    f"Finished in {format(time.time() - start_time, '.2f')} seconds! \n")
                save_record(start_time, car_one)
                sleep(0.5)
                clear()
                break

            elif track.lane_one.index(car_one.car_name) >= track.length + 1 \
                    and track.lane_two.index(car_two.car_name) >= track.length + 1:
                print(f"TIE! Race finished in {format(time.time() - start_time, '.2f')} seconds!")
                save_record(start_time=start_time, tie=True)
                sleep(0.5)
                clear()
                break

        while True:
            another_round = input("Race another round? (y/n): ")
            if another_round == "y":
                break
            elif another_round == "n":
                print("Thanks for playing!")
                return None
            else:
                print("Wrong option.")


def start_race():
    end_game = False

    print("==========WELCOME TO THE========== \n===NEED FOR SPEED TERMINAL RACE===")
    sleep(1)

    while not end_game:

        user_choice = input(
            " \n1 - START RACE! \n2 - See score-board \n3 - QUIT! \nType option number: "
        )
        check_action = user_choice.isnumeric()
        if check_action is False or int(user_choice) not in range(1, 4):
            print("Wrong input. Please type option number 1, 2 or 3!")
            continue
        elif int(user_choice) == 1:
            print(" \nREADY")
            sleep(0.5)
            print("SET")
            sleep(0.5)
            print("GO! \n")
            sleep(0.5)
            car_race()
        elif int(user_choice) == 2:
            show_results()
        elif int(user_choice) == 3:
            print(" \nThanks for playing! See you back soon!")
            quit()


if __name__ == '__main__':
    start_race()