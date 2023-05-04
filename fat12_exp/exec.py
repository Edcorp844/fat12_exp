import os 
import time
import sys
from platform import system as S

def slow(msg):
    for c in msg + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2./ 50)

def execute():
    if S() == "Linux":
        slow("Runng run.sh")
        os.system("bash run.sh")
    else:
        slow("If you're on windows, simply run make and then make run, ensure make is installed on your system first\n")
    

if __name__ == "__main__":
    execute()