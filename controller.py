import Python_notepad.view as view

def start():
    while True:
        op = view.get_op()
        if op == 1:
            view.view_notes()
        elif op == 2:
            view.view_notes()
        elif op == 3:
            view.edit_notes()
        elif op == 4:
            view.delete_note()
        elif op == 5:
            break
        else:
            print('Недопустимый выбор')