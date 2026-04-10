# To-Do List CLI in Python

An application to manage a to-do list create with a Tkinter UI.  
Tasks are automatically saved to a tasks.json file so your list persists between runs.

## Features

- Add a new task
- Remove a task by its number
- Change the name of an existing task
- Mark task as donne
- Clear the entire list

## Technologies Used

- Python 3
- Standard library modules: `json`.
- External library modules: `tkinter`.
- Structure: `interface` (User interface), `dominio` (business logic), `infrastructure` (JSON persistence)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/PhellypeMiranda/To-Do-List.git
   cd To-Do-List

Project Structure
This project follows a simplified version of Clean Architecture, separating responsibilities into layers:

project/
│
├── models/            # Domain entities
│   ├── task.py
│   └── todo_list.py
│
├── use_cases/         # Application logic
│   ├── add_task.py
│   ├── remove_task.py
│   ├── mark_task.py 
│   ├── modify_task.py
│   └── clear_list.py
│
├── infrastructure/      # Data persistence (JSON)
│   ├── config
│   │   └── config.py
│   ├── data
│   │   └── tasks.json
│   ├── mappers
│   │   └── todo_mappers.py
│   └── repositories
│       └── repository_json.py
│
├── interface/         # UI (Tkinter)
│   └── ui.py
│
├── src/
│   └── images/
│
└── main.py            # Application entry point

What I Learned
Structuring a real application using Clean Architecture
Managing UI state and events with Tkinter
Separating business logic from interface logic
Handling persistence in a maintainable way

Autor
Phellype Miranda

License
MIT License (or choose another — see the LICENSE file if present).
Made with Python