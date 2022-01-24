def verify_lines(vl_list, vl_line):
    chosen_line = -1  # IF THE LINE WASN'T FOUND RETURN -1
    vl_data = open("data_lines.txt", "r")
    for vl_counter in range(len(vl_list)):
        vl_verify = vl_data.readline(2)  # READ THE 2 FIRST DIGITS OF EACH LINE
        if vl_verify == vl_line:
            chosen_line = int(vl_counter)  # IF THE VERIFIED DIGIT IS OK, RETURN THE LIST POSITION OF IT
        vl_data.readline()  # MAKE THE PROGRAM GO TO NEXT LINE
    vl_data.close()
    return chosen_line


def show_lines_list():
    sll_data = open("data_lines.txt")
    sll_line_list = sll_data.readlines()
    print("\nList of Lines\n")
    for sll_counter in sll_line_list:  # LOOP TO PRINT EACH LINE IN LIST
        print(sll_counter, end='')
    sll_data.close()
    return sll_line_list


selection = 0

# WELCOME MESSAGE

print("\n===================================")
print("║                                 ║")
print("║   Welcome to Bus Line Manager   ║")
print("║                                 ║")
print("===================================")

while selection == 0:

    # MENU

    print("\nType the respective number to navigate\n")
    print("1. See the line list")
    print("2. See the line schedules")
    print("3. Add a new line")
    print("4. Add a new schedule")
    print("5. Delete a line")
    print("6. Delete a schedule")
    print("7. Exit Program\n")

    selection = input()

    match selection:
        # SEE LINE LIST
        case ("1"):
            show_lines_list()
            print("\nType anything to go back\n")
            input()
            selection = 0
        # SEE LINE SCHEDULES
        case ("2"):
            print("WIP")
        # ADD A NEW LINE
        case ("3"):
            selection = 1
            while selection == 1:
                # CREATE THE NAME AND ID OF THE LINE AND STORES IN DATA FILE
                data = open("data_lines.txt", "a")
                print("\nWrite the line number, (two digits):", end=' ')
                line_number = input()
                # VERIFY IF THE LINE NUMBER IS VALID
                if len(line_number) > 2 or len(line_number) < 2 or int(line_number) <= 0:
                    print("\nInvalid number, returning to menu...\n")
                    selection = 0
                    break
                print("Write the line name:", end=' ')
                line_name = input()
                data.write(line_number + " " + line_name + "\n")
                print("\nType 1 to add another line or 0 to go back\n")
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
        case ("4"):
            print("WIP")
        # DELETE A LINE
        case ("5"):
            selection = 1
            while selection == 1:
                line_list = show_lines_list()
                # CHOOSE THE LINE
                print("\nWrite the line number you want to delete:", end=' ')
                line_number = input()
                deleted_line = verify_lines(line_list, line_number)
                # IF THE LINE WASN'T FOUND
                if deleted_line == -1:
                    print("\nThis line was not found")
                    print("\nType 1 to try again or 0 to go back:", end=' ')
                    sub_selection = 1
                    while sub_selection == 1:
                        selection = input()
                        # VERIFY IF THE NUMBER TYPED BY THE USER IS VALID
                        if selection == "1":
                            selection = 1
                            sub_selection = 0
                        elif selection == "0":
                            selection = 0
                            sub_selection = 0
                        else:
                            print("\nInvalid number typed, try again:", end=' ')
                            sub_selection = 1
                # IF THE LINE WAS FOUND
                else:
                    # REMOVE FROM THE LIST OF LINES THE DELETED LINE
                    line_list.pop(deleted_line)
                    # WIPE ALL CONTENT FROM THE DATA FILE
                    data = open("data_lines.txt", "w")
                    data.write('')
                    data.close()
                    # WRITE THE NEW LIST OF LINES IN DATA FILE
                    data = open("data_lines.txt", "a")
                    for counter in range(len(line_list)):
                        data.write(line_list[counter])
                    data.close()
                    print("\nType 1 to delete another line or 0 to go back\n")
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
        case ("6"):
            print("WIP")
        # EXIT PROGRAM
        case ("7"):
            SystemExit()
        # INVALID NUMBER
        case _:
            print("\nSelect a valid option!\n")
            selection = 0
