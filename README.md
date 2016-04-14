# Dicegame in Python

This is a short dice game as requested for a trainee evaluation.  
The game is rather simple dice simulation,
where user tries to quess the sum of two dice.

Program is written in Python 3.5.1.  
Visuals were made with pygame 1.9.2.  

The game is built around a simple state machine.

### Installation
Clone this repository, by running:
```
git clone https://github.com/MiriPii/dicegame.git
```
Install pygame, if you don't have it yet:

Guidance for installing pygame can be found at:  
http://www.pygame.org/download.shtml

### Running the game
Go to the `$REPOPATH/dicegame/`  
And run the `main.py` from this folder :  
i.e. In linux 
```
~/$REPOPATH/dicegame/ > $ python3.5 main.py
```

### Description

The given outline for the game:

1. User quesses the sum of two dies.
2. Program simulates the roll of the 2 dies.
3. Program shows the sum and tells the player if he guessed right.
4. User chooses to either start a new round or exit the program.
