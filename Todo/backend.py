def get_todos():
    with open('todos.txt','r') as file:
        local_todos = file.readlines()

    return local_todos

def write_todos(todos):
    with open('todos.txt','w') as file:
        file.writelines(todos)


