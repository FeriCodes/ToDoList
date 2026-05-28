import json
import sys
import os


def main_menu():
    print("\n----------Main Menu----------\n")
    print("1-Add task")
    print("2-Mark task done")
    print("3-View calendar")
    print("4-Remove task")
    print("5-View streaks")
    print("6-show all the tasks")
    print("7-Exit")


def load_file():
    """this is for read the "tasks.json" file and if the file dosen't exsist then return an empty list for prevent the an Error."""
    if not os.path.exists("tasks.json"):
        return []

    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:

        return []


def write_file(tasks_list):
    """this is can write the file when user give the program an input."""

    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks_list, file, indent=4, ensure_ascii=False)


def get_choice():
    try:
        user = int(input("\nChoose a number from the menu: "))
        return user
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        return None


def select_task(tasks_list):

    if show_tasks(tasks_list) is False:
        return None
    try:
        task_number = int(
            input("Enter the number of the task you completed: "))

        if task_number <= 0 or task_number > len(tasks_list):
            print("❌ Error: Task number out of range!")
            return None
        return task_number - 1
    
    except ValueError:
        print("❌ Error: please enter a number")


def add_task():
    """
    1-Adds tasks to help build streaks and habits. tasks are also saved to a json file.
    """
    while True:
       

        activity_name = input("Enter the task or habit you want to add: ")

        if activity_name.isdigit():
            print("❌ please enter a task instead the numbers.")
            continue

        if not activity_name:
            print("❌ Task name cannot be empty.")
            continue

        # open the file even if dosen't exsist this can make a new file name "tasks.json"
        tasks_list = load_file()

        new_task = {
            "task": activity_name,
            "streak": 0,
            "done_today": False
        }

        tasks_list.append(new_task)

        # write down on the file by the users input
        write_file(tasks_list)

        print(f"✅ '{activity_name}' added successfully!")

        asking = input(
            "Do you want to add another task? (y/n): ").lower().strip()

        if asking == "y":
            continue
        elif asking == "n":
            break
        else:
            print("❌ Invalid input! Please enter 'y' or 'n'.")
            break


def mark_task_done(tasks_list):
    """
    2-Marks a task as completed.
    """
    index = select_task(tasks_list)

    if tasks_list is None or index is None:
        return

    selected_task = tasks_list[index]

    user_done = input(
        f"are you done the {selected_task['task']} task? (y/n): ").strip().lower()

    if user_done == "y":
        selected_task["streak"] += 1
        selected_task["done_today"] = True
        print("🔥 Great job! Streak updated.")
    elif user_done == "n":
        selected_task["streak"] = 0
        selected_task["done_today"] = False
        print("❌ Streak reset. Consistency is key!")
    else:
        print("❌ Invalid input!")
        return

    write_file(tasks_list)


def view_calendar():
    """
    3-Creates a simple calendar view and displays all associated tasks.
    """
    pass


def remove_task(tasks_list):
    """
    4-Remove the selected task from the program.
    """
    index = select_task(tasks_list)
    if index is None:
        return 
    
    selected_task = tasks_list[index]

    confrim = input(f"Are you sure you want to remove {selected_task['task']}?: (y/n)")
    if confrim == "y":
        tasks_list.pop(index)
        write_file(tasks_list) 
        print("✅Task removed succssfully!")
    else:
        print("❌Removal canceled.")


def view_streaks():
    """
    5-Displays all tracked streaks for the user's tasks.
    """
    pass 


def show_tasks(tasks_list):
    """
    6-Displays all the tasks which you add to the "tasks.json" file.
    """
    if not tasks_list:
        print("no tasks found. add some tasks.")
        return False
    
    # this is for choose the every task you want.
    print("\n--- Your Tasks---")
    for index, item in enumerate(tasks_list):
        status = "✅" if item['done_today'] else "❌"
        print(f"{index + 1}. Task: {item['task']} | Streak: {item['streak']} | status: {status}")

    return True

def main():
    while True:
        current_tasks = load_file()

        main_menu()
        choice = get_choice()
        if choice == 1:
            add_task()
        elif choice == 2:
            mark_task_done(current_tasks)
        elif choice == 3:
            view_calendar()
        elif choice == 4:
            remove_task(current_tasks)
        elif choice == 5:
            view_streaks()
        elif choice == 6:
            show_tasks(current_tasks)
        elif choice == 7:
            print("\ngoodbye!")
            return sys.exit()
        elif choice is None:
            continue
        else:
            print("Option not found. Please try again.")


if __name__ == "__main__":
    main()
