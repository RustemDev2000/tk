from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

try:
    conn = mysql.connector.connect(
        user='root', password='Rustem_09', host='localhost', database='library'
    )
except:
    print('could not connect to database')


def add_auth():
    name_author = author_name.get()
    surname1 = surname.get()
    middle_name1 = middle_name.get()
    country1 = country.get()
    # add to database
    authors = (name_author, surname1, country1, middle_name1)
    if name_author == '' or surname1 == '' or middle_name1 == '' or country1 == '':
        message.set('fill the empty field!!!')
    else:
        cur = conn.cursor()
        cur.execute('INSERT INTO authors(name,surname,country,middle_name) VALUES(%s,%s,%s,%s)', authors)
        conn.commit()
    # add to table tk
    cur = conn.cursor()
    sql = ('SELECT id FROM authors WHERE name=%s AND surname=%s')
    cur.execute(sql, (name_author, surname1,))
    result = cur.fetchall()
    authors = [(result, name_author, surname1, middle_name1, country1)]
    for author in authors:
        tree_aut.insert('', END, values=author)
    author_name.set('')
    surname.set('')
    middle_name.set('')
    country.set('')
    messagebox.showinfo('', 'successfully')


def add_books():
    name_books = books_name.get()
    About1 = About.get()
    Age_limit1 = Age_limit.get()
    Page1 = Page.get()
    # add to database
    books = (name_books, About1, Age_limit1, Page1)
    if name_books == '' or About1 == '' or Age_limit1 == '' or Page1 == '':
        message.set('fill the empty field!!!')
    else:
        cur = conn.cursor()
        cur.execute('INSERT INTO books(name,about,age_limit,page) VALUES(%s,%s,%s,%s)', books)
        conn.commit()
    # add to table tk
    cur = conn.cursor()
    sql = ('SELECT id FROM books WHERE name=%s AND about=%s')
    cur.execute(sql, (name_books, About1,))
    result = cur.fetchall()
    books = [(result, name_books, About1, Age_limit1, Page1)]
    for book in books:
        tree_books.insert('', END, values=book)
    books_name.set('')
    About.set('')
    Age_limit.set('')
    Page.set('')
    messagebox.showinfo('', 'successfully')


def update_auth():
    name_author = author_name.get()
    surname1 = surname.get()
    middle_name1 = middle_name.get()
    country1 = country.get()
    cur = conn.cursor()
    if name_author != values_author[1]:
        sql = 'UPDATE authors SET name=%s where id=%s'
        cur.execute(sql, (name_author, values_author[0]))
        conn.commit()
    if surname1 != values_author[2]:
        sql2 = 'UPDATE authors SET surname=%s where id=%s'
        cur.execute(sql2, (surname1, values_author[0]))
        conn.commit()
    if middle_name1 != values_author[3]:
        sql3 = 'UPDATE authors SET middle_name=%s where id=%s'
        cur.execute(sql3, (middle_name1, values_author[0]))
        conn.commit()
    if country1 != values_author[4]:
        sql4 = 'UPDATE authors SET country=%s where id=%s'
        cur.execute(sql4, (country1, values_author[0]))
        conn.commit()
    else:
        pass

    tree_aut.item(item_author,values=(values_author[1],name_author))
    tree_aut.item(item_author,values=(values_author[2],surname1))
    tree_aut.item(item_author,values=(values_author[3],country1))
    tree_aut.item(item_author,values=(values_author[4],middle_name1))

def update_books():
    pass


# def delete():
def double_click_auth(event):
    global values_author
    global item_author
    item_author = tree_aut.focus()
    values_author = tree_aut.item(item_author, 'values')
    author_name.set(values_author[1])
    surname.set(values_author[2])
    country.set(values_author[3])
    middle_name.set(values_author[4])


def double_click_books(event):
    global values_books
    global item_books
    item_books = tree_books.focus()
    values_books = tree_books.item(item_books, 'values')
    books_name.set(values_books[1])
    About.set(values_books[2])
    Age_limit.set(values_books[3])
    Page.set(values_books[4])


def clear_auth():
    author_name.set('')
    surname.set('')
    middle_name.set('')
    country.set('')


def clear_books():
    books_name.set('')
    About.set('')
    Age_limit.set('')
    Page.set('')


