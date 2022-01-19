import os

selection = 0

while selection == 0:

    # MENU
    print("\nWelcome to Bus Line Manager")
    print("Type the respective number to navigate\n")
    print("1. See the line list")
    print("2. See the line schedules")
    print("3. Add a new line")
    print("4. Add a new schedule")
    print("5. Delete a line")
    print("6. Delete a schedule")
    print("7. Exit Program\n")

    selection = input()

    # SEE LINE LIST
    if selection == "1":
        data = open("data.txt")
        line_list = data.readlines()
        print("")
        for i in line_list:
            print(i, end='')
        print("\nType anything to go back\n")
        input()
        data.close()
        selection = 0

    # SEE LINE SCHEDULES
    elif selection == "2":
        print("2")

    # ADD A NEW LINE
    elif selection == "3":
        selection = 1
        while selection == 1:
            # CREATE THE NAME AND ID OF THE LINE AND STORES IN DATA FILE
            data = open("data.txt", "a")
            print("\nWrite the line number: ", end='')
            line_number = input()
            print("Write the line name: ", end='')
            line_name = input()
            data.write(line_number + " " + line_name + "\n")
            print("\nType 1 to add another line and 0 to go back\n")
            selection = input()
            if int(selection) == 1:
                selection = 1
            elif int(selection) == 0:
                data.close()
                selection = 0
            # IF THE NUMBER TYPED IS INVALID, RETURN TO MENU ANYWAY
            else:
                print("\nInvalid number typed, returning to menu...\n")
                data.close()
                selection = 0

    # ADD A NEW SCHEDULE
    elif selection == "4":
        print("4")

    # DELETE A LINE
    elif selection == "5":
        selection = 1
        while selection == 1:
            # SHOW THE LIST OF LINES
            data = open("data.txt")
            line_list = data.readlines()
            print("\nList of Lines\n")
            for i in line_list:
                print(i, end='')
            data.close()
            # CHOOSE THE LINE
            data = open("data.txt", "r")
            print("\nWrite the line number you want to delete: ", end='')
            line_number = input()
            deleted_line = -1
            # VERIFY WITCH LINE IN DATA MUST BE DELETED
            for i in range(len(line_list)):
                verify = data.readline(2)
                print(verify)
                if verify == line_number:
                    deleted_line = int(i)
                next_line = data.readline()  # MAKE THE PROGRAM GO TO NEXT LINE
            # IF THE LINE WAS NOT FOUND
            if deleted_line == -1:
                print("\nThis line was not found")
                print("\nType 1 to try again ou 0 to go back\n")
                selection = input()
                # VERIFY IF THE NUMBER TYPED BY THE USER IS VALID
                if selection == "1":
                    selection = 1
                elif selection == "0":
                    data.close()
                    selection = 0
                else:
                    print("\nInvalid number typed, returning to menu...\n")
                    data.close()
                    selection = 0
            # IF THE LINE WAS FOUND
            else:
                # REMOVE FROM THE LIST OF LINES THE DELETED LINE
                line_list.pop(deleted_line)
                print(line_list)
                data.close()
                # WIPE ALL CONTENT FROM THE DATA FILE
                data = open("data.txt", "w")
                data.write('')
                data.close()
                # WRITE THE NEW LIST OF LINES IN DATA FILE
                data = open("data.txt", "a")
                print(line_list)
                for i in range(len(line_list)):
                    data.write(line_list[i])
                data.close()
                print("\nType 1 to delete another line and 0 to go back\n")
                selection = input()
                if int(selection) == 1:
                    selection = 1
                elif int(selection) == 0:
                    data.close()
                    selection = 0
                # IF THE NUMBER TYPED IS INVALID, RETURN TO MENU ANYWAY
                else:
                    print("\nInvalid number typed, returning to menu...\n")
                    data.close()
                    selection = 0

    # DELETE A SCHEDULE
    elif selection == "6":
        print("6")

    # EXIT PROGRAM
    elif selection == "7":
        SystemExit()

    # WRONG NUMBER
    else:
        print("Select a valid option!\n")
        selection = 0
