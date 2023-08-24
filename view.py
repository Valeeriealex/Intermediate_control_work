import uuid
from datetime import datetime
global notes

#класс заметки и его поля: ид, заголовок, тело заметки и дата/время
class Note:
    def _init_(self, id, title, body, date):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

#запись заметки в файл
    def save_notes(notes):
        note = input()
        line = f"{note}\n"
        with open('notes.txt', 'w') as file:
            file.write(line)
        print("Заметка сохранена")

#чтение заметки из файла
    def read_notes():
      with open('notes.txt', 'r') as file:
        for line in file.readlines():
            print(line,end='')

#добавление заметки в файл: заголовок, тело, д/в
#UUID - генерация уникального идентификатора
    def add_note():
        title = input('Введите заголовок заметки: ')
        body = input('Введите текст заметки: ')
        date = datetime.now().strftime('%d.%m.%y %h:%m:%s')
        id = str(uuid.uuid4())
        note = Note(id, title, body, date)
        notes.append(note)
        save_notes(notes)

#редактирование заметки через запрос ид; изменение заголовка, тела, д/в; обновление в списке
    def edit_note():
        id = input('Введите идентификатор заметки для редактирования: ')
        note = next((note for note in notes if note.id == id), None)
        if note:
            print(f'Редактирование заметки: {note.title}')
            title = input('Введите новый заголовок заметки или пропустите: ')
            body = input ('Введите новый текст заметки или пропустите: ')
            date = input ('Введите новые дату и время в формате dd.mm.yyyy hh:ss или пропустите')
            if title:
                note.title = title
            if body:
                note.body = body
            if date:
                note.date = date
            save_notes(notes)
        else:
            print('Заметка не найдена')

#удаление заметки по ид
    def delete_note():
        id = input('Введите идентификатор заметки для удаления: ')
        note = next((note for note in notes if note.id == id,) None)
        if note:
            notes.remove(note)
            save_notes(notes)
        else:
            print('Заметка не найдена')

#главная функция для запуска программы
#бесконечный цикл для вызова меню
#вызов функций в зависимости от выбора
    def get_op():
        notes = read_notes()
        print('Выберете действие')
        op = int(input(
    "1 - Показать список заметок \n 2 - Добавить заметку \n 3 - Редактировать заметку \n 4 - Удалить заметку \n 5 - Выход\n"))
        return op
