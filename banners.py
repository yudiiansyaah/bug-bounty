from pyfiglet import Figlet
import random

def colorize_text(text):
    colors = [
        "\033[31m",  # Red
        "\033[32m",  # Green
        "\033[33m",  # Yellow
        "\033[34m",  # Blue
        "\033[35m",  # Magenta
        "\033[36m",  # Cyan
    ]
    reset = "\033[0m"  # Reset color

    colored_text = ""
    for char in text:
        colored_text += random.choice(colors) + char
    colored_text += reset 
    return colored_text

def bug_bounty_banner():
    f = Figlet(font='standard')
    banner = f.renderText("BUG BOUNT")
    return colorize_text(banner)


def created_by_banner():
    f = Figlet(font='small')
    banner = f.renderText("Created by Yud'S")
    return colorize_text(banner)

if __name__ == '__main__':
    print(bug_bounty_banner())
    print(created_by_banner())