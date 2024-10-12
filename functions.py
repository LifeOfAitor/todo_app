def showresults(todos):
    # only for console use
    for index, item in enumerate(todos):
        print(f"{index + 1}.{item}")

def tareamodify(old, new, todos):
    todos[todos.index(old)] = new
    writefile(todos)

def tareacompletar(todo, todos):
    todos.remove(todo)
    writefile(todos)

def readfile():
    with (open("todos.txt", "r")) as file:
        todos = file.readlines()
    return todos

def writefile(todos):
    with open("todos.txt", "w") as file:
        file.writelines(tarea + "\n" for tarea in todos)

def loadtodos():
    todos_list = readfile()
    todos = [tarea.strip("\n") for tarea in todos_list]
    return todos

# New functions for improvements

def strike_through(text):
    """Mark a todo as completed by striking through"""
    return f"~~{text}~~"

def sort_todos(todos, reverse=False):
    """Sort the todos alphabetically"""
    return sorted(todos, reverse=reverse)

