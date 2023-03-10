from flask import Flask, redirect, render_template
from flask import request
from flask import url_for
import forms

from flask import jsonify
from config import DevelopmentConfig #archivo config con el debug y la conexion a mysql
from flask_wtf.csrf import CSRFProtect
from models import db 
# mapeo de la base de datos
from models import Alumnos # mapeo de la tabla alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig) # generar configuracion de bd ( servidor, usuario, pass, puesto), cadena de conexion
csrf = CSRFProtect()

@app.route("/", methods = ['GET', 'POST'])
def index():
    create_form = forms.UserForm(request.form)
    if request.method == 'POST':
        #objeto que permite pasarselo al db para guardarlo en la base de datos
        alum = Alumnos(nombre = create_form.nombre.data,
                       apellidos = create_form.apellidos.data,
                       correo = create_form.correo.data)
        db.session.add(alum)
        db.session.commit()
    
    return render_template('index.html', form = create_form)

@app.route("/ABCompleto", methods = ['GET', 'POST'])
def ABCompleto():
    create_form = forms.UserForm(request.form)
    alumnos = Alumnos.query.all()
    return render_template('ABCompleto.html', form = create_form, alumnos = alumnos)

@app.route("/modificar", methods = ['GET', 'POST'])
def modificar():
    create_form = forms.UserForm(request.form)

    if request.method == 'GET':
        id =  request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = alum1.id
        create_form.nombre.data = alum1.nombre
        create_form.apellidos.data = alum1.apellidos
        create_form.correo.data = alum1.correo
    
    if request.method == 'POST':
        id = create_form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alum.nombre = create_form.nombre.data 
        alum.apellidos = create_form.apellidos.data
        alum.correo = create_form.correo.data
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for("ABCompleto"))
    
    return render_template("modificar.html", form = create_form)

@app.route("/eliminar", methods = ['GET', 'POST'])
def eliminar():
    create_form = forms.UserForm(request.form)

    if request.method == 'GET':
        id =  request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = alum1.id
        create_form.nombre.data = alum1.nombre
        create_form.apellidos.data = alum1.apellidos
        create_form.correo.data = alum1.correo
    
    if request.method == 'POST':
        id = create_form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alum.nombre = create_form.nombre.data 
        alum.apellidos = create_form.apellidos.data
        alum.correo = create_form.correo.data
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for("ABCompleto"))
    
    return render_template("eliminar.html", form = create_form)


if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app) # inicia la conexion en base de datos
    with app.app_context():
        db.create_all() # analizar archivo config para corroborar que esten mapeado, sino, crea el mapeo
    app.run(port=3000)