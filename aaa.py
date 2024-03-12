import tkinter as tk
from tkinter import ttk
import psycopg2
from tkinter import messagebox

pupirka = ['orders','products','recipient','robots','sender','orderhistory']
stolbec = 1
def get_table_data(table_name):
    try:
        # Подключение к базе данных PostgreSQL
        connection = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='admin',
            host='127.0.0.1',
            port='5432'
        )
        cursor = connection.cursor()
        if table_combobox.get() == 'orders':
            pupirka = ['id','id_получателя','id_отправителя','id_товара','Статус']
            tree["columns"] = tuple(range(5))
            stolbec = 5
        if table_combobox.get() == 'products':
            pupirka = ['id','Название','Описание','Количество']
            tree["columns"] = tuple(range(4))
            stolbec = 4
        if table_combobox.get() == 'recipient':
            pupirka = ['id','ФИО','Адрес','Телефон']
            tree["columns"] = tuple(range(4))
            stolbec = 4
        if table_combobox.get() == 'robots':
            pupirka = ['id','модель','местоположение','id_заказа']
            tree["columns"] = tuple(range(4))
            stolbec = 4
        if table_combobox.get() == 'sender':
            pupirka = ['id','ФИО','Телефон','Адрес']
            tree["columns"] = tuple(range(4))
            stolbec = 4    
        if table_combobox.get() == 'orderhistory':
            pupirka = ['id','id_заказа','id_робота','Дата','Отзыв']
            tree["columns"] = tuple(range(5))
            stolbec = 5    
        for i in range(stolbec):
            tree.column(i, anchor='center')
            tree.heading(i, text=pupirka[i])
        # Выполнение запроса к базе данных
        cursor.execute(f"SELECT * FROM {table_name}")
        data = cursor.fetchall()

        # Закрытие соединения с базой данных
        connection.close()

        return data

    except psycopg2.Error as error:
        messagebox.showerror("Ошибка", f"Ошибка при доступе к базе данных PostgreSQL: {error}")

def on_table_select(event):
    selected_table = table_combobox.get()
    
    if selected_table:
        # Получение данных для выбранной таблицы
        table_data = get_table_data(selected_table)

        # Очистка данных в Treeview
        for row in tree.get_children():
            tree.delete(row)

        # Вставка данных в таблицу
        for row in table_data:
            tree.insert("", tk.END, values=row)

def sort_by_name():
    selected_table = table_combobox.get()

    if selected_table:
        # Получение данных для выбранной таблицы
        table_data = get_table_data(selected_table)

        # Сортировка данных по столбцу "name"
        sorted_data = sorted(table_data, key=lambda x: x[1])  # Предположим, что "name" находится во втором столбце

        # Очистка данных в Treeview
        for row in tree.get_children():
            tree.delete(row)

        # Вставка отсортированных данных в таблицу
        for row in sorted_data:
            tree.insert("", tk.END, values=row)


def edit_record():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Предупреждение", "Выберите запись для редактирования.")
        return

    selected_values = tree.item(selected_item)["values"]
    edit_window = tk.Toplevel()
    edit_window.title("Редактирование записи")

    entry_fields = []
    for i, value in enumerate(selected_values):
        tk.Label(edit_window, text=f"Значение {i+1}").grid(row=i, column=0)
        entry_field = tk.Entry(edit_window)
        entry_field.grid(row=i, column=1)
        entry_field.insert(tk.END, str(value))
        entry_fields.append(entry_field)

            
    def save_changes():
     
        try:
           
            connection = psycopg2.connect(
                dbname='postgres',
                user='postgres',
                password='admin',
                host='127.0.0.1',
                port='5432'
            )
            
            cursor = connection.cursor()
            
            if table_combobox.get() == 'orders':
                pupirka = ['id','id_получателя','id_отправителя','id_товара','Статус']
            if table_combobox.get() == 'products':
                pupirka = ['id','Название','Описание','Количество']
            if table_combobox.get() == 'recipient':
                pupirka = ['id','ФИО','Адрес','Телефон']                
            if table_combobox.get() == 'robots':
                pupirka = ['id','модель','местоположение','id_заказа']
            if table_combobox.get() == 'sender':
                pupirka = ['id','ФИО','Телефон','Адрес']          
            if table_combobox.get() == 'orderhistory':
                pupirka = ['id','id_заказа','id_робота','Дата','Отзыв']          
            update_query = f"UPDATE {table_combobox.get()} SET "
            for i, value in enumerate(entry_fields):
                update_query +=  pupirka[i]
                update_query +=f"= '{value.get()}'"
                if i != len(entry_fields) - 1:
                    update_query += ", "
            update_query += f" WHERE id = '{selected_values[0]}'"

            cursor.execute(update_query)
            connection.commit()

            connection.close()

            messagebox.showinfo("Успех", "Запись успешно обновлена.")

            edit_window.destroy()

            on_table_select(None)

        except psycopg2.Error as error:
            messagebox.showerror("Ошибка", f"Ошибка при обновлении записи: {error}")

    save_button = tk.Button(edit_window, text="Сохранить", command=save_changes)
    save_button.grid(row=len(selected_values), columnspan=2)

