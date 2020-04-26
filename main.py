#!/usr/bin/python
import sys
from run2048 import Game


if __name__ == '__main__':
    try:
        Game()
    except KeyboardInterrupt:
        pass
