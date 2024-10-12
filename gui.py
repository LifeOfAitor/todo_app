import FreeSimpleGUI as sg
import functions
import time
import os

# Constants for keys to avoid typos and ensure consistency
KEY_TODO_INPUT = "todo"
KEY_TODO_LIST = "todos"
KEY_CLOCK = "clock"
KEY_STATUS = "status"

# Check if the "todos.txt" file exists; if not, create it
if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

# Set the theme for the GUI
sg.theme("DarkTeal9")

# Load the todos from the file using the function in functions.py
todos = functions.loadtodos()

# Define the components of the GUI (clock, input box, buttons, listbox, etc.)
clock = sg.Text("", key=KEY_CLOCK)  # Display the clock
input_box = sg.InputText(key=KEY_TODO_INPUT,
                         size=(40, 1))  # Input field for adding/editing todos
add_button = sg.Button("Añadir")  # Button to add a todo

# Listbox to display the todos, updated dynamically
listbox = sg.Listbox(todos, key=KEY_TODO_LIST, enable_events=True,
                     size=(40, 10))

# Buttons for editing, completing, and exiting the app
edit_button = sg.Button("Editar")
complete_button = sg.Button("Completar")
exit_button = sg.Button("Salir")

# Buttons for sorting the list of todos
sort_asc_button = sg.Button("Ordenar Ascendente")  # Sort ascending
sort_desc_button = sg.Button("Ordenar Descendente")  # Sort descending

# Status bar to display messages and feedback to the user
status_bar = sg.Text("", key=KEY_STATUS, size=(40, 1))

# Arrange the components in the layout of the window
layout = [
    [clock],
    [input_box, add_button],
    [listbox],
    [edit_button, complete_button, exit_button],
    [sort_asc_button, sort_desc_button],
    [status_bar]
]

# Create the window with the defined layout
window = sg.Window("TODO_APP", layout, return_keyboard_events=True)


# Function to update the listbox with the latest todos
def update_todo_list(window, todos):
    window[KEY_TODO_LIST].update(todos)


# Function to clear the input box after an action
def clear_input(window):
    window[KEY_TODO_INPUT].update("")


# Main event loop for the application
while True:
    # Read events and values from the window, update the clock every second
    event, values = window.read(timeout=1000)

    # If the window is closed or the "Salir" button is pressed, break the loop
    if event in (sg.WIN_CLOSED, "Salir"):
        break

    # Update the clock display with the current time
    window[KEY_CLOCK].update(time.strftime("%m-%d  %H:%M"))

    # Check for the event triggered by user interactions
    if event == sg.WIN_CLOSED:
        break
    elif event == "Añadir":
        # Add a new todo if the input is not empty
        todo = values[KEY_TODO_INPUT].strip()
        if todo:
            todos.append(todo)  # Add todo to the list
            functions.writefile(todos)  # Write the updated list to the file
            update_todo_list(window, todos)  # Update the GUI with the new list
            clear_input(window)  # Clear the input box after adding
            window[KEY_STATUS].update(
                "Tarea añadida con éxito")  # Show success message
        else:
            sg.popup(
                "No puedes añadir una tarea vacía")  # Show an error popup if input is empty
    elif event == "Editar":
        # Edit the selected todo if one is selected and the input is not empty
        try:
            todo_to_edit = values[KEY_TODO_LIST][
                0]  # Get the selected todo from the listbox
            new_todo = values[
                KEY_TODO_INPUT].strip()  # Get the new value from the input box
            if new_todo:
                functions.tareamodify(todo_to_edit, new_todo,
                                      todos)  # Modify the selected todo
                update_todo_list(window,
                                 todos)  # Update the listbox with the new list
                window[KEY_STATUS].update(
                    "Tarea editada con éxito")  # Show success message
            else:
                sg.popup(
                    "Por favor, introduce el nuevo texto de la tarea")  # Error if input is empty
        except IndexError:
            sg.popup(
                "Elige una tarea de la lista")  # Error if no todo is selected
    elif event == "Completar":
        # Mark the selected todo as completed (strike-through) and remove it from the list
        try:
            todo_to_complete = values[KEY_TODO_LIST][0]  # Get the selected todo
            completed_todo = functions.strike_through(
                todo_to_complete)  # Apply strike-through
            todos = [completed_todo if todo == todo_to_complete else todo for
                     todo in todos]
            functions.writefile(todos)  # Write the updated list to the file
            update_todo_list(window, todos)  # Update the listbox
            clear_input(window)  # Clear the input box
            window[KEY_STATUS].update(
                "Tarea completada")  # Show success message
        except IndexError:
            sg.popup(
                "Elige una tarea de la lista")  # Error if no todo is selected
    elif event == KEY_TODO_LIST:
        # Update the input box with the selected todo when clicked in the listbox
        window[KEY_TODO_INPUT].update(values[KEY_TODO_LIST][0])
    elif event == "Return:13":  # Trigger "Añadir" on pressing Enter
        if values[KEY_TODO_INPUT].strip():
            todos.append(values[KEY_TODO_INPUT])
            functions.writefile(todos)
            update_todo_list(window, todos)
            clear_input(window)
            window[KEY_STATUS].update("Tarea añadida con éxito")
    elif event == "Ordenar Ascendente":
        # Sort the todos in ascending order
        todos = functions.sort_todos(todos)
        update_todo_list(window,
                         todos)  # Update the listbox with the sorted list
        window[KEY_STATUS].update(
            "Tareas ordenadas ascendentemente")  # Show success message
    elif event == "Ordenar Descendente":
        # Sort the todos in descending order
        todos = functions.sort_todos(todos, reverse=True)
        update_todo_list(window,
                         todos)  # Update the listbox with the sorted list
        window[KEY_STATUS].update(
            "Tareas ordenadas descendentemente")  # Show success message

    # Disable the "Editar" and "Completar" buttons if no task is selected
    if not values[KEY_TODO_LIST]:
        window["Editar"].update(disabled=True)
        window["Completar"].update(disabled=True)
    else:
        window["Editar"].update(disabled=False)
        window["Completar"].update(disabled=False)

# Close the window when the loop ends
window.close()
