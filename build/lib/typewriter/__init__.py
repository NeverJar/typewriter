import sys
import time

def write():
    if timee is None:
        timee = 0.1
    if not "\n" in text:
        text = text + "\n"
        
    for char in text:
        time.sleep(timee)
        sys.stdout.write(char)
        sys.stdout.flush()