def create_window():
    global window
    global frame1
    global frame2

    # Create window
    window = Tk()
    window.title('Library')
    window.geometry('550x550')

    # Create Notebook
    notebook = ttk.Notebook(window)
    notebook.pack(fill='both', expand=True)
    tab1 = ttk.Frame(notebook)
    tab2 = ttk.Frame(notebook)
    notebook.add(tab1, text='Authors')
    notebook.add(tab2, text='Books')
    frame1 = Frame(tab1)
    frame1.pack(fill='both', expand=True)
    frame2 = Frame(tab2)
    frame2.pack(fill='both', expand=True)


def create_authors():
    global author_name
    global surname
    global middle_name
    global country
    global message

    author_name = StringVar()
    surname = StringVar()
    middle_name = StringVar()
    country = StringVar()
    message = StringVar()

    # Create Label
    Label(frame1, text='name').place(x=15, y=310)
    Label(frame1, text='surname').place(x=15, y=340)
    Label(frame1, text='country').place(x=15, y=370)
    Label(frame1, text='middle_name').place(x=15, y=400)
    Label(frame1, text='', textvariable=message).place(x=250, y=450)

    # Create Entry
    Entry(frame1, textvariable=author_name).place(x=100, y=310)
    Entry(frame1, textvariable=surname).place(x=100, y=340)
    Entry(frame1, textvariable=middle_name).place(x=100, y=370)
    Entry(frame1, textvariable=country).place(x=100, y=400)

    # create table
    global tree_aut
    columns = ('id', 'Name', 'Surname', 'Middle_name', 'Country')
    tree_aut = ttk.Treeview(frame1, columns=columns, show='headings')
    tree_aut.place(x=10, y=70)
    tree_aut.heading('id', text='id')
    tree_aut.heading('Name', text='Name')
    tree_aut.heading('Surname', text='Surname')
    tree_aut.heading('Middle_name', text='Middle name')
    tree_aut.heading('Country', text='Country')
    tree_aut.bind('<Double-Button-1>', double_click_auth)

    # Create srollbar

    # create button
    Button(frame1, foreground='green', text='Add author', command=add_auth).place(x=400, y=320)
    Button(frame1, foreground='green', text='Update author', command=update_auth).place(x=400, y=360)
    Button(frame1, foreground='green', text='Delete author').place(x=400, y=400)
    Button(frame1, foreground='green', text='Cler data', command=clear_auth).place(x=20, y=450)


def create_books():
    # Create Notebook

    global books_name
    global About
    global Page
    global Age_limit
    global message

    books_name = StringVar()
    Age_limit = IntVar()
    Page = IntVar()
    About = StringVar()
    # Create Label
    Label(frame2, text='name').place(x=15, y=310)
    Label(frame2, text='age limit').place(x=15, y=340)
    Label(frame2, text='page').place(x=15, y=370)
    Label(frame2, text='About').place(x=15, y=400)
    Label(frame2, text='', textvariable=message).place(x=250, y=450)

    # Create Entry
    Entry(frame2, textvariable=books_name).place(x=100, y=310)
    Entry(frame2, textvariable=Age_limit).place(x=100, y=340)
    Entry(frame2, textvariable=Page).place(x=100, y=370)
    Entry(frame2, textvariable=About).place(width=200, height=50, x=100, y=400)

    # create table
    global tree_books
    columns = ('id', 'Name', 'About', 'Age limit', 'Page')
    tree_books = ttk.Treeview(frame2, columns=columns, show='headings')
    tree_books.place(x=10, y=70)
    tree_books.heading('id', text='id')
    tree_books.heading('Name', text='Name')
    tree_books.heading('About', text='About')
    tree_books.heading('Age limit', text='Age limit')
    tree_books.heading('Page', text='Page')
    tree_books.bind('<Double-Button-1>', double_click_books)

    # Create srollbar

    # create button
    Button(frame2, foreground='blue', text='Add books', command=add_books).place(x=400, y=320)
    Button(frame2, foreground='blue', text='Update books', command=update_books).place(x=400, y=360)
    Button(frame2, foreground='blue', text='Delete books').place(x=400, y=400)
    Button(frame2, foreground='blue', text='Clear data', command=clear_books).place(x=20, y=450)


create_window()
create_authors()
create_books()
window.mainloop()
