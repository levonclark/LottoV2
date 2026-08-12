###########################################
# Florida Lottery Picker Version 3.0
# Programmed by Levon Clark
# "One day everyone will be a winner."
#############################################

import random
from colorama import init, Fore, Style

# Initialize Colorama
init(autoreset=True)


# ============================================================
#TICKET PRICES CAN BE ADJUSTED AS THE ECONOMY GOES UP AND DOWN
# ============================================================

POWERBALL_COST = 2.00
MEGA_MILLIONS_COST = 5.00
FLORIDA_LOTTO_COST = 2.00
FLORIDA_FANTASY_5_COST = 1.00

# Pick 4 and Pick 5 can be played for $0.50 or $1.00.
# This program uses $1.00 as the default.
PICK_5_COST = 1.00
PICK_4_COST = 1.00


# ============================================================
#                       DISPLAY HELPERS
# ============================================================

def clear_screen():
    """Print enough blank lines to visually clear the terminal."""
    print("\n" * 3)


def print_header():
    """Display the main program header."""
    print(Fore.CYAN + Style.BRIGHT)
    print("╔══════════════════════════════════════════════════════╗")
    print("║                                                      ║")
    print("║             🎟  FLORIDA LOTTERY PICKER  🎟           ║")
    print("║                Programmed by Levon Clark             ║")
    print("║              One Day We Will All Be Winners!         ║")
    print("║                                                      ║")
    print("╚══════════════════════════════════════════════════════╝")
    print(Style.RESET_ALL)


def print_menu():
    """Display the main menu."""
    print(Fore.YELLOW + Style.BRIGHT)
    print("╔══════════════════════════════════════════════════════╗")
    print("║                    MAIN MENU                         ║")
    print("╠══════════════════════════════════════════════════════╣")
    print("║                                                      ║")
    print("║   [1]  🎱  Powerball              $2.00             ║")
    print("║   [2]  💰  Mega Millions          $5.00             ║")
    print("║   [3]  🍀  Florida Lotto          $2.00             ║")
    print("║   [4]  ✨  Florida Fantasy 5      $1.00             ║")
    print("║   [5]  🔢  Pick 5                 $1.00             ║")
    print("║   [6]  🔢  Pick 4                 $1.00             ║")
    print("║   [7]  🎟️  Generate All Games    $12.00             ║")
    print("║   [8]  🚪  Exit                                      ║")
    print("║                                                      ║")
    print("╚══════════════════════════════════════════════════════╝")
    print(Style.RESET_ALL)


def print_section_title(title):
    """Display a formatted section title."""
    print()
    print(Fore.CYAN + Style.BRIGHT + "╔" + "═" * 52 + "╗")
    print(f"║  {title:<50}║")
    print("╚" + "═" * 52 + "╝")
    print(Style.RESET_ALL)


def print_cost(cost):
    """Display the ticket cost."""
    print()
    print(
        Fore.GREEN +
        Style.BRIGHT +
        f"  💵 Ticket Cost: ${cost:.2f}"
    )


def pause():
    """Pause before returning to the menu."""
    input(
        Fore.WHITE +
        "\nPress ENTER to return to the main menu..."
    )


# ============================================================
#                       LOTTERY GAMES
# ============================================================

def generate_powerball():
    """
    Generate a Powerball ticket.

    5 unique numbers from 1-69
    1 Powerball from 1-26
    """

    numbers = sorted(random.sample(range(1, 70), 5))
    powerball = random.randint(1, 26)

    print_section_title("🎱 POWERBALL")

    print(Fore.WHITE + "  Your Numbers:")
    print()

    print(
        "  " +
        "   ".join(
            Fore.WHITE +
            Style.BRIGHT +
            f"{number:02d}"
            for number in numbers
        )
    )

    print()
    print(Fore.RED + Style.BRIGHT + "  Powerball:")
    print()

    print(
        "  " +
        Fore.RED +
        Style.BRIGHT +
        f"🔴 {powerball:02d}"
    )

    print_cost(POWERBALL_COST)


