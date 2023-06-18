# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this program in your IDE otherwise the 
# program will look in your root directory for the text files.

#========Importing libraries========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

# Read tasks.txt and split contents into a list of strings
with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    # Remove any empty strings from the list
    task_data = [t for t in task_data if t != ""]

# Initialize an empty list to store the task dictionaries
task_list = []

# Loop through each string in the task_data list
for t_str in task_data:
    # Initialize an empty dictionary to store the task components
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    # Add the curr_t dictionary to the task_list
    task_list.append(curr_t)


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file exists, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary with lowercase usernames
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username.lower()] = password

logged_in = False
while not logged_in:

    # Prompt the user for their username and password
    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")

    # Check to see if the user entered exists in the username_password dictionary
    if curr_user.lower() not in username_password.keys():
        print("User does not exist")
        continue
    # Check to see see if the password is correct for the given username
    elif username_password[curr_user.lower()] != curr_pass:
        print("Wrong password... Password IS Case-Sensitive")
        continue
    else:
        print("Login Successful!")
        logged_in = True

#=========Defining Functions=========
# Function to check is a user exists
def user_exists(username):
    with open("user.txt", "r") as file:
        for line in file:
            user_info = line.strip().split(";")
            if user_info[0] == username:
                return True
    return False

# ===========================
# Function to register a user
def reg_user():
    # Loop until a unique username is entered that is not blank
    while True:
        username = input("Please enter a username: ").strip()
        if not username:
            print("Username cannot be blank. Please try again.")
            continue

        # Check if the username already exists in the file
        with open("user.txt", "r") as f:
            for line in f:
                if username.lower() == line.strip().split(";")[0].lower():
                    print("Username already exists. Please try again.")
                    break
            else:
                break
            
    # Loop until the user enters a password that is not blank and matches the confirmation password
    while True:
        password = input("Please enter a password: ").strip()
        if not password:
            print("Password cannot be blank. Please try again.")
            continue
            
        confirm_password = input("Please confirm your password: ").strip()
        if password == confirm_password:
            break
        else:
            print("Passwords do not match. Please try again.")

    # Write the new user to the file, with the username converted to lowercase
    with open("user.txt", "a") as f:
        f.write(f"\n{username.lower()};{password}")
    
    print("\nRegistration successful!")

# ==========================
# Function to add a new task
def add_task():
    # Read the list of users from the user file
    with open("user.txt", "r") as user_file:
        user_list = [line.split(";")[0] for line in user_file.read().splitlines()]

    # Loop until a valid user is assigned to the task, converting to lowercase as the usernames are converted to lowercase
    while True:
        assigned_to = input("Who is the task assigned to? ")
        assigned_to = assigned_to.lower()
        if assigned_to in [user.lower() for user in user_list]:
            break
        else:
            print("User not found. Please enter a valid username.")

    # Loop until the user inputs a non-empty title for the task
    while True:
        task_title = input("Title of task: ")
        if task_title.strip() != '':
            break
        else:
            print("Task title cannot be empty. Please try again.")

    # Loop until the user inputs a non-empty description for the task
    while True:
        task_description = input("Description of task: ")
        if task_description.strip() != '':
            break
        else:
            print("Task description cannot be empty. Please try again.")

    # Loop until the user inputs a deadline in the correct format
    while True:
        deadline = input("When is the deadline for this task? (YYYY-MM-DD) ")
        try:
            # Convert the deadline string to a date object
            deadline_dt = datetime.strptime(deadline, DATETIME_STRING_FORMAT).date()
            break
        except ValueError:
            print("Incorrect date format. Please enter the date in the format YYYY-MM-DD.")

    # Get the current date as the assigned date
    assigned_date = datetime.now().date()
    # Set completed to False, as the task is not completed when it is added
    completed = False
    
    # Write the task to the file
    with open("tasks.txt", "a") as f:
        f.write(f"\n{assigned_to};{task_title};{task_description};{deadline_dt};{assigned_date};{'Yes' if completed else 'No'}")
    print("Task added successfully!\n")

# ==========================
# Function to view all tasks
def view_all(task_list):
    if task_list:
        print("\nAll tasks:\n")
        for task in task_list:
            print(f"Username: {task['username']}\nTask title: {task['title']}\nTask description: {task['description']}\nAssigned date: {task['assigned_date'].strftime('%Y-%m-%d')}\nDue date: {task['due_date'].strftime('%Y-%m-%d')}\nCompleted: {'Yes' if task['completed'] else 'No'}\n{'-'*50}\n")
    else:
        print("No tasks found.\n")

