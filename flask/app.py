from dataclasses import dataclass
from flask import Flask, jsonify, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import PickleType
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'my_secret_key'

db = SQLAlchemy(app)

@dataclass
class Users(db.Model):
    id: int
    email: str
    password: str

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable = False)
    password = db.Column(db.String(255), nullable = False)
    
    def __repr__(self):
        return f'<User {self.id}>'    

@dataclass
class Trainer(db.Model):
    id: int
    email: str
    password: str
    calificacion: PickleType

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable = False)
    password = db.Column(db.String(255), nullable = False)
    calificacion = db.Column(db.PickleType, nullable = False)
    
    def __repr__(self):
        return f'<Trainer {self.id}>'   

@dataclass
class Sesion(db.Model):
    id: int
    entrenador_id: int
    usuario_id: int
    fecha: datetime
    precio: int

    id = db.Column(db.Integer, primary_key=True)
    entrenador_id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, nullable = False)
    precio = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f'<Sesion {self.id}>'
    

@dataclass
class Solicitudes(db.Model):
    id: int
    usuario_id: int
    entrenador_id: int
    fecha: datetime
    precio: int

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, primary_key=True)
    entrenador_id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, nullable = False)
    precio = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f'<Solicitudes {self.id}>'
    

with app.app_context():
    db.create_all()

@app.route('/')
def main_menu():
    return render_template()

@app.route('/static/<path:filename>')
def serve_static(filename):
    return app.send_static_file(filename)

@app.route('/users', methods=['GET', 'POST', 'PUT', 'DELETE'])
def route_users():
    if request.method == 'GET':
        users = Users.query.all()
        return jsonify([user.serialize() for user in users])
    elif request.method == 'POST':
        users = Users(email=request.form['email'], password=request.form['password'])
        db.session.add(users)
        db.session.commit()
        return 'SUCCESS'
    elif request.method == 'PUT':
        user = Users.query.get(request.form['id'])
        user.email = request.form['email']
        user.password = request.form['password']
        db.session.commit()
        return 'SUCCESS'
    elif request.method == 'DELETE':
        user = Users.query.get(request.form['id'])
        db.session.delete(user)
        db.session.commit()
        return 'SUCCESS'
    
@app.route('/trainer', methods=['GET', 'POST', 'PUT', 'DELETE'])
def route_trainers():
    if request.method == 'GET':
        trainers = Trainer.query.all()
        return jsonify([trainer.serialize() for trainer in trainers])
    elif request.method == 'POST':
        trainer = Trainer(email=request.form['email'], password=request.form['password'])
        db.session.add(trainer)
        db.session.commit()
        return 'SUCCESS'
    elif request.method == 'PUT':
        trainer = Trainer.query.get(request.form['id'])
        trainer.email = request.form['email']
        trainer.password = request.form['password']
        db.session.commit()
        return 'SUCCESS'
    elif request.method == 'DELETE':
        trainer = Trainer.query.get(request.form['id'])
        db.session.delete(trainer)
        db.session.commit()
        return 'SUCCESS'
    
@app.route('/sesion', methods=['GET', 'POST', 'PUT', 'DELETE'])
def route_sesion():
    if request.method == 'GET':
        sesion = Sesion.query.all()
        return jsonify([sesion.serialize() for sesion in sesion])
    elif request.method == 'POST':
        sesion = Sesion(id=request.form['id'], entrenador_id=request.form['entrenador_id'], usuario_id=request.form['usuario_id'], fecha=request.form['fecha'], hora=request.form['hora'], precio=request.form['precio'])
        db.session.add(sesion)
        db.session.commit()
        return 'SUCCESS'
    elif request.method == 'PUT':
        sesion = Sesion.query.get(request.form['id'])
        sesion.entrenador_id = request.form['entrenador_id']
        sesion.usuario_id = request.form['usuario_id']
        sesion.fecha = request.form['fecha']
        sesion.hora = request.form['hora']
        sesion.precio = request.form['precio']
        db.session.commit()
        return 'SUCCESS'
    elif request.method == 'DELETE':
        sesion = Sesion.query.get(request.form['id'])
        db.session.delete(sesion)
        db.session.commit()
        return 'SUCCESS'
    



if __name__ == '__main__':
    app.run(port=5001)