def generate_mega_millions():
    """
    Generate a Mega Millions ticket.

    5 unique numbers from 1-70
    1 Mega Ball from 1-24
    """

    numbers = sorted(random.sample(range(1, 71), 5))
    mega_ball = random.randint(1, 24)

    print_section_title("💰 MEGA MILLIONS")

    print(Fore.WHITE + "  Your Numbers:")
    print()

    print(
        "  " +
        "   ".join(
            Fore.WHITE +
            Style.BRIGHT +
            f"{number:02d}"
            for number in numbers
        )
    )

    print()
    print(Fore.YELLOW + Style.BRIGHT + "  Mega Ball:")
    print()

    print(
        "  " +
        Fore.YELLOW +
        Style.BRIGHT +
        f"🟡 {mega_ball:02d}"
    )

    print_cost(MEGA_MILLIONS_COST)


def generate_florida_lotto():
    """
    Generate a Florida Lotto ticket.

    6 unique numbers from 1-53
    """

    numbers = sorted(random.sample(range(1, 54), 6))

    print_section_title("🍀 FLORIDA LOTTO")

    print(Fore.WHITE + "  Your Numbers:")
    print()

    print(
        "  " +
        "   ".join(
            Fore.GREEN +
            Style.BRIGHT +
            f"{number:02d}"
            for number in numbers
        )
    )

    print_cost(FLORIDA_LOTTO_COST)


def generate_fantasy_5():
    """
    Generate a Florida Fantasy 5 ticket.

    5 unique numbers from 1-36
    """

    numbers = sorted(random.sample(range(1, 37), 5))

    print_section_title("✨ FLORIDA FANTASY 5")

    print(Fore.WHITE + "  Your Numbers:")
    print()

    print(
        "  " +
        "   ".join(
            Fore.CYAN +
            Style.BRIGHT +
            f"{number:02d}"
            for number in numbers
        )
    )

    print_cost(FLORIDA_FANTASY_5_COST)


def generate_pick_5():
    """
    Generate a Pick 5 number.

    5 digits from 0-9.
    Duplicate digits are allowed.
    """

    number = "".join(
        str(random.randint(0, 9))
        for _ in range(5)
    )

    print_section_title("🔢 PICK 5")

    print(Fore.WHITE + "  Your Number:")
    print()

    print(
        "  " +
        Fore.MAGENTA +
        Style.BRIGHT +
        f"★ {number} ★"
    )

    print_cost(PICK_5_COST)


def generate_pick_4():
    """
    Generate a Pick 4 number.

    4 digits from 0-9.
    Duplicate digits are allowed.
    """

    number = "".join(
        str(random.randint(0, 9))
        for _ in range(4)
    )

    print_section_title("🔢 PICK 4")

    print(Fore.WHITE + "  Your Number:")
    print()

    print(
        "  " +
        Fore.BLUE +
        Style.BRIGHT +
        f"★ {number} ★"
    )

    print_cost(PICK_4_COST)


# ============================================================
#                    GENERATE ALL GAMES
# ============================================================

