#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    options = ['rock', 'paper', 'scissors']
    # options = [[i] for i in options]
    output = []
    if n == 0:
        return [[]]
    if n == 1:
        return [[i] for i in options]

    def play_game(num, solutions):
        if num == 0:
            output.append(solutions)
        else:
            for item in options:
                play_game(num - 1, solutions + [item])

    play_game(n, [])
    return output


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
