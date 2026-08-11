# Lotto Version 2
# Programmed by Levon Clark
# This is the 2026 version. New and improved.
import random
# -----------------------------------------
# POWERBALL
# 5 numbers: 1-69
# Powerball: 1-26
# -----------------------------------------
def generate_powerball():
    numbers = sorted(random.sample(range(1, 70), 5))
    powerball = random.randint(1, 26)
    print("\nPOWERBALL")
    print("-" * 30)
    print("Numbers:   ", " ".join(f"{n:02d}" for n in numbers))
    print("Powerball: ", f"{powerball:02d}")
# -----------------------------------------
# MEGA MILLIONS
# 5 numbers: 1-70
# Mega Ball: 1-24
# -----------------------------------------
def generate_mega_millions():
    numbers = sorted(random.sample(range(1, 71), 5))
    mega_ball = random.randint(1, 24)
    print("\nMEGA MILLIONS")
    print("-" * 30)
    print("Numbers:   ", " ".join(f"{n:02d}" for n in numbers))
    print("Mega Ball: ", f"{mega_ball:02d}")
# -----------------------------------------
# FLORIDA LOTTO
# 6 numbers: 1-53
# -----------------------------------------
def generate_florida_lotto():
    numbers = sorted(random.sample(range(1, 54), 6))
    print("\nFLORIDA LOTTO")
    print("-" * 30)
    print("Numbers: ", " ".join(f"{n:02d}" for n in numbers))
# -----------------------------------------
# PICK 5
# 5 digits: 0-9
# Duplicates ARE allowed
# -----------------------------------------
def generate_pick_5():
    number = "".join(str(random.randint(0, 9)) for _ in range(5))
    print("\nPICK 5")
    print("-" * 30)
    print("Number: ", number)
# -----------------------------------------
# PICK 4
# 4 digits: 0-9
# Duplicates ARE allowed
# -----------------------------------------
def generate_pick_4():
    number = "".join(str(random.randint(0, 9)) for _ in range(4))
    print("\nPICK 4")
    print("-" * 30)
    print("Number: ", number)
# -----------------------------------------
# GENERATE ALL GAMES
# -----------------------------------------
def generate_all():
    print("\n" + "=" * 40)
    print("       RANDOM LOTTERY PICKS")
    print("=" * 40)
    generate_powerball()
    generate_mega_millions()
    generate_florida_lotto()
    generate_pick_5()
    generate_pick_4()
    print("\n" + "=" * 40)
# -----------------------------------------
# MAIN MENU
# -----------------------------------------
def main():
    while True:
        print("\n")
        print("=" * 40)
        print("       FLORIDA LOTTERY NUMBER PICKER")
        print("=" * 40)
        print("1. Powerball")
        print("2. Mega Millions")
        print("3. Florida Lotto")
        print("4. Pick 5")
        print("5. Pick 4")
        print("6. Generate All Games")
        print("7. Exit")
        print("=" * 40)
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            generate_powerball()
        elif choice == "2":
            generate_mega_millions()
        elif choice == "3":
            generate_florida_lotto()
        elif choice == "4":
            generate_pick_5()
        elif choice == "5":
            generate_pick_4()
        elif choice == "6":
            generate_all()
        elif choice == "7":
            print("\nThanks for using the Florida Lottery Number Picker!")
            break
        else:
            print("\nInvalid selection. Please enter a number from 1-7.")
# Start the program
if __name__ == "__main__":
    main()