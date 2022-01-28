import os


def verify_lines(vl_list, vl_line):
    vl_chosen_line = -1  # IF THE LINE WASN'T FOUND RETURN -1
    vl_data = open("./data/lines.txt", "r")
    for vl_counter in range(len(vl_list)):
        vl_verify = vl_data.readline(2)  # READ THE 2 FIRST DIGITS OF EACH LINE
        if vl_verify == vl_line:
            vl_chosen_line = int(vl_counter)  # IF THE VERIFIED DIGIT IS OK, RETURN THE LIST POSITION OF IT
        vl_data.readline()  # MAKE THE PROGRAM GO TO NEXT LINE
    vl_data.close()
    return vl_chosen_line


def show_lines_list():
    sll_data = open("./data/lines.txt")
    sll_line_list = sll_data.readlines()
    print("\nList of Lines\n")
    for sll_counter in sll_line_list:  # LOOP TO PRINT EACH LINE IN LIST
        print(sll_counter, end='')
    sll_data.close()
    return sll_line_list


def get_lines_list():
    gll_data = open("./data/lines.txt")
    gll_line_list = gll_data.readlines()
    gll_data.close()
    return gll_line_list


def binary_selection(bs_selection):
    match bs_selection:
        # RETURNS THE SELECTION FIRST AND THEN THE SUB_SELECTION
        case "1":
            return 1, 0
        case "0":
            return 0, 0
        case _:
            print("\nInvalid number typed, try again:", end=' ')
            return 0, 1


selection = 0

# CREATE DATA FILES AND DIRECTORY IF IT DOES NOT EXIST

if not os.path.isdir("./data"):
    os.makedirs("./data")

if not os.path.isfile("./data/lines.txt"):
    data = open("./data/lines.txt", "x")
    data.close()

if not os.path.isfile("./data/schedules.txt"):
    data = open("./data/schedules.txt", "x")
    data.close()

