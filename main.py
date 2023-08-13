import argparse
import sys
from pyfiles.birthdaysmanager import birthdaysmanager

path = "birthdays.txt"

parser = argparse.ArgumentParser(
                    prog="birthdaymanager",
                    description="A simple programm to manage birthdays",
                    epilog="Made by Afeef")

parser.add_argument("-n", "--next",     help=f"Prints all birthdays within the next 30 days.\nNote that this is the default option",
                                        action="store_true")
parser.add_argument("-l", "--list",     help="Prints every birthday",
                                        action="store_true")
parser.add_argument("-a", "--add",      help="Adds a birthday to the list. Year is optional and will be set to 2039 by default",
                                        metavar="NAME/DAY/MONTH/{YEAR}",)
parser.add_argument("-r", "--remove",   help="Removes a birthday with INDEX from the list. Use -l or --list to get INDEX",
                                        metavar="INDEX")
args = parser.parse_args()

def main():
    bm = birthdaysmanager(path)

    if(len(sys.argv) == 1):
        print(bm.get_next())

    if(args.next != False):
        print(bm.get_next())

    if(args.list != False):
        print(bm)

    if(args.add != None):
        try:
            argv = args.add.split('/')
            if(len(argv) == 4):
                bm.add_bd(argv[0], int(argv[1]), int(argv[2]), int(argv[3]))
            elif(len(argv) == 3):
                bm.add_bd(argv[0], int(argv[1]), int(argv[2]))
            else:
                print("Too few arguments given! Example for correct input: \"Hatsune Miku/3/9/2039\" (including the \")\nUse the -h option for help")
        except:
            print("Wrong Input! Example for correct input: \"Hatsune Miku/3/9/2039\" (including the \")\nUse the -h option for help")

    if(args.remove != None):
        try:
            bm.rm_bd(int(args.remove))
        except:
            print("Wrong input. Use the -h option for help")

if __name__ == '__main__':
    main()
