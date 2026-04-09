from services.todo_services import Services
from interface.ui import TodoUI

def main():
    services = Services()
    services.load_on_menu()
    app = TodoUI(services)
    app.run()

if __name__ == "__main__":
    main()