if not os.path.isfile("./data/vehicles.txt"):
    data = open("./data/vehicles.txt", "x")
    data.close()

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
    print("2. See the lines schedule")
    print("3. See the vehicle list")
    print("4. See a vehicle schedule")
    print("5. Add a new line")
    print("6. Add a new schedule")
    print("7. Delete a line")
    print("8. Delete a schedule")
    print("9. Exit Program\n")

    selection = input()

    match selection:
        # SEE LINE LIST
        case ("1"):
            show_lines_list()
            print("\nType anything to go back\n")
            input()
            selection = 0
        # SEE LINES SCHEDULE
        case ("2"):
            print("WIP")
        # SEE THE VEHICLE LIST
        case ("3"):
            data = open("./data/vehicles.txt")
            vehicle_list = data.readlines()
            print("\nList of Vehicles\n")
            for counter in vehicle_list:  # LOOP TO PRINT EACH LINE IN LIST
                print(counter, end='')
            data.close()
            print("\nType anything to go back\n")
            input()
            selection = 0
        # SEE A VEHICLE SCHEDULE
        case ("4"):
            print("WIP")
        # ADD A NEW LINE
        case ("5"):
            selection = 1
            while selection == 1:
                # CREATE THE NAME AND ID OF THE LINE AND STORES IN DATA FILE
                data = open("./data/lines.txt", "a")
                print("\nWrite the line number, (two digits):", end=' ')
                sub_selection = 1
                line_number = 0
                line_list = get_lines_list()
                while sub_selection == 1:
                    line_number = input()
                    chosen_line = verify_lines(line_list, line_number)
                    # VERIFY IF THE LINE NUMBER IS VALID
                    if len(line_number) > 2 or len(line_number) < 2 or int(line_number) <= 0 or chosen_line != -1:
                        print("\nInvalid number typed, try again:", end=' ')
                        sub_selection = 1
                    else:
                        sub_selection = 0
                print("Write the line name:", end=' ')
                line_name = input()
                data.write(line_number + " " + line_name + "\n")
                print("\nType 1 to add another line or 0 to go back\n")
                data.close()
                sub_selection = 1
                while sub_selection == 1:
                    selection = input()
                    selection, sub_selection = binary_selection(selection)
        # ADD A NEW SCHEDULE
        case ("6"):
            selection = 1
            while selection == 1:
                line_list = show_lines_list()
                print("\nWrite the line number you want to add a schedule:", end=' ')
                line_number = input()
                chosen_line = verify_lines(line_list, line_number)
                if chosen_line == -1:
                    print("\nThis line was not found")
                    print("\nType 1 to try again or 0 to go back:", end=' ')
                    sub_selection = 1
                    while sub_selection == 1:
                        selection = input()
                        selection, sub_selection = binary_selection(selection)
                # IF THE LINE WAS FOUND
                else:
                    data = open("./data/schedules.txt", "a")
                    print("\nWrite the hour of the vehicle, (two digits):", end=' ')
                    sub_selection = 1
                    vehicle_hour = "00"
                    while sub_selection == 1:
                        vehicle_hour = input()
                        # VERIFY IF THE HOUR TYPED IS VALID
                        if len(vehicle_hour) > 2 or len(vehicle_hour) < 2 or int(vehicle_hour) > 23 or int(
                                vehicle_hour) < 0:
                            print("\nInvalid hour typed, try again:", end=' ')
                            sub_selection = 1
                        else:
                            sub_selection = 0
                    print("\nWrite the minutes of the vehicle, (two digits):", end=' ')
                    sub_selection = 1
                    vehicle_minutes = "00"
                    while sub_selection == 1:
                        vehicle_minutes = input()
                        # VERIFY IF THE MINUTES TYPED ARE VALID
                        if len(vehicle_minutes) > 2 or len(vehicle_minutes) < 2 or int(vehicle_minutes) > 59 or int(
                                vehicle_minutes) < 0:
                            print("\nInvalid minutes typed, try again:", end=' ')
                            sub_selection = 1
                        else:
                            sub_selection = 0
                    print("\nWrite the vehicle code, (five digits):", end=' ')
                    sub_selection = 1
                    vehicle_code = "00000"
                    while sub_selection == 1:
                        vehicle_code = input()
                        # VERIFY IF THE VEHICLE CODE IS VALID
                        if len(vehicle_code) != 5 or not vehicle_code.isdecimal():
                            print("\nInvalid code typed, try again:", end=' ')
                            sub_selection = 1
                        else:
                            # VERIFY IF THE VEHICLE ALREADY IS IN DATA FILE, IF ISN'T, ADD
                            data_extra = open("./data/vehicles.txt", "r")
                            vehicle_list = data_extra.readlines()
                            data_extra.close()
                            vehicle_extra = False
                            data_extra = open("./data/vehicles.txt", "r")
                            for counter in range(len(vehicle_list)):
                                vehicle_verify = data_extra.readline(5)  # READ THE 5 FIRST DIGITS OF EACH LINE
                                if vehicle_verify == vehicle_code:
                                    vehicle_extra = True
                                data_extra.readline()  # MAKE THE PROGRAM GO TO NEXT LINE
                            data_extra.close()
                            if not vehicle_extra:
                                data_extra = open("./data/vehicles.txt", "a")
                                data_extra.write(vehicle_code + "\n")
                                data_extra.close()
                                sub_selection = 0
                            else:
                                sub_selection = 0
                    print("\nWrite a description, (optional):", end=' ')
                    vehicle_description = input()
                    if vehicle_description != "":
                        data.write(line_number + " - " + vehicle_code + " - " + vehicle_hour + ":" + vehicle_minutes +
                                   " " + vehicle_description + "\n")
                    else:
                        data.write(line_number + " - " + vehicle_code + " - " + vehicle_hour + ":" + vehicle_minutes + "\n")
                    print("\nType 1 to add another line or 0 to go back\n")
                    data.close()
                    sub_selection = 1
                    while sub_selection == 1:
                        selection = input()
                        selection, sub_selection = binary_selection(selection)
        # DELETE A LINE
        case ("7"):
            selection = 1
            while selection == 1:
                line_list = show_lines_list()
                # CHOOSE THE LINE
                print("\nWrite the line number you want to delete:", end=' ')
                line_number = input()
                chosen_line = verify_lines(line_list, line_number)
                # IF THE LINE WASN'T FOUND
                if chosen_line == -1:
                    print("\nThis line was not found")
                    print("\nType 1 to try again or 0 to go back:", end=' ')
                    sub_selection = 1
                    while sub_selection == 1:
                        selection = input()
                        selection, sub_selection = binary_selection(selection)
                # IF THE LINE WAS FOUND
                else:
                    # DELETE SCHEDULE FILE OF THE LINE IF IT'S EXIST
                    file_name = line_list[chosen_line]
                    file_name = "schedule_line_" + file_name[0:2] + ".txt"
                    if os.path.isfile("./data/" + file_name):
                        os.remove("./data/" + file_name)
                    # REMOVE FROM THE LIST OF LINES THE DELETED LINE
                    line_list.pop(chosen_line)
                    # WIPE ALL CONTENT FROM THE DATA FILE
                    data = open("./data/lines.txt", "w")
                    data.write('')
                    data.close()
                    # WRITE THE NEW LIST OF LINES IN DATA FILE
                    data = open("./data/lines.txt", "a")
                    for counter in range(len(line_list)):
                        data.write(line_list[counter])
                    data.close()
                    print("\nType 1 to delete another line or 0 to go back\n")
                    sub_selection = 1
                    while sub_selection == 1:
                        selection = input()
                        selection, sub_selection = binary_selection(selection)
        # DELETE A SCHEDULE
        case ("8"):
            print("WIP")
        # EXIT PROGRAM
        case ("9"):
            SystemExit()
        # INVALID NUMBER
        case _:
            print("\nSelect a valid option!\n")
            selection = 0
