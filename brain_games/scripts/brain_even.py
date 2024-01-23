#!/usr/bin/env python3
from brain_games.engine import run as run
from brain_games.games import even as brain_even


def main():
    run(brain_even)


if __name__ == "__main__":
    main()
