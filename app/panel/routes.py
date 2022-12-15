from flask import render_template,request,redirect,url_for
from flask_mysqldb import MySQL
from . import panel
from app import db

def com():
    com = db.connection.commit()
    return com

def cur():
    cur = db.connection.cursor()
    return cur

def deleteRow(id,table,field):
    cur().execute('DELETE FROM '+table+' WHERE '+field+' = {0}'.format(id))
    com()
    return print("all is ok")

def query(table):
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM "+table)
    result = cur.fetchall()
    return result

def querySpecific(table,condition):
    cur().execute("SELECT * FROM "+table+" WHERE "+condition);
    result = cur().fetchall()
    return result

@panel.route('/')
def inicio():
    return render_template('panel_home.html')

@panel.route('/libros')
def libros():
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM libros WHERE tipo = 'Libro' ")
    datos = cur.fetchall()
    return render_template('panel_libros.html',libros = datos)

@panel.route('/libros/add',methods=['POST'])
def add_libros():
    if request.method == 'POST':
        id = 0
        nombre = request.form['nombre']
        portada = request.form['portada']
        sinopsis = request.form['sinopsis']
        tipo = "Libro"
        categoria = request.form['categoria']
        precio = request.form['precio']
        autor= request.form['autor']
        cur().execute('INSERT INTO libros (id,nombre,portada,sinopsis,tipo,categoria,precio,autor) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',(id,nombre,portada,sinopsis,tipo,categoria,precio,autor))
        com()
        return redirect(url_for('panel.libros'))

@panel.route('/libros/delete/<id>',methods=['POST','GET'])
def delete_libros(id):
    deleteRow(id,"libros","id")
    return redirect(url_for('panel.libros'))

@panel.route('/libros/edit/<id>', methods=['POST', 'GET'])
def get_libros(id):
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM libros WHERE id = %s",[id])
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('panel_edit.html', li=data[0])

@panel.route('/libros/update/<id>', methods=['POST'])
def update_libros(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        portada = request.form['portada']
        sinopsis = request.form['sinopsis']
        categoria = request.form['categoria']
        precio = request.form['precio']
        autor = request.form['autor']
        cur = db.connection.cursor()
        cur.execute('UPDATE libros SET nombre = %s,portada = %s,sinopsis = %s,categoria = %s,precio = %s,autor = %s WHERE id = %s ', (nombre,portada,sinopsis,categoria,precio,autor,id))
        com()
        return redirect(url_for('panel.libros'))



@panel.route('/comics')
def comics():
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM libros WHERE tipo = 'Comic' ")
    datos = cur.fetchall()
    return render_template('panel_comics.html',libros = datos)

@panel.route('/comics/add',methods=['POST'])
def add_comics():
    if request.method == 'POST':
        id = 0
        nombre = request.form['nombre']
        portada = request.form['portada']
        sinopsis = request.form['sinopsis']
        tipo = "Comic"
        categoria = request.form['categoria']
        precio = request.form['precio']
        autor= request.form['autor']
        cur().execute('INSERT INTO libros (id,nombre,portada,sinopsis,tipo,categoria,precio,autor) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',(id,nombre,portada,sinopsis,tipo,categoria,precio,autor))
        com()
        return redirect(url_for('panel.comics'))



@panel.route('/comics/delete/<id>',methods=['POST','GET'])
def delete_comics(id):
    deleteRow(id,"libros","id")
    return redirect(url_for('panel.comics'))

@panel.route('/revistas')
def revistas():
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM libros WHERE tipo = 'Revista' ")
    datos = cur.fetchall()
    return render_template('panel_revistas.html',libros = datos)

@panel.route('/revistas/add',methods=['POST'])
def add_revistas():
    if request.method == 'POST':
        id = 0
        nombre = request.form['nombre']
        portada = request.form['portada']
        sinopsis = request.form['sinopsis']
        tipo = "Revista"
        categoria = request.form['categoria']
        precio = request.form['precio']
        autor= request.form['autor']
        cur().execute('INSERT INTO libros (id,nombre,portada,sinopsis,tipo,categoria,precio,autor) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',(id,nombre,portada,sinopsis,tipo,categoria,precio,autor))
        com()
        return redirect(url_for('panel.revistas'))

@panel.route('/revistas/delete/<id>',methods=['POST','GET'])
def delete_revistas(id):
    deleteRow(id,"libros","id")
    return redirect(url_for('panel.revistas'))
