"""
ENSUECHAOS

**FLASH WARNING**

Just a useless tool that makes your screen go crazy.
"""

import time
import random
import argparse
import threading
import pyautogui
from colorama import just_fix_windows_console, Fore


VERSION = "ensuechaos CLI v2.1"
BITS = ("0", "1")
MAX_X = pyautogui.size()[0] - 1
MAX_Y = pyautogui.size()[1] - 1
MOUSE_SPEED = 0.175


def spam(initial_time: int, time_limit: int) -> None:
    just_fix_windows_console()
    while time.time() - initial_time < time_limit:
        print(Fore.GREEN + random.choice(BITS), end="")


def mouse_action(initial_time: int, time_limit: int) -> None:
    while time.time() - initial_time < time_limit:
        x = random.randint(0, MAX_X)
        y = random.randint(0, MAX_Y)
        pyautogui.moveTo(x, y, MOUSE_SPEED)


def main():
    parser = argparse.ArgumentParser(
        prog="ensuechaos",
        description="Just a useless tool that makes your screen go crazy (FLASH WARNING)"
    )
    parser.add_argument(
        "-v", "--version", 
        action="version", 
        version=VERSION
    )
    parser.add_argument(
        "-d", "--duration", 
        type=int, 
        default=3, 
        help="specify duration in seconds"
    )

    args = parser.parse_args()
    spam_thread = threading.Thread(
        target=spam, 
        args=(time.time(), args.duration)
    )
    mouse_thread = threading.Thread(
        target=mouse_action, 
        args=(time.time(), args.duration)
    )

    try:
        spam_thread.start()
        mouse_thread.start()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
