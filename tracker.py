import json
import sys


def main_menu():
    print("\n----------Main Menu----------\n")
    print("1-Add task")
    print("2-Mark task done")
    print("3-View calendar and tasks")
    print("4-Remove task")
    print("5-View streaks")
    print("6-Exit")


def get_choice():
    try:
        user = int(input("\nChoose a number from the menu: "))
        return user
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        return None


def add_task():
    """
    1-Adds tasks to help build streaks and habits. tasks are also saved to a json file.
    """


def mark_task_done():
    """
    2-Marks a task as completed. Visually indicates completion (e.g., with a green mark) or non-completion (e.g., with a red mark) if the task was not done.
    """


def view_calendar():
    """
    3-Creates a simple calendar view and displays all associated tasks.
    """


def remove_task():
    """
    4-Remove the selected task from the program.
    """


def view_streaks():
    """
    5-Displays all tracked streaks for the user's tasks.
    """


def main():
    while True:
        main_menu()
        choice = get_choice()
        if choice == 1:
            add_task()
        elif choice == 2:
            mark_task_done()
        elif choice == 3:
            view_calendar()
        elif choice == 4:
            remove_task()
        elif choice == 5:
            view_streaks()
        elif choice == 6:
            print("\ngoodbye!")
            return sys.exit()
        elif choice is None:
            continue
        else:
            print("Option not found. Please try again.")


if __name__ == "__main__":
    main()
