# To-Do List CLI in Python

A simple command-line interface (CLI) application to manage a to-do list.  
Tasks are automatically saved to a **tasks.json** file so your list persists between runs.

## Features

- Add a new task
- Remove a task by its number
- Clear the entire list (with confirmation)
- View the numbered list
- Save changes and exit (with confirmation)
- Automatic screen clearing (works on Windows, Linux, and macOS)

## Technologies Used

- Python 3
- Standard library modules: `json`, `os`, `sys`
- Modular structure: `main.py` (menu loop), `funcs.py` (business logic), `storage.py` (JSON persistence)

## Installation & Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
   cd YOUR-REPOSITORY

(Optional) Create and activate a virtual environment:Bashpython -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
Run the program:Bashpython main.py

No external packages are required — it uses only Python's built-in libraries.
How to Use
When you start the program, you will see:
textTO DO:
1 - Example task
...

What do you want to do?
1 - Add item to the list
2 - Remove item from the list
3 - Clear list
4 - Save and exit
Type a number:
Enter the number of the desired option.

Add: type the task when prompted.
Remove: enter the task number and confirm with Y.
Clear: confirm with Y.
Exit: confirm with Y → saves to tasks.json.

Project Structure
text.
├── main.py         # Main menu and program loop
├── funcs.py        # List manipulation functions
├── storage.py      # JSON read/write functions
└── tasks.json      # Auto-generated file (do not commit)
Why this project?
A beginner-friendly project to practice:

Python modularization (splitting code into files)
List manipulation
Basic error handling (ValueError, IndexError)
JSON file persistence
Cross-platform terminal handling
Interactive command-line interface

Contributing
Feel free to open issues or pull requests with improvements, such as:

Mark tasks as completed
Add task priorities or due dates
Search/filter tasks
Use a richer terminal UI (e.g., with Rich or Textual)

License
MIT License (or choose another — see the LICENSE file if present).
Made with Python 🐍
text### Additional recommendations

- Replace `YOUR-USERNAME/YOUR-REPOSITORY` with your actual GitHub repo URL.
- Add this to your `.gitignore` file (create it if it doesn't exist):
tasks.json
pycache/
*.pyc
*.pyo
venv/
.idea/
text- Optional: take a screenshot of the running program, save it as `demo.png` (or similar), upload it to the repo, and add this line under the Features section:

```markdown
<image-card alt="Demo" src="demo.png" ></image-card>