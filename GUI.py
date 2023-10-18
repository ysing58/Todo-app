import Functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter To-Do", key="todo")
add_button = sg.Button("Add")

List_box = sg.Listbox(values=Functions.get_todos(), key='todos', enable_events=True, size=[45, 10])
edit_button= sg.Button("Edit")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button], [List_box, edit_button]],
                   font=('Helvetica', 20))

while True:
    event, value = window.read()
    print(1, event)
    print(2, value)
    match event :
        case "Add":
            todos = Functions.get_todos()
            new_todo = value["todo"].capitalize() + "\n"
            todos.append(new_todo)
            Functions.Write_todos(todos)
            window['todos'].update(values=todos)

        case sg.WIN_CLOSED:
            break
        case "Edit":
            todo_to_edit = value["todos"][0]
            edited_todo = value["todo"].capitalize() + "\n"
            print(todo_to_edit)
            todos = Functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = edited_todo
            Functions.Write_todos(todos)
            window['todos'].update(values=todos)
        case "todos":
            window['todo'].update(value=value['todos'][0])

window.close()