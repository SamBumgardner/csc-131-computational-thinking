""""
jumpTable.py
A toy program on jump tables.
Program displays a menu to a user and prompts user to make a selection.
Menu options are keys in the jump table --- a dicionary--- with corresponding values
as aliases/references to the functions associated with the menu options/commands
"""

def insert():
    print("a new customer record has been inserted")

def delete():
    print("a customer record has been deleted")

def modify():
    print("a customer record has been modified")

jumpTable = {}

#load jumpTable with the command names and corresponding functions

jumpTable['i'] = insert
jumpTable['d'] = delete
jumpTable['m'] = modify

MENU  = """
         MENU
i insert new customer record
d delete a customer record
m modify a customer record
q Quit the program
_____________________________
"""

def main():
    while True:
        print(MENU)
        command = input("Select menu option: ")
        if command not in ['i', 'd', 'm', 'q']:
            print("Invalid menu option, try again")
            continue
        elif command == 'q':
            print("Good Bye!")
            break
        else:
            jumpTable[command]() #call corresponding function
        

main()
