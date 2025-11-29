# Cricket Game (Python Console)

A simple console-based cricket mini-game built in Python. The player selects a shot between 1 and 6. The bowler then delivers a random number between 1 and 6.
If both numbers match, the batsman is OUT. Otherwise, the selected run is added to the score.
The game continues until the batsman gets out.

---

## Features

* Console-based interactive gameplay
* Randomized bowler deliveries using Python's `random` module
* Color-coded messages using ANSI color codes (`RED`, `GREEN`, `BLUE`, `YELLOW`)
* Error handling for invalid user input
* Simple class-based architecture (`CricketGame` class)

---

## Requirements

Install the required Python package:

```bash
pip install colour
```

Make sure your terminal supports ANSI colors.

---

## How to Run

1. Save the script as `cricket_game.py`
2. Run it using:

```bash
python cricket_game.py
```

---

## Game Rules

* Enter any number from **1 to 6** as your shot.
* If the **bowler's random number matches your shot**, you are **out**.
* Otherwise, your score increases by your chosen run.
* Game ends when you get out, and your final score is displayed.

---

## Code Structure

```
CricketGame
 ├── __init__()      # Initialize score and out flag
 ├── play_ball()     # Handles each ball, scoring, and OUT logic
 └── start()         # Main loop and game instructions
```

---

## Sample Output

```
Are you ready batsman
Hit between (1-6).
if bowler matches the shot >> you are out!

Enter your shot (1-6): 4
bowler delivered : 2
Nice shot! Total score : 4

Enter your shot (1-6): 3
bowler delivered : 3
OUT! bowled.....
Your final score : 4
Thanks for playing
```

---

## Future Enhancements

* Add overs and ball tracking
* Add levels (Easy / Medium / Hard)
* Add a bowler AI with weighted probabilities
* Add a replay option
* Add sound effects for terminals that support it
* add gui for online playable

---

## License

This project is open for modification and learning purposes.