def generate_all():
    """Generate a ticket for every lottery game."""

    total_cost = (
        POWERBALL_COST +
        MEGA_MILLIONS_COST +
        FLORIDA_LOTTO_COST +
        FLORIDA_FANTASY_5_COST +
        PICK_5_COST +
        PICK_4_COST
    )

    print_section_title("🎟️  QUICK PICK — ALL GAMES")

    print(Fore.CYAN + "  Generating your numbers...")
    print()

    # --------------------------------------------------------
    # POWERBALL
    # --------------------------------------------------------

    numbers = sorted(random.sample(range(1, 70), 5))
    powerball = random.randint(1, 26)

    print(Fore.WHITE + Style.BRIGHT + "  🎱 POWERBALL")
    print(
        "     " +
        "  ".join(f"{number:02d}" for number in numbers) +
        Fore.RED +
        f"   |   PB {powerball:02d}"
    )

    print(
        Fore.GREEN +
        f"     Cost: ${POWERBALL_COST:.2f}"
    )

    print()

    # --------------------------------------------------------
    # MEGA MILLIONS
    # --------------------------------------------------------

    numbers = sorted(random.sample(range(1, 71), 5))
    mega_ball = random.randint(1, 24)

    print(Fore.WHITE + Style.BRIGHT + "  💰 MEGA MILLIONS")
    print(
        "     " +
        "  ".join(f"{number:02d}" for number in numbers) +
        Fore.YELLOW +
        f"   |   MB {mega_ball:02d}"
    )

    print(
        Fore.GREEN +
        f"     Cost: ${MEGA_MILLIONS_COST:.2f}"
    )

    print()

    # --------------------------------------------------------
    # FLORIDA LOTTO
    # --------------------------------------------------------

    numbers = sorted(random.sample(range(1, 54), 6))

    print(Fore.WHITE + Style.BRIGHT + "  🍀 FLORIDA LOTTO")
    print(
        "     " +
        "  ".join(f"{number:02d}" for number in numbers)
    )

    print(
        Fore.GREEN +
        f"     Cost: ${FLORIDA_LOTTO_COST:.2f}"
    )

    print()

    # --------------------------------------------------------
    # FLORIDA FANTASY 5
    # --------------------------------------------------------

    numbers = sorted(random.sample(range(1, 37), 5))

    print(Fore.WHITE + Style.BRIGHT + "  ✨ FLORIDA FANTASY 5")
    print(
        "     " +
        "  ".join(f"{number:02d}" for number in numbers)
    )

    print(
        Fore.GREEN +
        f"     Cost: ${FLORIDA_FANTASY_5_COST:.2f}"
    )

    print()

    # --------------------------------------------------------
    # PICK 5
    # --------------------------------------------------------

    pick5 = "".join(
        str(random.randint(0, 9))
        for _ in range(5)
    )

    print(Fore.WHITE + Style.BRIGHT + "  🔢 PICK 5")
    print(
        f"     {Fore.MAGENTA}{pick5}"
    )

    print(
        Fore.GREEN +
        f"     Cost: ${PICK_5_COST:.2f}"
    )

    print()

    # --------------------------------------------------------
    # PICK 4
    # --------------------------------------------------------

    pick4 = "".join(
        str(random.randint(0, 9))
        for _ in range(4)
    )

    print(Fore.WHITE + Style.BRIGHT + "  🔢 PICK 4")
    print(
        f"     {Fore.BLUE}{pick4}"
    )

    print(
        Fore.GREEN +
        f"     Cost: ${PICK_4_COST:.2f}"
    )

    # --------------------------------------------------------
    # TOTAL
    # --------------------------------------------------------

    print()
    print(Fore.CYAN + Style.BRIGHT)
    print("  ══════════════════════════════════════════════════")

    print(
        Fore.GREEN +
        Style.BRIGHT +
        f"  💵 TOTAL FOR ALL 6 GAMES: ${total_cost:.2f}"
    )

    print(Fore.CYAN + Style.BRIGHT)
    print("  ══════════════════════════════════════════════════")


# ============================================================
#                         MAIN PROGRAM
# ============================================================

def main():

    while True:

        clear_screen()

        print_header()
        print_menu()

        choice = input(
            Fore.GREEN +
            Style.BRIGHT +
            "  Enter your selection: "
        ).strip()

        if choice == "1":

            clear_screen()
            print_header()
            generate_powerball()
            pause()

        elif choice == "2":

            clear_screen()
            print_header()
            generate_mega_millions()
            pause()

        elif choice == "3":

            clear_screen()
            print_header()
            generate_florida_lotto()
            pause()

        elif choice == "4":

            clear_screen()
            print_header()
            generate_fantasy_5()
            pause()

        elif choice == "5":

            clear_screen()
            print_header()
            generate_pick_5()
            pause()

        elif choice == "6":

            clear_screen()
            print_header()
            generate_pick_4()
            pause()

        elif choice == "7":

            clear_screen()
            print_header()
            generate_all()
            pause()

        elif choice == "8":

            clear_screen()

            print(Fore.CYAN + Style.BRIGHT)
            print("╔══════════════════════════════════════════════════════╗")
            print("║                                                      ║")
            print("║     Thank you for using the Florida Lottery Picker   ║")
            print("║                      Version 3.0                     ║")
            print("║              Programmed by Levon Clark!              ║")
            print("║                                                      ║")
            print("║                      Good luck! 🍀                  ║")
            print("║                                                      ║")
            print("╚══════════════════════════════════════════════════════╝")
            print(Style.RESET_ALL)

            break

        else:

            print(
                Fore.RED +
                Style.BRIGHT +
                "\n  ❌ Invalid selection."
            )

            print(
                Fore.WHITE +
                "  Please enter a number between 1 and 8."
            )

            pause()


# ============================================================
#                     PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()