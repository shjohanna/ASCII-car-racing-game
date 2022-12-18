from car import Car
from colorama import Fore, Style
import csv
import os
import random
import time
from time import sleep
from track import Track

#  file where the game results will be stored
results_file = "results.csv"


def clear():
    os.system('clear')


# function for saving game results
def save_record(start_time, car=None, tie=False):
    high_score = []

    if tie:
        timing = float(f"{format(time.time() - start_time, '.2f')}")
        winner = "TIE"
        score = [timing, winner]
        high_score.append(score)
    else:
        timing = float(f"{format(time.time() - start_time, '.2f')}")
        winner = car.car_name
        score = [timing, winner]
        high_score.append(score)

    with open(results_file, "a") as results:
        writer = csv.writer(results)
        for line in high_score:
            writer.writerow(line)

    with open(results_file, "a+") as results:
        reader = csv.reader(results)
        for line in reader:
            high_score.append(line)
        high_score.sort(key=lambda x: float(x[0]))


# function for presenting the stored game results in Terminal
def show_results():
    with open(results_file, "r") as results:
        print(results.read())


# function for quitting the game and clearing the saved game results
def quit_game():
    with open(results_file, 'w') as results:
        high_score = []
        w = csv.writer(results)
        for row in high_score:
            w.writerow(row)

    print(" \nThanks for playing! See you back soon!")
    quit()


# the game
def car_race():
    print(" \nREADY")
    sleep(0.5)
    print("SET")
    sleep(0.5)
    print("GO! \n")
    sleep(0.5)

    round_ended = False

    while not round_ended:
        start_time = time.time()
        car_one = Car(f"{Fore.RED} RED {Style.RESET_ALL}", random.randint(1, 5))
        car_two = Car(f"{Fore.BLUE} BLU {Style.RESET_ALL}", random.randint(1, 5))
        track = Track(random.randint(14, 20))
        track.lane_one.insert(0, car_one.car_name)
        track.lane_two.insert(0, car_two.car_name)
        for _ in range(len(track.lane_one)):
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
            sleep(0.25)

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


if __name__ == '__main__':
    check_action = {1: car_race,
                    2: show_results,
                    3: quit_game,
                    }

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
            car_race()
        elif int(user_choice) == 2:
            show_results()
        elif int(user_choice) == 3:
            quit_game()
