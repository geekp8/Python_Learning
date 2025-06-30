#thread=one task into multiple process ->lightweight process
#why?
#what is multitasking?->multiple task at the same time,as your cpu it will do time sharing
#soo many things happening at one time

import os

def main():
    print("PID of process is : ",os.getpid())#get process id

if __name__ == "__main__":
    main()