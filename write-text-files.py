# Name: Pineda, Patricia Anne E.
# Section: BSCPE 1-5
# Assignment 4: Programming Exercise 3 (Multiple Line of Text Contents into a Text File)

# while loop
try_again = ""
while try_again != "n":
    # open text file
    my_file = open("mylife.txt", "w")
    # write line 1
    my_file.write("Enter line: Beautiful is better than ugly.")
    # write line 2
    line_2 = "\nEnter line: Explicit is better than Implicit."
    my_file.write(line_2)
    # write line 3
    line_3 = "\nEnter line: Simple is better than complex."
    my_file.write(line_3)
    # ask user for input
    try_again = input("\n\033[35mAre there any more lines y/n? ")
    # if yes
    if try_again == "y":
        import pyfiglet
        starting = pyfiglet.figlet_format("Starting...")
        print("\n" + starting)
        import time
        time.sleep(2)
    # if no
    elif try_again == "n":
        import time
        time.sleep(2)
        bye = pyfiglet.figlet_format("Okay, bye!")
        print("\n" + bye)
    # if invalid input
    else:
        print("invalid output.")