import FreeSimpleGUI as sg
import functions

todos = functions.loadtodos()

label = sg.Text("Tareas: ")
input_box = sg.InputText(key="todo")
add_button = sg.Button("Añadir")

listbox = sg.Listbox(todos,
                     key="todos",
                     enable_events=True,
                     size=(45, 10))

edit_button = sg.Button("Editar")

complete_button = sg.Button("Completar")

layout = [[label, input_box, add_button],
          [listbox, edit_button, complete_button]]

window = sg.Window("TODO_APP", layout)
while True:
    functions.showresults(todos)
    event, values = window.read()
    print(event, values)
    match event:
        case sg.WIN_CLOSED:
            break
        case "Añadir":
            todos.append(values["todo"])
            functions.writefile(todos)
            window["todos"].update(todos)
        case "Editar":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]
            functions.tareamodify(todo_to_edit, new_todo, todos)
            window["todos"].update(todos)
        case "todos":
            window["todo"].update(values["todos"][0])
window.close()
