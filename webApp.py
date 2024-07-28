import streamlit as st
import functions
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

todos = functions.loadtodos()


def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo)
    functions.writefile(todos)
    st.session_state["new_todo"] = ""


st.title("TAREAS PENDIENTES:")

for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        functions.tareacompletar(todo, todos)
        del st.session_state[todo]
        st.rerun()

text_input = st.text_input(label="", placeholder="Escribe una tarea",
                           on_change=add_todo, key="new_todo")