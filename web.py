import streamlit as st
import Functions

todos = Functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(f"{todo}\n".capitalize())
    Functions.Write_todos(todos)


st.title('My Todo App')
st.subheader('Yadvendra Singh.')
st.write('This is to increase your productivity.')

for index, i in enumerate(todos):
    checkbox = st.checkbox(i, key=i)
    if checkbox:
        todos.pop(index)
        Functions.Write_todos(todos)
        del st.session_state[i]
        st.rerun()

st.text_input(label="Enter the Todo to be added.", placeholder=""
              , on_change=add_todo, key='new_todo')