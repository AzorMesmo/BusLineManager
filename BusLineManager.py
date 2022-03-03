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


def verify_schedule_lines(vsl_list, vsl_line):
    vsl_chosen_line = []  # IF THE LINE WASN'T FOUND RETURN AN EMPTY LIST
    vsl_data = open("./data/schedules.txt", "r")
    for vsl_counter in range(len(vsl_list)):
        vsl_verify = vsl_data.readline(2)  # READ THE 2 FIRST DIGITS OF EACH LINE
        if vsl_verify == vsl_line:
            vsl_chosen_line.append(int(vsl_counter))  # IF THE VERIFIED DIGIT IS OK, RETURN THE LIST POSITION OF IT
        vsl_data.readline()  # MAKE THE PROGRAM GO TO NEXT LINE
    vsl_data.close()
    return vsl_chosen_line


def get_lines_list(gll_show):
    gll_data = open("./data/lines.txt")
    gll_line_list = gll_data.readlines()
    if gll_show:
        print("\nList of Lines\n")
        for gll_counter in gll_line_list:  # LOOP TO PRINT EACH LINE IN LIST
            print(gll_counter, end='')
    gll_data.close()
    return gll_line_list


def get_schedules_list():
    gsl_data = open("./data/schedules.txt")
    gsl_line_list = gsl_data.readlines()
    gsl_data.close()
    return gsl_line_list


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
            get_lines_list(True)
            print("\nType anything to go back\n")
            input()
            selection = 0
        # SEE LINES SCHEDULE
        case ("2"):
            line_list = get_lines_list(True)
            print("\nWrite the line number you want to see the schedule:", end=' ')
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
                print("")
                data = open("./data/schedules.txt")
                schedule_list = data.readlines()
                data.close()
                data = open("./data/schedules.txt")
                for counter in schedule_list:
                    line_number_extra = data.readline(2)
                    if line_number_extra == line_number:
                        vehicle_code = data.readline(8)
                        data.readline(3)  # SKIP THREE CHARACTERS
                        vehicle_time = data.readline(5)
                        print(vehicle_time + vehicle_code)
                    data.readline()  # GO TO NEXT LINE
            print("\nType anything to go back\n")
            input()
            selection = 0
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
                line_list = get_lines_list(False)
                while sub_selection == 1:
                    line_number = input()
                    chosen_line = verify_lines(line_list, 'lines.txt')
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
                line_list = get_lines_list(True)
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
                        # VERIFY IF THE SAME VEHICLE ISN'T USED MULTIPLE TIMES AT THE SAME TIME
                        data.extra = open("./data/schedules.txt", "r")
                        schedule_list = data.extra.readlines()
                        data.extra.close()
                        data.extra = open("./data/schedules.txt", "r")
                        for counter in schedule_list:
                            data.extra.readline(5)  # SKIP THE FIRST FIVE CHARACTERS OF EACH LINE
                            verify_vehicle_code = data.extra.readline(5)  # GET THE CODE IN SCHEDULE
                            data.extra.readline(3)  # SKIP MORE THREE CHARACTERS
                            verify_vehicle_hour = data.extra.readline(2)  # GET THE HOUR IN SCHEDULE
                            data.extra.readline(1)  # SKIP MORE ONE CHARACTER
                            verify_vehicle_minutes = data.extra.readline(2)  # GET THE MINUTES IN SCHEDULE
                            data.extra.readline()  # GO TO NEXT LINE
                            if vehicle_code == verify_vehicle_code and vehicle_hour == verify_vehicle_hour and \
                                    vehicle_minutes == verify_vehicle_minutes:
                                print("\nThis vehicle already has a route at this time, try again:", end=' ')
                                sub_selection = 1
                    print("\nWrite a description, (optional):", end=' ')
                    vehicle_description = input()
                    if vehicle_description != "":
                        data.write(line_number + " - " + vehicle_code + " - " + vehicle_hour + ":" + vehicle_minutes +
                                   " " + vehicle_description + "\n")
                    else:
                        data.write(
                            line_number + " - " + vehicle_code + " - " + vehicle_hour + ":" + vehicle_minutes + "\n")
                    data.close()
                    print("\nType 1 to add another schedule or 0 to go back\n")
                    sub_selection = 1
                    while sub_selection == 1:
                        selection = input()
                        selection, sub_selection = binary_selection(selection)
        # DELETE A LINE
        case ("7"):
            selection = 1
            while selection == 1:
                line_list = get_lines_list(True)
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
                    # CREATE A SCHEDULE LIST AND AN ARRAY WITH THE SCHEDULES TO BE DELETED
                    schedule_list = get_schedules_list()
                    chosen_schedules = verify_schedule_lines(schedule_list, line_number)
                    if chosen_schedules:
                        # REMOVE FROM THE SCHEDULES LIST THE DELETED LINE SCHEDULES
                        for counter in chosen_schedules:
                            schedule_list.pop(counter)
                        # WIPE ALL CONTENT FROM THE DATA FILE
                        data = open("./data/schedules.txt", "w")
                        data.write('')
                        data.close()
                        # WRITE THE NEW LIST OF SCHEDULES IN DATA FILE
                        data = open("./data/schedules.txt", "a")
                        for counter in range(len(schedule_list)):
                            data.write(schedule_list[counter])
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
