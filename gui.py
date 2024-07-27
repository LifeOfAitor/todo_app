import FreeSimpleGUI as sg
import functions
import time

sg.theme("DarkTeal9")
todos = functions.loadtodos()

clock = sg.Text("", key="clock")
input_box = sg.InputText(key="todo", size=(40, 1))
add_button = sg.Button("Añadir")

listbox = sg.Listbox(todos,
                     key="todos",
                     enable_events=True,
                     size=(40, 10))

edit_button = sg.Button("Editar")

complete_button = sg.Button("Completar")
exit_button = sg.Button("Salir")

layout = [[clock],
          [input_box, add_button],
          [listbox],
          [edit_button, complete_button, exit_button]]

window = sg.Window("TODO_APP", layout)

while True:
    event, values = window.read(timeout=1000)
    if event in (sg.WIN_CLOSED, "Salir"):
        break
    # Update the clock
    window["clock"].update(time.strftime("%m-%d  %H:%M"))
    match event:
        case sg.WIN_CLOSED:
            break
        case "Añadir":
            todos.append(values["todo"])
            functions.writefile(todos)
            window["todos"].update(todos)
            window["todo"].update("")
        case "Editar":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]
                functions.tareamodify(todo_to_edit, new_todo, todos)
                window["todos"].update(todos)
            except IndexError:
                sg.popup("Elige una tarea de la lista")
        case "Completar":
            try:
                todo_to_complete = values["todos"][0]
                functions.tareacompletar(todo_to_complete, todos)
                window["todos"].update(todos)
                window["todo"].update("")
            except IndexError:
                sg.popup("Elige una tarea de la lista")
        case "todos":
            # actualizar la lista en la ventana
            window["todo"].update(values["todos"][0])

window.close()
