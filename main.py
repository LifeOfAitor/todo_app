def showResults():
    for index, item in enumerate(todos):
        print(f"{index + 1}.{item}")
    return

def tareaModify(tarea):
    if tarea > len(todos):
        print("Ese numero no es correcto")
        return True
    return False

with (open("todos.txt", "r")) as file:
    todos = file.readlines()
todos = [tarea.strip("\n") for tarea in todos]
if todos:
    print("Tareas pendientes:")
    showResults()

while True:
    todo = input("Tareas pendientes: (añadir, editar, completar, salir) ").strip()
    match todo:
        case "añadir":
            tarea = input("Introduce la tarea: ")
            todos.append(tarea)
            showResults()
        case "editar":
            editada = input("tarea editada: ")
            showResults()
            tarea_editar = int(input("Número de la tarea a editar: "))
            if tareaModify(tarea_editar):
                continue
            todos[tarea_editar-1] = editada
            showResults()
        case "completar":
            tarea_completar = int(input("Número de la tarea a completar: "))
            if tareaModify(tarea_completar):
                continue
            todos.pop(tarea_completar-1)
            showResults()
        case "salir":
            # Al salir escribimos de nuevo en el fichero las tareas actualizadas
            with open("todos.txt", "w") as file:
                file.writelines(tarea + "\n" for tarea in todos)
            break
print("Todo hecho")
