import time
import random
import argparse


VERSION = "ensuechaos CLI v1.0"


def infinite_loop() -> None:
    while True:
        print(random.choice(("A", "a", " ")), end="")


def timed_loop(seconds: int) -> None:
    initial_time = time.time()
    while time.time() - initial_time < seconds:
        print(random.choice(("A", "a", " ")), end="")


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
        "-t", "--time", 
        type=int, 
        default=3, 
        help="specify time of execution in seconds"
    )
    parser.add_argument(
        "-i", "--infinite", 
        action="store_true", 
        help="make execution infinite"
    )

    args = parser.parse_args()

    try:
        if args.infinite:
            infinite_loop()
        else:
            timed_loop(args.time)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
