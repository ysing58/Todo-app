#from Functions import get_todos, Write_todos
import Functions
import time

now=time.strftime("%d-%b %Y %H:%M-%S")
print(f"It is {now}")

prompt = "Enter add , show, edit, complete or exit:"

while True:
    User_action = (input(prompt).strip())

    if User_action.startswith("add"):
        try:
            Task = User_action[4:]

            Task = Task.title()

            Todos= Functions.get_todos()

            Todos.append(Task + '\n' )

            Functions.Write_todos(Todos)

        except ValueError:
            continue

    elif User_action.startswith('show'):
        Todos= Functions.get_todos()
        for index,Todo in enumerate((Todos)):
            Todo = Todo.strip('\n')
            print(f"{index+1}:{Todo}")

    elif User_action.startswith('edit'):
        try:
            item_no= int(User_action[5:])
            New_task = input("Please enter the new task :").capitalize()
            Todos= Functions.get_todos()
            Todos[(item_no-1)]= New_task + '\n'
            print("done")

            Functions.Write_todos(Todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif User_action.startswith('complete'):
        try:
            completed_task = input("Enter the task no which is completed : ")
            Todos.pop(int(completed_task)-1)

            Functions.Write_todos(Todos)

            print("done")
        except IndexError:
            print("Enter a valid command")
            continue
    elif User_action.startswith('exit'):
        break
    else:
        print("You entered an unknown command, please try again.")

print("Bye!")