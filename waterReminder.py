import time

startTime = time.time()

def main():
    #To give the reminder at the starting
    print("It's one hour since you had water. Time to drink water.")
    #To give reminder after every one hour
    while(True):
        if((time.time() - startTime) >= 3600):
            print("It's one hour since you had water. Time to drink water.")

if __name__ == "__main__":
    main()