import functions
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

todos_list = functions.readfile()
todos = [tarea.strip("\n") for tarea in todos_list]
if todos:
    print("Tareas pendientes:")
    functions.showresults(todos)

while True:
    todo = input("Tareas pendientes: (añadir, editar, completar, salir) ").strip()
    match todo:
        case "añadir":
            tarea = input("Introduce la tarea: ")
            todos.append(tarea)
            functions.showresults(todos)
        case "editar":
            tarea_editar = int(input("Número de la tarea a editar: "))
            editada = input("tarea editada: ")
            if functions.tareamodify(tarea_editar, todos):
                continue
            todos[tarea_editar-1] = editada
            functions.showresults(todos)
        case "completar":
            tarea_completar = int(input("Número de la tarea a completar: "))
            if functions.tareamodify(tarea_completar, todos):
                continue
            todos.pop(tarea_completar-1)
            functions.showresults(todos)
        case "salir":
            # Al salir escribimos de nuevo en el fichero las tareas actualizadas
            functions.writefile(todos)
            break
print("Todo hecho")
