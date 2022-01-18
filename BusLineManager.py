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

    selection = input()

    # SEE LINE LIST
    if selection == "1":
        data = open("data.txt")
        line_list = data.readlines()
        print("")
        for i in line_list:
            print(i)
        print("\nType anything to go back")
        input()
        selection = 0

    # SEE LINE SCHEDULES
    elif selection == "2":
        print("2")

    # ADD A NEW LINE
    elif selection == "3":
        selection = 1
        while selection == 1:
            # CREATE THE NAME AND ID OF THE LINE AND STORES IN DATA FILE
            data = open("data.txt", "w")
            print("\nWrite the line number:")
            line_number = input()
            print("Write the line name:")
            line_name = input()
            data.write(line_number + " " + line_name + "\n")
            print("\nType 1 to add another line and 0 to go back\n")
            selection = input()
            if int(selection) == 1:
                selection = 1
            elif int(selection) == 0:
                selection = 0
                data.close()
            # IF THE NUMBER TYPED IS INVALID, RETURN TO MENU ANYWAY
            else:
                print("\nInvalid number typed, returning to menu...")
                selection = 0
                data.close()

    # ADD A NEW SCHEDULE
    elif selection == "4":
        print("4")

    # DELETE A LINE
    elif selection == "5":
        print("5")

    # DELETE A SCHEDULE
    elif selection == "6":
        print("6")

    # WRONG NUMBER
    else:
        print("Select a valid option!")
        selection = 0