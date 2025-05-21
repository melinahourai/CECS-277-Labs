# Names: Melina Hourai, Leilani Grimaldo, Paige Moua
# Date: 04/29/25
# Group: 2
# Purpose: Create a program that maintains a task list for the user

import check_input
import tasklist


def main_menu():
    """displays the main menu and options for user to chose from"""
    print("1. Display current task\n2. Display all tasks\n3. Mark current task complete\n4. Add new task\n5. Search by date\n6. Save and quit")
    choice = check_input.get_int_range("Enter choice: ", 1, 6) # checks input of user 1-6
    return choice

def get_date():
    """Prompts the user to enter the month, day, and year. Returns the date formatted as: MM/DD/YYYY."""
    print("Enter due date:")
    month_choice = check_input.get_int_range("Enter month: ", 1, 12) # checks user input for valid input of months 1-12
    day_choice = check_input.get_int_range("Enter day: ", 1, 31) # checks user input for valid input of days from 1-31
    year_choice = check_input.get_int_range("Enter year: ", 2020, 2100)
    if month_choice < 10:
        # if user input for month is less than 10, formats it as a string with a 0 added to the front
        month_choice = "0" + str(month_choice)
    if day_choice < 10:
        # if user input for days is less than 10, formats it as a string with a 0 added to the front
        day_choice = "0" + str(day_choice)
    return f"{month_choice}/{day_choice}/{year_choice}" # returns the date input formatted MM/DD/YYYY

def get_time():
    """Prompts the user to enter the hour (military time) and minute."""
    print("Enter time:")
    hour_choice = check_input.get_int_range("Enter hour: ", 0, 23) # checks user input for valid input of hour 0-23
    minute_choice = check_input.get_int_range("Enter minute: ", 0, 59) # checks user input for valid input of minutes 0-59
    # reformats user input as a string if input hour or minute is less than 10, then a 0 is added to the front
    if hour_choice <10:
        hour_choice = "0" + str(hour_choice)
    if minute_choice <10:
        minute_choice = "0" + str(minute_choice)
    return f"{hour_choice}:{minute_choice}" # returns the time formatted as HH:MM

def main():
    task_list = tasklist.TaskList() # creates tasklist object

    while True: # loops until user decides to save file
        print("\n-Tasklist-")
        print(f"Tasks to complete: {len(task_list)}")
        choice = main_menu() # gets users choice for what to do with tasklist
        if choice == 1: # if user wants to display current task
            print(f"Current task: {task_list.get_current_task()}")
        elif choice == 2: # if user wants to see all tasks
            if len(task_list)== 0:
                print("There are no tasks to view")
            else:
                print("Tasks:")
                for i, task in enumerate(task_list, start=1):
                    print(f"{i}. {task}")
        elif choice == 3: # if user wants to mark current task as complete and see new current task
            print(f"Marking current task as complete: {task_list.mark_complete()}")
            print(f"New current task: {task_list.get_current_task()}")
        elif choice == 4: # If user wants to add a new task to task list
            desc = input("Enter a task: ")
            date = get_date()
            time = get_time()
            task_list.add_task(desc, date, time)
        elif choice == 5: # if user wants to search by date
            date = get_date()
            print(f"Tasks due on {date}:")
            matches = []
            for task in task_list:
                if task.date == date:
                    matches.append(task)
            if matches == []:
                print(f"No tasks found for {date}")
            else:
                for j in range(len(matches)):
                    print(f"{j+1}. {matches[j]}")
        elif choice == 6: # If user wants to save and quit
            print("Saving list...")
            task_list.save_file() # Saves updated contents
            break


main()
