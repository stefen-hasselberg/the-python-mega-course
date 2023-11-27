
todos = []

while True:
    user_action = input("Type add or show/display, edit, complete or exit: ")

    user_action = user_action.strip()

    match user_action.strip():
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':
            print("List of todos")

            for idx,todo in  enumerate(todos):
                row = f"{idx + 1}.{todo.title()}"
                print(row)
                
        case 'edit':
            number = input("Number of todo to edit: ")

            idx = int(number) - 1

            update_todo = input("Enter new todo: ")

            todos[idx] = update_todo

        case 'complete':
            
            todo_num = int(input("Enter number of todo to complete"))
            idx = todo_num - 1

            todos.pop(idx)
            
            print(f"todo removed")

        case 'exit':
            print("Exiting...")
            break
        case _:
            print("Option unknow command")

    