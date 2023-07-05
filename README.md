Project Name: Task Manager

Description:

The Task Manager is a command-line application that allows users to manage tasks and track their progress. It provides functionality for creating tasks, assigning them to users, setting due dates, and marking tasks as completed. The application also generates reports to provide an overview of task statistics and user activity.
The Task Manager is designed to improve task management and collaboration within a team or organization. By centralizing task information and providing easy access to task details, it helps streamline project workflows and ensures timely completion of tasks.

Installation:
To install the Task Manager project locally, follow these steps:

Clone the project repository from GitHub: https://github.com/NickWade13/Task-Manager

Navigate to the project directory using the command line.

Ensure that you have Python installed on your system. The Task Manager project requires Python 3.7 or above.

Create a virtual environment for the project using the following command:

python3 -m venv myenv
Activate the virtual environment. The command may vary depending on your operating system:

For Windows:
myenv\Scripts\activate

For macOS/Linux:
source myenv/bin/activate

Usage:
After installing the Task Manager project, follow these instructions to use it:

Open a terminal or command prompt.

Navigate to the project directory.

Activate the virtual environment created during the installation process (if not already activated).

Run the main script using the following command:
python task_manager.py

The application will prompt you to enter your username and password for login. Use the following credentials to access the admin rights:

Username: admin

Password: password

Once logged in, you will have access to various options and commands. Here are the main functionalities:

Add a Task: You can add a new task by selecting the corresponding option and providing the necessary information such as the task title, description, assigned user, and due date.

View All Tasks: This option allows you to view all tasks in the system. It displays detailed information about each task, including the username, task title, description, assigned date, due date, and completion status.

View My Tasks: This option displays all tasks assigned to the currently logged-in user. It provides an overview of the tasks assigned to you, including their details and completion status.

Generate Reports: This option generates two reports: "task_overview.txt" and "user_overview.txt." These reports provide statistics and insights into task management, including the total number of tasks, completed tasks, incompleted tasks, overdue tasks, and user-specific task information.

Follow the on-screen instructions to navigate through the application and perform the desired actions.

Note: Make sure to open the entire project folder in your IDE or command line environment to ensure that the program accesses the required files correctly.

Enjoy using the Task Manager to efficiently manage and track your tasks!
