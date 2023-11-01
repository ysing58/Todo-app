def get_todos(Filepath='todos.txt'):
    """ Read a text file and return the text of the
     to-do list
    """
    with open(Filepath, 'r') as file:
        Todos_local = file.readlines()
    return Todos_local

def Write_todos(todos_local,Filepath='todos.txt'):
    """ Write items in to-do list to a text file"""
    with open(Filepath, 'w') as file:
        file.writelines(todos_local)

#if __name__ == "__main__":
#    print("in functions")