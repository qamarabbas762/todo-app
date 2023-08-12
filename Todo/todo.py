import backend
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(key='todo')

add_button = sg.Button("Add")

list_box = sg.Listbox(values =backend.get_todos(),
                      key='todos',enable_events=True,
                      size = [45,10])

edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')

exit_button = sg.Button('Exit')

window = sg.Window("My To DO APP",
                   layout=[[label],[input_box,add_button],
                           [list_box,edit_button,complete_button],
                           [exit_button]],font=('Helvetica',20))

while True:
    event,values = window.read()
    print(event)
    print(values)

    if event == 'Add':
        todos = backend.get_todos()
        new_todo = values['todo'] + "\n"
        todos.append(new_todo)
        backend.write_todos(todos)
        window['todos'].update(values=todos)

    elif event == 'Edit':
        try:
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = backend.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            backend.write_todos(todos)
            window['todos'].update(values=todos)

        except IndexError:
            sg.popup("Please Select an item first",font=('Helvetica',20))

    elif event == 'Complete':
        try:
            todo_to_complete = values['todos']
            todos = backend.get_todos()
            todos.remove(todo_to_complete)
            backend.write_todos(todos)
            window['todos'].update(values=todos)
        except IndexError:
            sg.popup('Please select an Item first',font=('Helvetica',20))

    elif event == 'Exit':
        break

    elif sg.WINDOW_CLOSED:
        break

window.close()

