import FreeSimpleGUI as sg
import functions

# cargamos la lista de tareas primero para trabajar
todos = functions.loadtodos()

label = sg.Text("Tareas: ")
input_box = sg.InputText(key="todo")
add_button = sg.Button("Añadir")

layout = [[label, input_box, add_button]]

window = sg.Window("TODO_APP", layout)
while True:
    functions.showresults(todos)
    event, values = window.read()
    match event:
        case sg.WIN_CLOSED:
            break
        case "Añadir":
            todos.append(values["todo"])
            functions.writefile(todos)
            functions.showresults(todos)
window.close()