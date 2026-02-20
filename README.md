## Rock Paper Scissors (Console)

A simple, lightweight **player vs computer** Rock–Paper–Scissors game that runs in your terminal.  
The game keeps track of wins, losses, and ties for the current session until you exit.

### Requirements
- **Python 3.x** installed and available on your PATH

### How to Run
From the project folder:

```bash
python rock_paper_scissors.py
```

If your system uses `python3` instead:

```bash
python3 rock_paper_scissors.py
```

### How to Play
- When prompted with `What do you throw down?` type one of:
  - `rock`
  - `paper`
  - `scissors`
- The computer will randomly choose its move.
- The result of the round is printed, along with the **running score**:
  - Your wins
  - Computer wins
  - Ties
- To stop playing, type:

```text
quit
```

When you quit, the game prints the final session score and exits.

### Notes
- All scores are kept **in memory only**; they reset each time you restart the program.
