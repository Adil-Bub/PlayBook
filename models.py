import sqlite3 as sql
from os import path

from flask import redirect
ROOT = path.dirname(path.relpath((__file__)))

def create_entry(name, cont):
    connection = sql.connect(path.join(ROOT, 'data.db'))
    cursor = connection.cursor()
    cursor.execute('insert into posts (name, content) values(?, ?)', (name, cont))
    connection.commit()
    connection.close()

def get_entries():
    connection = sql.connect(path.join(ROOT, 'data.db'))
    cursor = connection.cursor()
    cursor.execute('select * from posts')
    posts = cursor.fetchall()
    return posts

def delete_entry(id):
    connection = sql.connect(path.join(ROOT, 'data.db'))
    cursor = connection.cursor()
    cursor.execute('delete from posts where id = ?', (id,))
    connection.commit()
    connection.close()