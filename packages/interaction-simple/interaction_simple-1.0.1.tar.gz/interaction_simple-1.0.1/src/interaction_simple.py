import sys
def start():
    sys.stdout.write("Hi there!")
    sys.stdout.write("\nCan you please tell me your name?\n")

    name = input()
    while (not name):
        sys.stdout.write("Plese say your name.\n")
        name = input()
    sys.stdout.write(f"\nHey {name}! It's really nice to meet you!")

    sys.stdout.write(f"\nHow is your day {name}?\n")
    
    ans = input()
    while (not ans):
        ans = input()
    sys.stdout.write(f"\nI have a great time interacting with you {name}.\nI hope to catch up with you very soon.")
    sys.stdout.write("\U0001F44B \U0001F44B \n")