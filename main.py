import json
import sys
import time


# Function to add a task to the tasks.json file
def add_task(task_id, task_name, task_description, task_status, created_at):
    task = {
        "id": task_id,
        "name": task_name,
        "description": task_description,
        "status": task_status,
        "createdAt": created_at,
        "updatedAt": "No updates yet."
    }
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
        
    tasks.append(task)
    
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


# Function to update a task in the tasks.json file
def update_task(task_id, task_name, updated_at):
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("No tasks found to update.")
        return

    for task in tasks:
        if task["id"] == task_id:
            task["name"] = task_name
            task["updatedAt"] = updated_at
            break
    else:
        print(f"No task found with ID: {task_id}")
        return
    
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
        

# Function to mark a task as in-progress or done in the tasks.json file
def mark_task(task_id, task_status, updated_at):
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("No tasks found to update.")
        return

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = task_status
            task["updatedAt"] = updated_at
            break
    else:
        print(f"No task found with ID: {task_id}")
        return
    
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
        

# Function to delete a task from the tasks.json file
def delete_task(task_id):
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("No tasks found to delete.")
        return
    
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print(f"Task with ID: {task_id} deleted successfully.")
            break
        
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
        
        
# Function to get the next ID for the task
def get_next_id():
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
        print("Usage: python main.py <action> <task_name> <task_description>")
        sys.exit(1)
    
    action = sys.argv[1]
    status = sys.argv[2] if len(sys.argv) > 2 else None
    if action == "list": 
        if status == "todo":
            try:
                with open("tasks.json", "r") as file:    
                    tasks = json.load(file)
            except FileNotFoundError:
                print("No tasks found.")
                
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
            try:
                with open("tasks.json", "r") as file:    
                    tasks = json.load(file)
            except FileNotFoundError:
                print("No tasks found.")
                
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
            try:
                with open("tasks.json", "r") as file:    
                    tasks = json.load(file)
            except FileNotFoundError:
                print("No tasks found.")
                
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
            try:
                with open("tasks.json", "r") as file:
                    tasks = json.load(file)
            except FileNotFoundError:
                tasks = []
            
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
        
    task_name = sys.argv[2]
    task_description = " ".join(sys.argv[3:])
    task_status = "todo"
    created_at = time.strftime("%Y-%m-%d %H:%M:%S")
    updated_at = "No updates yet."
    
    if action not in ["add", "list", "update", "delete", "mark-in-progress", "mark-done"]:
        print(f'''
Unknown action: {action}

Valid actions:
- add
- list
- update
- delete
              ''')
    
    if not task_description:
        task_description = "None"
            
    if action == "add":
        task_id = get_next_id()
        add_task(task_id, task_name, task_description, task_status, created_at)
        print("Task added successfully. Task ID: ", task_id)
        
    elif action == "update":
        task_id = int(sys.argv[2])
        task_name = " ".join(sys.argv[3:])
        updated_at = time.strftime("%Y-%m-%d %H:%M:%S")
        update_task(task_id, task_name, updated_at)
        print("Task updated successfully. Task ID: ", task_id)
    
    elif action == "delete":
        delete_task(int(sys.argv[2]))
        sys.exit(1)
        
    elif action == "mark-in-progress":
        task_id = int(sys.argv[2])
        task_status = "in progress"
        updated_at = time.strftime("%Y-%m-%d %H:%M:%S")
        mark_task(task_id, task_status, updated_at)
        print(f"Task with ID: {task_id} marked as in progress")
        
    elif action == "mark-done":
        task_id = int(sys.argv[2])
        task_status = "done"
        updated_at = time.strftime("%Y-%m-%d %H:%M:%S")
        mark_task(task_id, task_status, updated_at)
        print(f"Task with ID: {task_id} marked as done")
        

               

if __name__ == "__main__":
    main()