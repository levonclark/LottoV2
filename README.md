# LottoV2
The 2026 new and improved Florida Lottery generator. Powerball, Mega Millions, Florida Lotto, Pick 5, Pick 4.

# 🎟️ Florida Lottery Picker Programmed by Levon Clark

A simple, colorful Python application that generates random numbers for popular Florida Lottery draw games.

The program provides an easy-to-use terminal menu for generating numbers for **Powerball, Mega Millions, Florida Lotto, Pick 5, and Pick 4**.

> ⚠️ **Disclaimer:** This program generates random lottery numbers for entertainment purposes only. Random number generation does not improve the mathematical odds of winning. Please play responsibly.

---

## 🎯 Features

* 🎱 Generate Powerball numbers
* 💰 Generate Mega Millions numbers
* 🍀 Generate Florida Lotto numbers
* 🔢 Generate Pick 5 numbers
* 🔢 Generate Pick 4 numbers
* 🎟️ Generate a Quick Pick for all supported games
* 💵 Display the cost of each ticket
* 💰 Calculate the total cost when generating all games
* 🎨 Colorful and formatted terminal interface
* ✅ Input validation for the main menu
* 🖥️ Can be run directly as a Python program
* 📦 Can be packaged as a standalone Windows `.exe`

---

## 🎮 Supported Games

| Game             | Main Numbers        | Special Number | Ticket Cost |
| ---------------- | ------------------- | -------------- | ----------: |
| 🎱 Powerball     | 5 numbers from 1–69 | Powerball 1–26 |       $2.00 |
| 💰 Mega Millions | 5 numbers from 1–70 | Mega Ball 1–24 |       $5.00 |
| 🍀 Florida Lotto | 6 numbers from 1–53 | None           |       $2.00 |
| 🔢 Pick 5        | 5 digits from 0–9   | None           |      $1.00* |
| 🔢 Pick 4        | 4 digits from 0–9   | None           |      $1.00* |

* The current version of the program uses the $1.00 wager for Pick 4 and Pick 5. These games may offer other wager options depending on the play selected.

### Generate All Games

The **Generate All Games** option generates one ticket for each supported game.

Current default total:

**$11.00**

---

## 🖥️ Example

When the program starts, you'll see a menu similar to:

```text
╔══════════════════════════════════════════════════════╗
║                                                      ║
║             🎟  FLORIDA LOTTERY PICKER  🎟           ║
║                                                      ║
║             Programmed by Levon Clark                ║
║                                                      ║
╚══════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════╗
║                    MAIN MENU                         ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║   [1]  🎱  Powerball              $2.00             ║
║   [2]  💰  Mega Millions          $5.00             ║
║   [3]  🍀  Florida Lotto          $2.00             ║
║   [4]  🔢  Pick 5                 $1.00             ║
║   [5]  🔢  Pick 4                 $1.00             ║
║   [6]  🎟️   Generate All Games    $11.00            ║
║   [7]  🚪  Exit                                      ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
```

Example Powerball output:

```text
╔════════════════════════════════════════════════════╗
║  🎱 POWERBALL                                      ║
╚════════════════════════════════════════════════════╝

  Your Numbers:

  07   18   29   44   63

  Powerball:

  🔴 12

  💵 Ticket Cost: $2.00
```

---

## 🐍 Requirements

To run the Python version, you need:

* Python 3.12 or newer
* Colorama

The project uses Python's built-in `random` module for number generation.

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/levonclark/LottoV2.git
```

Then enter the project directory:

```bash
cd LottoV2
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

Or install the required packages manually:

```bash
python -m pip install colorama
```

### 3. Run the program

```bash
python lottov2_menus.py
```

On some systems you may need:

```bash
python3 lottov2_menus.py
```

---

## 🪟 Windows Executable

The program can be packaged as a standalone Windows executable using **PyInstaller**.

Install PyInstaller:

```powershell
python -m pip install pyinstaller
```

Build the executable:

```powershell
python -m PyInstaller --onefile --name "FloridaLotteryPickerv2" lottov2_menus.py
```

The executable will be created in:

```text
dist/
└── FloridaLotteryPickerv2.exe
```

The executable can then be run on a Windows computer without requiring the user to manually install the Python dependencies.

---

## 📁 Project Structure

```text
LottoV2/
│
├── lottov2_menus.py       # Main Python program
├── README.md              # Project documentation
├── LICENSE                # MIT License
├── requirements.txt       # Python dependencies
├── .gitignore             # Files excluded from Git
│
├── build/                 # PyInstaller build files
└── dist/                  # Compiled executable
```

The `build/` and `dist/` directories are generated by PyInstaller and may be excluded from the Git repository depending on the project's release strategy.

---

## 🎲 How Number Generation Works

The program uses Python's built-in `random` module.

### Powerball

Five unique numbers are selected from:

```text
1–69
```

and one Powerball is selected from:

```text
1–26
```

Python's `random.sample()` is used for the five main numbers so that duplicate numbers cannot occur.

### Mega Millions

Five unique numbers are selected from:

```text
1–70
```

and one Mega Ball is selected from:

```text
1–24
```

### Florida Lotto

Six unique numbers are selected from:

```text
1–53
```

### Pick 5

Five individual digits are randomly generated from:

```text
0–9
```

Duplicate digits are allowed.

For example:

```text
58321
00742
55519
```

are all possible results.

### Pick 4

Four individual digits are randomly generated from:

```text
0–9
```

Duplicate digits are allowed.

For example:

```text
0748
1234
5555
```

are all possible results.

---

## ⚠️ Important Disclaimer

This application is a **random number generator** and is not a lottery prediction system.

Lottery drawings are designed to be random, and previous winning numbers do not make particular numbers more or less likely to be drawn in a future drawing.

The program does not claim to predict winning numbers or increase the probability of winning.

Lottery participation involves financial risk. Please play responsibly and only spend what you can afford to lose.

For official game rules, current prices, and drawing information, refer to the official Florida Lottery website.

---

## 🛠️ Future Features

Possible improvements planned for future versions include:

* [ ] Generate multiple tickets at once
* [ ] Save generated tickets
* [ ] Ticket history
* [ ] Ticket IDs
* [ ] Enter winning numbers and check tickets
* [ ] Automatically retrieve recent winning numbers
* [ ] Historical number statistics
* [ ] Number frequency analysis
* [ ] Hot and cold number analysis
* [ ] Odd/even number analysis
* [ ] Low/high number analysis
* [ ] Configurable Pick 4 and Pick 5 wager amounts
* [ ] Graphical user interface
* [ ] Automatic Windows builds through GitHub Actions
* [ ] GitHub Releases with downloadable `.exe` files

---

## 📜 License

This project is licensed under the **MIT License**.

See the [`LICENSE`](LICENSE) file for details.

---

## 👨‍💻 Author

**Levon Clark**

Built as a Python learning project and ongoing experiment in software development, GitHub, automation, and application packaging.

---

## ⭐ Contributing

Suggestions, bug reports, and improvements are welcome.

If you'd like to contribute:

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Test the program.
5. Submit a pull request.

---

### 🎟️ Good luck and have fun!

**Remember: The numbers are random — the fun is in the picking. 🍀**
