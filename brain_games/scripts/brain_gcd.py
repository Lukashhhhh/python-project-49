#!/usr/bin/env python3
from brain_games.engine import run_game as run
from brain_games.games import brain_gcd as brain_gcd


def main():
    run(brain_gcd)


if __name__ == "__main__":
    main()
