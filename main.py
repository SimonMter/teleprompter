import os
import sys
import termios
import tty
import re

filename = None
words = []

def clear():
    os.system("clear")

def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def load_file():
    global filename, words
    filename = input("Enter filename: ")
    

    with open(filename, "r") as f:
        content = f.read()
        words = [p.strip() for p in re.split(r'\n\s*\n', content) if p.strip()]


def main():
    global words
    load_file()
    current_index = 0
    max_index = len(words) - 1

    while True:
        clear()
        print(words[current_index])

        key = get_key()
        if key == " " and current_index < max_index:
            current_index += 1
        elif key == "\r" or key == "\n":  # Enter key
            if current_index > 0:
                current_index -= 1
        elif key.lower() == "q":
            clear()
            break
        elif key == " " and current_index >= max_index:
            clear()
            break

if __name__ == "__main__":
    main()

