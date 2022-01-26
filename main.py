from trucks import *


class Main:


    # total_miles = truck1.total_miles + truck2.total_miles + truck3.total_miles

    print('******************************************')
    print('Welcome to the WGU Package Tracking System')
    print('******************************************')
    user_choice = 1
    user_package_id = 1
    user_time = [1,0]
    while user_choice in range(1,4):
        print('---------------Main Menu-----------------\n'
             'Press 1 for total miles of latest delivery route.\n'
             'Press 2 Display status of ALL packages at a specific time.\n'
             'Press 3 to search for status of a specific package.\n'
             'Press 4 to Exit\n')
        user_choice = int(input())
        if user_choice == 1:
            print(f"Total miles driven to deliver all packages was {(truck1.get_total_miles()+truck2.get_total_miles()):.2f}")
        if user_choice == 2:
            # user_package_id = -1
            # print('Enter the package ID.')
            # while user_package_id > 40 or user_package_id < 0:
            #     try:
            #         user_package_id = int(input(''))
            #         if user_package_id > 40 or user_package_id< 0:
            #             print('Please enter a valid package ID.')
            #     except Exception:
            #         print('Please enter a valid package ID.')
            user_time = [13,61]
            print('Enter package time in format HH:MM')
            while user_time[0] > 12 or user_time[1] > 59:
                try:
                    string_user_time = input("").split(':')
                    user_time[0] = int(string_user_time[0])
                    user_time[1] = int(string_user_time[1])

                    if user_time[0] not in range(1, 13) or user_time[1] not in range(0, 60):
                        print('Please enter valid time in the format HH:MM, Hours must be 12 or less and minutes 60 or less')
                except Exception:
                    print('Please enter valid time format HH:MM, Hours must be 12 or less and minutes 60 or less')
                    #user_time = [13, 00]
            package_list.status_all_packages(string_user_time)

        if user_choice == 3:
            user_package_id = -1
            print('Enter the package ID.')
            while user_package_id > 40 or user_package_id < 0:
                try:
                    user_package_id = int(input(''))
                    if user_package_id > 40 or user_package_id< 0:
                        print('Please enter a valid package ID.')
                except Exception:
                    print('Please enter a valid package ID.')
            user_time = [13,61]
            print('Enter package time in format HH:MM')
            while user_time[0] > 12 or user_time[1] > 59:
                try:
                    string_user_time = input("").split(':')
                    user_time[0] = int(string_user_time[0])
                    user_time[1] = int(string_user_time[1])
                    if user_time[0] not in range(1, 13) or user_time[1] not in range(0, 60):
                        print('Please enter valid time in the format HH:MM, Hours must be less than 12 and minutes less than 60')
                except Exception:
                    print('Please enter valid time format HH:MM, Hours must be equal or less than 12 and minutes less than 60')
                    user_time = [13, 00]
            package_list.status_one_package(user_package_id, string_user_time)