# =======================================
# Function to view tasks assigned to user
def view_mine(logged_in_user):
    all_tasks = []
    user_tasks = []

    # Read the tasks from file
    with open("tasks.txt", "r") as file:
        for line in file:
            task = line.strip().split(";")
            all_tasks.append(task)
            if task[0] == logged_in_user:
                user_tasks.append(task)

    # If the user has any tasks, they will be displayed in an easy to read manner
    if user_tasks:
        while True:
            print(f"\nAll tasks assigned to {logged_in_user}:")
            for i, task in enumerate(user_tasks):
                completed = "Yes" if task[5] == "Yes" else "No"
                print(f"{i+1}. Task: {task[1]}\n   Description: {task[2]}\n   Assigned to: {task[3]}\n   Deadline: {task[4]}\n   Completed: {completed}")

            # Prompt the user to select a task to view, or return to the main menu
            print("Enter the number of the task you would like to view, or enter -1 to return to the main menu.")
            choice = input("Choice: ")

            if choice == '-1':
                break
            try:
                index = int(choice) - 1
                selected_task = user_tasks[index]
                all_tasks_index = all_tasks.index(selected_task)

                # Display selected task details
                print(f"\nTask: {selected_task[1]}\nDescription: {selected_task[2]}\nAssigned to: {selected_task[3]}\nAssigned date: {selected_task[5]}\nDeadline: {selected_task[4]}\nCompleted: {selected_task[5]}\n")
                
                # If the task is not complete, give the user the option to mark as complete or edit it
                if selected_task[5] == "No":
                    edit_choice = input("Do you want to mark the task as complete or edit the task?\nEnter 'C' to mark the task as complete, 'E' to edit the task, or enter any other key to return to the main menu:\n")
                    
                    # Mark the task as complete
                    if edit_choice.lower() == 'c':
                        selected_task[5] = "Yes"
                        all_tasks[all_tasks_index] = selected_task
                        print("Task marked as complete.")
                    
                    # Edit the task
                    elif edit_choice.lower() == 'e':
                        edit_option = input("Enter 'U' to change the assigned user, 'D' to change the due date, or enter any other key to return to the main menu:\n")
                        
                        # Changing the assigned user, and checking to see if the username already exists
                        if edit_option.lower() == 'u':
                            while True:
                                new_user = input("Enter the username of the new user: ").lower()
                                if user_exists(new_user):
                                    selected_task[0] = new_user
                                    all_tasks[all_tasks_index] = selected_task
                                    print("\nTask assigned to", new_user)
                                    break
                                else:
                                    print("\nUser does not exist.\n")

                        # Changing the due date, and checking to ensure the date is entered in the correct format
                        elif edit_option.lower() == 'd':
                            while True:
                                new_date = input("Enter the new due date (YYYY-MM-DD): ")
                                try:
                                    datetime.strptime(new_date, DATETIME_STRING_FORMAT).date()
                                    selected_task[4] = new_date
                                    all_tasks[all_tasks_index] = selected_task
                                    print("\nDue date changed to", new_date)
                                    break
                                except ValueError:
                                    print("Incorrect date format. Please enter the date in the format YYYY-MM-DD.")
                        else:
                            break
                    else:
                        break
                else:
                    print("This task has already been completed and cannot be edited.\n")
                    continue
            except (ValueError, IndexError):
                print("\nInvalid choice. Please select a number from the list.\n")
    else:
        print(f"No tasks found for {logged_in_user}.\n")

    # Write the updated task list to the file
    with open("tasks.txt", "w") as file:
        for task in all_tasks:    
            file.write(";".join(task) + "\n")      

