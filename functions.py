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

def readfile(filename="todos.txt"):
    with (open("todos.txt", "r")) as file:
        todos = file.readlines()
    return todos


def writefile(todos, filename="todos.txt"):
    with open("todos.txt", "w") as file:
        file.writelines(tarea + "\n" for tarea in todos)


def loadtodos():
    todos_list = readfile()
    todos = [tarea.strip("\n") for tarea in todos_list]
    return todos
