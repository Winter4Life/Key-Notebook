import os.path
import frame1
from frame4 import open_frame4

def main():
    if __name__ == "__main__":
        if os.path.exists("current_user.txt"):
            open_frame4()
        else:
            frame1.open_frame1() 

main()   