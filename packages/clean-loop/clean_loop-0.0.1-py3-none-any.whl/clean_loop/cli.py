#!/bin/python3

import argparse
import colorama
from colorama import Fore
import subprocess
from subprocess import PIPE
import sys
import time


def countdown(loopCount: int):
    seconds: int = 0
    while loopCount > seconds:
        print(f"\r:: [ {Fore.YELLOW}{loopCount}{Fore.RESET} ] ", end="")
        loopCount -= 1
        time.sleep(1)


def main():
    argumentParser = argparse.ArgumentParser()
    argumentParser.add_argument("--delay", "-d", type=str)
    argumentParser.add_argument("--script", "-s", type=str)
    arguments = argumentParser.parse_args()

    if arguments.delay is None:
        argumentParser.print_help()
        sys.exit(1)
    elif arguments.script is None:
        argumentParser.print_help()
        sys.exit(1)

    scriptFile = open(str(arguments.script), "r")
    script = scriptFile.read()

    print(":: Starting loop in...")

    countdown(3)
    print("\r:: Started loop.")

    while True:
        countdown(int(arguments.delay))
        print(f"\r:: [   ]", end="")

        subprocessTask = subprocess.run(script, shell=True, stdout=PIPE, stderr=PIPE)

        if subprocessTask.returncode == 1:
            print(f"\r:: {Fore.RED}[ ✘ ]{Fore.RESET}")
        elif subprocessTask.returncode == 0:
            print(f"\r:: {Fore.GREEN}[ ✓ ]{Fore.RESET}")
        else:
            print(f"\r:: {Fore.YELLOW}[ ✘ ]{Fore.RESET}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
