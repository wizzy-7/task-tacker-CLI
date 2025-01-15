"""
Task Tracker CLI
This script allows users to add, update, and list tasks using command-line arguments.
"""

import json
import sys
import time


# Function to add a task to the tasks.json file
def add_task(task_id, task_name, task_description, task_status, created_at):
    """
    Adds a new task to the tasks.json file.

    Parameters:
    - task_id (int): The unique ID of the task.
    - task_name (str): The name of the task.
    - task_description (str): The description of the task.
    - task_status (str): The status of the task.
    - created_at (str): The creation timestamp of the task.
    """
    
    task = {
        "id": task_id,
        "name": task_name,
        "description": task_description,
        "status": task_status,
        "createdAt": created_at,
        "updatedAt": "No updates yet."
    }
    try:
        # Read the existing tasks from the tasks.json file
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        # If the file does not exist, create an empty list
        tasks = []
    
    # Append the new task to the existing tasks
    tasks.append(task)
    
    # Write the updated tasks to the tasks.json file
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


# Function to update a task in the tasks.json file
def update_task(task_id, task_name, updated_at):
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("No tasks found to update.")
        sys.exit(1)

    # Update the task with the given ID
    for task in tasks:
        if task["id"] == task_id:
            task["name"] = task_name
            task["updatedAt"] = updated_at
            break
    else:
        print(f'''
Please enter a valid task ID
Usage: python main.py update <task_id> <new_task_name>
''')
        sys.exit(1)
    
    # Write the updated task to the tasks.json file
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
        

# Function to mark a task as in-progress or done in the tasks.json file
def mark_task(task_id, task_status, updated_at):
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("No tasks found to update.")
        sys.exit(1)

    # Update the status of the task with the given ID
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = task_status
            task["updatedAt"] = updated_at
            break
    else:
        print(f'''
Please enter a valid task ID
Usage: python main.py mark-done/mark-in-progesss <task_id>
''')
        sys.exit(1)
     
    
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
        

# Function to delete a task from the tasks.json file
def delete_task(task_id):
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("No tasks found to delete.")
        sys.exit(1)
    
    # Remove the task with the given ID
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print(f"Task with ID: {task_id} deleted successfully.")
            break
    else:
                print(f'''
Please enter a valid task ID
Usage: python main.py delete <task_id>
''')
                sys.exit(1)
        
    # Write the updated tasks to the tasks.json file   
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
        
        
# Function to get the next ID for the task
def get_next_id():
    """
    Returns the next available task ID.

    Reads the existing tasks from the tasks.json file and returns the next
    available ID based on the highest existing ID. If the file does not exist
    or is empty, returns 1.
    """
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        if tasks:
            return max(task["id"] for task in tasks) + 1
        else:
            return 1
    except FileNotFoundError:
        return 1


def main():
    if len(sys.argv) < 2:
        print('''Usage: 
- List tasks: python main.py list
- List tasks by status: python main.py list <status>
- Delete a task: python main.py delete <task_id>
- Mark a task as in progress: python main.py mark-in-progress <task_id>
- Mark a task as done: python main.py mark-done <task_id>
''')
        sys.exit(1)
    
    action = sys.argv[1]
    status = sys.argv[2] if len(sys.argv) > 2 else None

    # List tasks based on status
    if action == "list": 
        if status == "todo":
            # Read tasks from the tasks.json file
            try:
                with open("tasks.json", "r") as file:    
                    tasks = json.load(file)
            except FileNotFoundError:
                print("No tasks found.")
                sys.exit(1)
            
            # Print tasks with status "todo"    
            for task in tasks:
                if task["status"] == "todo":
                                print(f'''
Task ID: {task["id"]},
Task Name: {task["name"]},
Task Description: {task["description"]},
Task Status: {task["status"]},
Created: {task["createdAt"]},
Last Updated: {task["updatedAt"]
}
--------------------------------''')
            sys.exit(0)
            
        elif status == "in-progress":
            # Read tasks from the tasks.json file
            try:
                with open("tasks.json", "r") as file:    
                    tasks = json.load(file)
            except FileNotFoundError:
                print("No tasks found.")
                sys.exit(1)
            
            # Print tasks with status "in progress"
            for task in tasks:
                if task["status"] == "in progress":
                                print(f'''
Task ID: {task["id"]},
Task Name: {task["name"]},
Task Description: {task["description"]},
Task Status: {task["status"]},
Created: {task["createdAt"]},
Last Updated: {task["updatedAt"]
}
--------------------------------''')
            sys.exit(0)
            
        elif status == "done":
            # Read tasks from the tasks.json file
            try:
                with open("tasks.json", "r") as file:    
                    tasks = json.load(file)
            except FileNotFoundError:
                print("No tasks found.")
                sys.exit(1)
                
            # Print tasks with status "done"
            for task in tasks:
                if task["status"] == "done":
                                print(f'''
Task ID: {task["id"]},
Task Name: {task["name"]},
Task Description: {task["description"]},
Task Status: {task["status"]},
Created: {task["createdAt"]},
Last Updated: {task["updatedAt"]
}
--------------------------------''')
            sys.exit(0)
        
        else:
            # Read tasks from the tasks.json file
            try:
                with open("tasks.json", "r") as file:
                    tasks = json.load(file)
            except FileNotFoundError:
                print("No tasks found.")
                sys.exit(1)
            
            # Print all tasks
            for task in tasks:
                print(f'''
Task ID: {task["id"]},
Task Name: {task["name"]},
Task Description: {task["description"]},
Task Status: {task["status"]},
Created: {task["createdAt"]},
Last Updated: {task["updatedAt"]
}
--------------------------------''')
            sys.exit(0)
        
    task_name = sys.argv[2] if len(sys.argv) > 2 else None
    task_description = " ".join(sys.argv[3:])
    task_status = "todo"
    created_at = time.strftime("%Y-%m-%d %H:%M:%S")
    updated_at = "No updates yet."
    
    if not task_description:
        task_description = "None"
        
    # Perform the action based on the input       
    if action == "add":
        task_id = get_next_id()
        if task_name is None:
            print('''
Task name is required.
Usage: python main.py add <task_name> (<task_description>)
''')
            sys.exit(1)
        add_task(task_id, task_name, task_description, task_status, created_at)
        print("Task added successfully. Task ID: ", task_id)
        sys.exit(0)
        
    task_id = int(sys.argv[2]) if len(sys.argv) > 2 else None
    if action == "update":
        task_name = " ".join(sys.argv[3:])
        updated_at = time.strftime("%Y-%m-%d %H:%M:%S")
        update_task(task_id, task_name, updated_at)
        print("Task updated successfully. Task ID: ", task_id)

    
    if action == "delete":
        delete_task(task_id)
        sys.exit(0)
        
    if action == "mark-in-progress":
        task_status = "in progress"
        updated_at = time.strftime("%Y-%m-%d %H:%M:%S")
        mark_task(task_id, task_status, updated_at)
        print(f"Task with ID: {task_id} marked as in progress")
        
    if action == "mark-done":
        task_status = "done"
        updated_at = time.strftime("%Y-%m-%d %H:%M:%S")
        mark_task(task_id, task_status, updated_at)
        print(f"Task with ID: {task_id} marked as done")
    
    if action not in ["add", "list", "update", "delete", "mark-in-progress", "mark-done"]:
        print(f'''
Unknown action: {action}

Valid actions:
- add
- list
- update
- delete
- mark-in-progress
- mark-done
        ''')
        sys.exit(1)
        

if __name__ == "__main__":
    main()