# ============================
# Function to generate reports
def generate_reports():
    # Calculating the necessary information for the report for task_overview.txt
    total_tasks = len(task_list)
    completed_tasks = len([t for t in task_list if t['completed']])
    incompleted_tasks = total_tasks - completed_tasks
    overdue_tasks = len([t for t in task_list if not t['completed'] and t['due_date'].date() < datetime.today().date()])
    incomplete_percentage = (incompleted_tasks / total_tasks) * 100
    overdue_percentage = (overdue_tasks / total_tasks) * 100

    # Writing the report to task_overview.txt
    with open('task_overview.txt', 'w') as file:
        file.write(f'Total number of tasks: {total_tasks}\n')
        file.write(f'Total number of completed tasks: {completed_tasks}\n')
        file.write(f'Total number of incompleted tasks: {incompleted_tasks}\n')
        file.write(f'Total number of overdue tasks: {overdue_tasks}\n')
        file.write(f'Percentage of tasks that are incomplete: {incomplete_percentage:.2f}%\n')
        file.write(f'Percentage of tasks that are overdue: {overdue_percentage:.2f}%')
    
    # Calculating the total number of users and tasks
    user_task_count = {}
    for task in task_list:
        username = task['username']
        if username not in user_task_count:
            user_task_count[username] = {
                'total': 0,
                'completed': 0,
                'overdue': 0
            }
        user_task_count[username]['total'] += 1
        if task['completed']:
            user_task_count[username]['completed'] += 1
        elif task['due_date'].date() < datetime.today().date():
            user_task_count[username]['overdue'] += 1

    # Writing total number of users and tasks to file
    with open('user_overview.txt', 'w') as file:
        file.write(f'Total number of users: {len(user_task_count)}\n')
        file.write(f'Total number of tasks: {total_tasks}\n')

        # Calculating the remaining information needed, for each user, for the report for user_overview.txt
        for user, task_count in user_task_count.items():
            assigned_percentage = (task_count['total'] / total_tasks) * 100
            completed_percentage = (task_count['completed'] / task_count['total']) * 100
            incompleted_percentage = 100 - completed_percentage
            overdue_percentage = (task_count['overdue'] / task_count['total']) * 100
            
            # Writing the report to user_overview.txt
            file.write(f'\nUser: {user}\n')
            file.write(f'Total tasks assigned: {task_count["total"]} ({assigned_percentage:.2f}% of all tasks)\n')
            file.write(f'Completed tasks: {task_count["completed"]} ({completed_percentage:.2f}% of assigned tasks)\n')
            file.write(f'incompleted tasks: {task_count["total"] - task_count["completed"]} ({incompleted_percentage:.2f}% of assigned tasks)\n')
            file.write(f'Overdue tasks: {task_count["overdue"]} ({overdue_percentage:.2f}% of assigned tasks)\n')

    print("\nYou have successfully generated the reports 'task_overview.txt' and 'user_overview.txt'")

# ==============================
# Function to display statistics
def display_stats():
    # Read task data from the file
    with open("tasks.txt", "r") as task_file:
        task_data = task_file.read().split("\n")
        task_data = [t for t in task_data if t != ""]

    # Count the total number of tasks, completed tasks and overdue tasks
    total_tasks = len(task_data)
    completed_tasks = sum([1 for t in task_data if t.split(";")[5] == "Yes"])
    today = date.today()
    overdue_tasks = 0
    for t in task_data:
        task_due_date = datetime.strptime(t.split(";")[4], "%Y-%m-%d").date()
        if task_due_date < today and t.split(";")[5] != "Yes":
            overdue_tasks += 1

    # Calculate the percentages of complete, incomplete and overdue tasks
    completed_percentage = (completed_tasks / total_tasks) * 100
    incomplete_percentage = ((total_tasks - completed_tasks) / total_tasks) * 100
    overdue_percentage = (overdue_tasks / total_tasks) * 100

    print(f"\nTotal tasks: {total_tasks}")
    print(f"Total completed tasks: {completed_tasks}")
    print(f"Total incompleted tasks: {total_tasks - completed_tasks}")
    print(f"Total overdue tasks: {overdue_tasks}")
    print(f"Percentage of tasks that are complete: {completed_percentage:.2f}%")
    print(f"Percentage of tasks that are incomplete: {incomplete_percentage:.2f}%")
    print(f"Percentage of tasks that are overdue: {overdue_percentage:.2f}%")

    # Calculate the number of users
    with open("user.txt", "r") as user_file:
        user_data = user_file.read().split("\n")
        user_data = [u for u in user_data if u != ""]

    total_users = len(user_data)

    print(f"Total number of users: {total_users}")

while True:
    # Presenting the menu to the user and 
    # Making sure that the user input is converted to lower case
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my tasks{}
e - Exit
: '''.format('\n' + 'ds - Display statistics \ngr - Generate Reports' if curr_user == 'admin' else '')).lower()

    # Call on the appropriate function based on the user's selection
    if menu == "r":
        reg_user()
    elif menu == "a":
        add_task()
    elif menu == "va":
        view_all(task_list)
    elif menu == "vm":
        view_mine(logged_in_user=curr_user)
    elif menu == "ds" and curr_user == "admin":
        display_stats()
    elif menu == "gr" and curr_user == "admin":
        generate_reports()
    elif menu == "e":
        print("Goodbye!")
        break
    else:
        print("Invalid option selected.")