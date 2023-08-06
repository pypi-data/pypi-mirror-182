import time
import random
import argparse
import threading
import pyautogui


VERSION = "ensuechaos CLI v2.0"
CHARACTERS = ("A", "a", " ")
MAX_X = pyautogui.size()[0] - 1
MAX_Y = pyautogui.size()[1] - 1
MOUSE_RITHM = 0.125


def spam(initial_time: int, time_limit: int) -> None:
    while time.time() - initial_time < time_limit:
        print(random.choice(CHARACTERS), end="")


def mouse_action(initial_time: int, time_limit: int) -> None:
    while time.time() - initial_time < time_limit:
        x = random.randint(0, MAX_X)
        y = random.randint(0, MAX_Y)
        pyautogui.moveTo(x, y, MOUSE_RITHM)


def main():
    parser = argparse.ArgumentParser(
        prog="ensuechaos",
        description="Just a useless tool that makes your screen go crazy."
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
    spam_thread = threading.Thread(target=spam, args=(time.time(), args.duration))
    mouse_thread = threading.Thread(target=mouse_action, args=(time.time(), args.duration))

    try:
        spam_thread.start()
        mouse_thread.start()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
