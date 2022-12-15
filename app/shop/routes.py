from flask import render_template
from flask_mysqldb import MySQL
from . import shop
from app import db

#mi query builder###############################################################

def cur():
    cur = db.connection.cursor()
    return cur

def query(table):
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM "+table)
    result = cur.fetchall()
    return result

def queryLimit(table,position,amount):
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM "+table+" LIMIT "+position+","+amount)
    result = cur.fetchall()
    return result

def queryCount(table,data='*'):
    cur = db.connection.cursor()
    if (data == '*'):
        cur.execute("SELECT COUNT(*) FROM "+table)
        tup = cur.fetchall()
    elif (data != '*' ):
        cur.execute("SELECT COUNT("+data+") FROM "+table)
        tup = cur.fetchall()
    string = str(tup)
    characters ="(,)' "
    for x in range(len(characters)):
            string = string.replace(characters[x],"")

    nstring = "".join(string)
    result = int(nstring)
    return result
################################################################################
@shop.route('/')
def home():
    return render_template('home.html')

@shop.route('/libros')
def libros():
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM libros WHERE tipo = 'Libro' ")
    datos = cur.fetchall()
    return render_template('libros.html',libros = datos)

@shop.route('/comics')
def comics():
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM libros WHERE tipo = 'Comic' ")
    datos = cur.fetchall()
    return render_template('comics.html',libros = datos)

@shop.route('/revistas')
def revistas():
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM libros WHERE tipo = 'Revista' ")
    datos = cur.fetchall()
    return render_template('revistas.html',libros = datos)
