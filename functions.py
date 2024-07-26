def showresults(todos):
    for index, item in enumerate(todos):
        print(f"{index + 1}.{item}")


def tareamodify(tarea, todos):
    if tarea > len(todos):
        print("Ese numero no es correcto")
        return True
    return False


def readfile(filename="todos.txt"):
    with (open("todos.txt", "r")) as file:
        todos = file.readlines()
    return todos


def writefile(todos, filename="todos.txt"):
    with open("todos.txt", "w") as file:
        file.writelines(tarea + "\n" for tarea in todos)
