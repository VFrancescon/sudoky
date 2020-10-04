# sudoky
## Functionality and Usage
Sudoky is a python based Sudoku application. In its current iteration, the program is able to print a sudoky grid (with values edited within the grid.py file), allows the user to insert values into the grid (left click -> number input) or comment values (right click -> number input).

The program is also able to solve sudokus of medium to advanced difficulty autonomously (input 's' to generate the candidates for each cell -> input r to apply 1 pass of the solving algorithm, repeat as required).

As the aim is to produce a solving companion for a user attempting to learn how to solve sudokus individually, the project does not use backtracking algorithms to find the correct solution for a given grid. Instead, techniques usable by a human being are applied at all points to ensure followable solutions.

![Image of Gameplay](images/gameplay.png)

## Future Features
Future implementations of the program will allow users to input their own puzzle from the grid itself. Furthermore, the solving algorithms will be expanded to cover all humanly solvable sudokus. 

A final version of the program will also be able to copy a grid from a screenshot or picture.

# Setup Instructions
Run the following in the installation folder

1. [Install pip](https://pip.pypa.io/en/stable/installing/)
2. git clone https://github.com/VFrancescon/sudoky
3. pip install -r requirements.txt
4. install helvetica.ttf
5. python3 game.py


### Special thanks
Thanks Rahul!

Created by Vittorio Francescon
