# Task Tracker CLI

This is an implementation of the [Roadmap.sh Task Tracker CLI project](https://roadmap.sh/projects/task-tracker) .

This script allows users to add, update, list, and manage tasks using command-line arguments. Tasks are stored in a JSON file (`tasks.json`).

## Features

- Add a new task
- Update an existing task
- List all tasks
- Delete a task
- Mark a task as "in progress"
- Mark a task as "done"

## Usage

### Add a Task

To add a new task, use the `add` action followed by the task name and description:

```sh
python main.py add "Task Name" "Task Description"
```

### Update a Task
To update an existing task, use the update action followed by the task ID and the new task name:

```sh
python main.py update <task_id> "New Task Name"
```

### List Tasks
To list all tasks, use the list action:

```sh
python main.py list
```

### Delete a Task
To delete a task, use the delete action followed by the task ID:

```sh
python main.py delete <task_id>
```

### Mark a Task as In Progress
To mark a task as "in progress", use the mark-in-progress action followed by the task ID:

```sh
python main.py mark-in-progress <task_id>
```

### Mark a Task as Done
To mark a task as "done", use the mark-done action followed by the task ID:

```sh
python main.py mark-done <task_id>
```

## Example
Here is an example of how to use the CLI:

1. Add a new task:
  ```sh
  python main.py add "Write Documentation" "Write the README file for the project"
  ```

2. List all tasks:
 ```sh
 python main.py list
 ```

3. Update a task:
 ```sh
 python main.py update 1 "Write Detailed Documentation"
 ```

4. Mark a task as in progress:
 ```sh
 python main.py mark-in-progress 1
 ```

5. Mark a task as done:
 ```sh
 python main.py mark-done 1
 ```

6. Delete a task:
 ```sh
 python main.py delete 1
 ```

## Requirements
Ensure you have Python installed on your system.
