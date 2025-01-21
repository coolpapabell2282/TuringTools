# TuringTools
Some tools for exploring puzzles for the board game Turing Machine

As of now, this code is built to do one thing - finding puzzles for the board game Turing Machine that can be solved solely through metalogic, without asking any actual questions. Specifically, it looks for 5-question puzzles where only 1 set of answers to the questions has a unique solution, but the 4-question puzzles obtained by deleting one question are not uniquely determined, so that the 5 questions are not redundant. The parameter NUMOFTRIALS in the header can be altered to change the number of random combinations that will be checked when the code runs.
