import sys
import time

def animated_input(prompt="Example prompt for input:", delay=0.05):
    result = ""
    for character in prompt:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    while True:
        key = sys.stdin.read(1)
        if key == "\n" or key == "\r":
            break
        result += key
        #sys.stdout.write(key)
        #sys.stdout.flush()
    return result