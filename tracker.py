import json
import sys
import os


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
    while True:

        activity_name = input("Enter the task or habit you want to add: ")

        if activity_name.isdigit():
            print("please enter a task instead the numbers.")
            continue

        if os.path.exists("tasks.json"):

            with open("tasks.json", "r", encoding="utf-8") as file:
                tasks_list = json.load(file)
        else:
            tasks_list = []

        new_task = {
            "task": activity_name,
            "streak": 0,
            "done_today": False
        }

        tasks_list.append(new_task)

        # if the file dosen't exsits this can create the file
        with open("tasks.json", "w", encoding="utf-8") as file:
            json.dump(tasks_list, file, indent=4)

        print(f"✅ '{activity_name}' added successfully!")

        asking = input(
            "Do you want to add another task? (y/n): ").lower().strip()

        if asking == "y":
            continue
        elif asking == "n":
            break
        else:
            print("❌ Invalid input! Please enter 'y' or 'n'.")


def mark_task_done():
    """
    2-Marks a task as completed. Visually indicates completion (e.g., with a green mark) or non-completion (e.g., with a red mark) if the task was not done.
    """
    with open("tasks.json", "r", encoding="utf-8") as file:
        tasks_list = json.load(file)

    # this is for choose the every task you want.
    for index, item in enumerate(tasks_list):
        print(f"{index + 1}. Task: {item['task']} | Streak: {item['streak']}")

    try:
        task_number = int(
            input("Enter the number of the task you completed: "))
        if task_number <= 0:
            print("❌ Error: The number must be 1 or higher!")
            return

        index = task_number - 1

        if index >= len(tasks_list):
            print("❌ Error: Task number out of range!")
            return

        selected_task = tasks_list[index]
        user_done = input(
            f"are you done the {selected_task["task"]} task? (y/n): ")

        if user_done == "y":
            selected_task["streak"] += 1
            selected_task["done_today"] = True
            print("🔥 Great job! Streak updated.")

        elif user_done == "n":
            selected_task["streak"] = 0
            selected_task["done_today"] = False
            print("❌ Streak reset. Consistency is key!")

        with open("tasks.json", "w", encoding="utf-8") as file:
            json.dump(tasks_list, file, indent=4)

    except ValueError:
        print("❌ Error: please enter a number")


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
