# Hangman Game - Python CLI Version

This is a simple terminal-based Hangman game built using Python.  
The player must guess a secret word, letter by letter, within a limited number of attempts.  
The game includes category-based word selection, and automatic restart after each round.

## Features

- Random word selection from multiple categories (animals, fruits, objects, jobs, etc.)
- Colorful terminal output with ASCII-art hangman stages
- Restartable game session with user confirmation
- Clean and modular OOP design (Object-Oriented Programming)
- Easy to extend or modify for new categories and game logic

## Prerequisites

Make sure Python 3 is installed on your system.

## File Structure
```text
hangman_game/
│
├── hangman.py      # Main game logic
├── dist/
│   └── hangman.exe # Compiled executable (optional)
└── README.md
```

## How to Run
```bash
python hangman.py
```

## Run the Game (EXE Version)
If you don't have Python installed, you can run the .exe file directly:
Download the .exe file from the Releases page.
Double-click the .exe file to start the game.
Play directly from your terminal

This file was generated using pyinstaller:

```bash
pyinstaller --onefile hangman.py
```

## Sample Gameplay
🎮 Welcome to Hangman!\
Category: Fruits\
Guess the word. You have 6 attempts to save the hangman.

Word: _ _ _ _ _\
Guessed letters: a, e, i

Guess a letter: o\
Correct guess!

## Word Categories Included
- Digital: python, programming, algorithm, ...
- Occupations: teacher, doctor, engineer, ...
- Animals: lion, tiger, dolphin, ...
- Fruits: mango, banana, kiwi, ...
- Objects: table, pencil, lamp, ...

## Future Ideas
- Difficulty levels
- High score system
- Choose your category
- Web-based version

Author\
[Ridwan Darmawan]\
This project is part of my learning journey in Python development.

Thank you for checking out this project!\
Pull requests, stars, and feedback are always welcome!

