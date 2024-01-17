#!/usr/bin/env python3
from brain_games.engine import run_game as run
from brain_games.games import brain_even as brain_even


def main():
    run(brain_even)


if __name__ == "__main__":
    main()
