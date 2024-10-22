## Description
I implemented a minimax algorithm to determine the next move made. The code for the minimax algorithm is contained mostly within `MinimaxPlayer.py` in classes/agents. The evaluation function is located in `Board.py` (source for number used in evalutation function and values assigned to pieces: https://www.chessprogramming.org/Simplified_Evaluation_Function)

## Instructions
There are no additional dependencies that need to be installed. To run the code for just a single game, you need to use the command `python main.py HumanPlayer MinimaxPlayer False` or `python main.py RandomPlayer MinimaxPlayer False`. To run the code with 100 trials, you need to run `python main.py RandomPlayer MinimaxPlayer True`.(warning: it takes a while to fully run all itterations)