def delete_record():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Предупреждение", "Выберите запись для удаления.")
        return

    selected_id = tree.item(selected_item)["values"][0]

    try:
        connection = psycopg2.connect(
         dbname='postgres',
         user='postgres',
         password='admin',
         host='127.0.0.1',
         port='5432'
        )
        cursor = connection.cursor()

        delete_query = f"DELETE FROM {table_combobox.get()} WHERE id = %s"

        cursor.execute(delete_query, (selected_id,))
        connection.commit()

        messagebox.showinfo("Успех", "Запись успешно удалена.")

        on_table_select(None)

        connection.close()

    except psycopg2.Error as error:
        messagebox.showerror("Ошибка", f"Ошибка при удалении записи: {error}")


def add_record():
    add_window = tk.Toplevel()
    add_window.title("Добавление записи")
    entry_fields = []
    if table_combobox.get() == 'orders':
        stolbec = 5
    if table_combobox.get() == 'products':
        stolbec = 4
    if table_combobox.get() == 'recipient':
        stolbec = 4
    if table_combobox.get() == 'robots':
        stolbec = 4    
    if table_combobox.get() == 'sender':
        stolbec = 4
    if table_combobox.get() == 'orderhistory':
        stolbec = 5
    for i in range(stolbec):  # Предположим, что у нас есть 3 колонки для добавления данных
        tk.Label(add_window, text=f"Значение {i+1}").grid(row=i, column=0)
        entry_field = tk.Entry(add_window)
        entry_field.grid(row=i, column=1)
        entry_fields.append(entry_field)
    def save_record():
        try:
            connection = psycopg2.connect(
              dbname='postgres',
              user='postgres',
              password='admin',
              host='127.0.0.1',
              port='5432'
            )
            cursor = connection.cursor()
            if stolbec == 3:
                insert_query = f"INSERT INTO {table_combobox.get()} VALUES (%s, %s, %s)"
            if stolbec == 4:
                insert_query = f"INSERT INTO {table_combobox.get()} VALUES (%s, %s, %s, %s)"
            if stolbec == 5:
                insert_query = f"INSERT INTO {table_combobox.get()} VALUES (%s, %s, %s, %s, %s)"
            record_values = tuple(entry_field.get() for entry_field in entry_fields)
            cursor.execute(insert_query, record_values)
            connection.commit()
            messagebox.showinfo("Успех", "Запись успешно добавлена.")
            add_window.destroy()
            on_table_select(None)
            connection.close()
        except psycopg2.Error as error:
            messagebox.showerror("Ошибка", f"Ошибка при добавлении записи: {error}")
    save_button = tk.Button(add_window, text="Сохранить", command=save_record)
    save_button.grid(row=len(entry_fields), columnspan=2)


# Функция для выполнения поиска и сортировки
def search_and_sort():
    keyword = search_entry.get()
    selected_table = table_combobox.get()

    if selected_table:
        # Получение данных для выбранной таблицы
        table_data = get_table_data(selected_table)

        # Фильтрация данных по ключевому  слову
        filtered_data = [row for row in table_data if keyword.lower() in str(row).lower()]

        # Сортировка отфильтрованных данных (здесь предполагается сортировка по первому столбцу)
        sorted_data = sorted(filtered_data, key=lambda x: x[0])

        # Очистка данных в Treeview
        for row in tree.get_children():
            tree.delete(row)

        # Вставка отсортированных и отфильтрованных данных в таблицу
        for row in sorted_data:
            tree.insert("", tk.END, values=row)

# Создание окна
display_window = tk.Tk()
display_window.title("Отображение данных из базы данных")

# Добавление текстового поля для ввода данных
search_entry = tk.Entry(display_window)
search_entry.pack()

# Создание выпадающего списка для выбора таблицы
table_combobox = ttk.Combobox(display_window, state="readonly")
table_combobox.pack()
# Добавьте список таблиц в Combobox, например:
table_combobox['values'] = ['orders', 'products', 'recipient', 'robots', 'sender','orderhistory']
# или загрузите список таблиц из базы данных

# Создание Treeview для отображения данных
tree = ttk.Treeview(display_window)

# Определение колонок в таблице
# Замените это на логику, соответствующую вашей схеме таблицы
tree["columns"] = tuple(range(5))  # Здесь 3 - количество колонок
for i in range(5):
    tree.column(i, anchor='center')
    tree.heading(i, text=f"Column {i+1}")

tree.pack()

# Привязка события выбора таблицы к обработчику
table_combobox.bind("<<ComboboxSelected>>", on_table_select)

# Кнопки для редактирования и удаления записи
edit_button = tk.Button(display_window, text="Редактировать запись", command=edit_record)
edit_button.pack()
edit_button.place(x= 300,y=270)

# Создание кнопки для добавления записи
add_button = tk.Button(display_window, text="Добавить запись", command=add_record)
add_button.pack()
add_button.place(x= 440,y=270)

delete_button = tk.Button(display_window, text="Удалить запись", command=delete_record)
delete_button.pack()
delete_button.place(x= 550,y=270)

# Создание кнопки для добавления записи
search_button = tk.Button(display_window, text="Поиск записи", command=search_and_sort)
search_button.pack()
search_button.place(x= 650,y=270)

# Создание кнопки для сортировки по столбцу "name"
sort_button = tk.Button(display_window, text="Сортировать по имени", command=sort_by_name)
sort_button.pack()
sort_button.place(x= 745,y=270)


# Запуск главного цикла окна
display_window.mainloop()



