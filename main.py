#Oliver (Ollie) Kim
#October 10, 2024

#CS172 HW02 The passage of time
#aids user in date recording and comparision.
#assumes all February's have 28 days, thus disregarding leap year

from date import Date

#global variables
listDates = [] #keeps track of user's inputted dates

#functions
#command: asks for user input to use program functions
def command():
    commandList = ['ADD', 'LIST', 'EDIT', 'COMPARE', 'MENU', 'A', 'L', 'E', 'C', 'M']
    command = input("\nPlease input function: ")
    loop = True
    while loop:
        if command.upper() not in commandList:
            print("Invalid command.")
            command = input("Please input function: ")
        else:
            loop = False
            if command.upper() == 'ADD' or command.upper() == 'A':
                add()
            elif command.upper() == 'LIST' or command.upper() == 'L':
                listPrint()
            elif command.upper() == 'EDIT' or command.upper() == 'E':
                edit()
            elif command.upper() == 'COMPARE' or command.upper() == 'C':
                compare()
            elif command.upper() == 'MENU' or command.upper() == 'M':
                menu()

#menu: prints function menu
def menu():
    print("\n~~~Function Menu~~~\nADD: Add another date.\nLIST: View all added dates\nEDIT: Add days to a date\nCOMPARE: Compare two inputted dates\nMENU: View functions menu")
    command()

#add: adds new Date object to listDates
def add():
    newDate = input("\nPlease enter your date (MM/DD/YYYY): ").split("/")
    loop = True
    while loop:
        try:
            newDate[0] = int(newDate[0])
            newDate[1] = int(newDate[1])
            newDate[2] = int(newDate[2])
            if len(newDate) == 3:
                newDateObject = Date(newDate[0], newDate[1], newDate[2])
                if checkDate(newDateObject) == False:
                    raise(ValueError)
                elif checkDate(newDateObject) == True:
                    loop = False
                    listDates.append(newDateObject)
                    command()
        except ValueError:
            print("Invalid date.")
            newDate = input("\nPlease enter your date (MM/DD/YYYY): ").split("/")
        except IndexError:
            print("Invalid date.")
            newDate = input("\nPlease enter your date (MM/DD/YYYY): ").split("/")

#listPrint: prints listDates
def listPrint():
    for index in range(len(listDates)): # print
        print(f'{index + 1}: {listDates[index]}')
    command()

#edit: allows the user to edit a previously inputted Date object
def edit():
    for index in range(len(listDates)): # print
        print(f'{index + 1}: {listDates[index]}')
    user = int(input("Which date would you like to edit? "))

    loop = True
    while loop:
        try: 
            if 0 <= (user - 1) <= len(listDates):
                moreDays = int(input("How many days will you add? "))
                listDates[user - 1].changeDate(moreDays)
                print(f'This is the new day: {listDates[user - 1]}')
                loop = False
            else:
                print("Invalid Date.")
                user = int(input("Which date would you like to edit? "))
        except IndexError:
            print("Index out of Bounds.")
            user = int(input("Which date would you like to edit? "))
        except ValueError:
            print("Invalid input.")
            moreDays = int(input("How many days will you add? "))
    command()

#compare: compare two dates and say which is older
def compare():
    for index in range(len(listDates)): # print
        print(f'{index + 1}: {listDates[index]}')
    user = input("Which two dates would you like to compare? (#,#) ").split(",")

    loop = True
    while loop:
        try: 
            if 0 <= (int(user[0]) - 1) <= len(listDates) and 0 <= (int(user[1]) - 1) <= len(listDates):
                date1 = listDates[int(user[0]) - 1]
                date2 = listDates[int(user[1]) - 1]

                loop = False
                if date1 < date2:
                    print(f'{date1} is before {date2}')
                    loop = False
                elif date1 > date2:
                    print(f'{date1} is after {date2}')
                    loop = False
                else:
                    print(f'{date1} and {date2} are the same day!')
                    loop = False
            else:
                raise(IndexError)
        except IndexError:
            print("One or Both Indexes are out of Bounds.")
            user = input("Which two dates would you like to compare? (#,#) ").split("/")
        except ValueError:
            print("Invalid input.")
            user = input("Which two dates would you like to compare? (#,#) ").split("/")
    command()

#function checkDate: boolean. checks if entered Date Object is valid
def checkDate(Date):
    oddMonths = {1, 3, 5, 8, 10, 12} #31 days
    evenMonths = {2, 4, 6, 9, 11} #30 days and february

    if Date.getMonth() > 12: #month check
        return False
    
    if (Date.getMonth() in oddMonths) and (Date.getDay() > 31): #31 day check
        return False
    elif Date.getMonth() in evenMonths:
        if (Date.getMonth() == 2) and (Date.getDay() > 28): #february check
            return False
        elif (Date.getDay() > 30): #30 day check
            return False
    return True


#main
if __name__ == "__main__":

    print("\nWelcome to the Passage of Time,\nwhere you can enter dates and do whichever.")
    menu()