#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from dataclasses import dataclass
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, PickleType
from datetime import datetime
from sqlalchemy.orm import relationship
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'my_secret_key'

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<User {self.id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password
        }


class Trainer(db.Model):
    __tablename__ = 'trainer'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    calificacion = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Trainer {self.id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password,
            'calificación' : self.calificacion
        }


class Session(db.Model):
    __tablename__ = 'session'
    id = db.Column(db.Integer, primary_key=True)
    entrenador_id = db.Column(db.Integer, db.ForeignKey("trainer.id"), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    precio = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Session {self.id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'entrenador_id': self.entrenador_id,
            'usuario_id': self.usuario_id,
            'fecha': str(self.fecha),
            'precio': self.precio
        }
    
# Example JSON body for Session:
# [
#     {
#         "id": 1,
#         "entrenador_id": 1,
#         "usuario_id": 1,
#         "fecha": "2021-05-01 10:00:00",
#         "precio": 100
#     },

with app.app_context():
    db.create_all()


@app.route('/users', methods=['GET', 'POST', 'PUT', 'DELETE'])
def route_users():
    if request.method == 'GET':
        users = User.query.all()
        users_data = [user.to_dict() for user in users]
        return jsonify(users_data)
    elif request.method == 'POST':
        user_data = request.get_json()
        for user_form in user_data:
            if User.query.filter_by(email=user_form['email']).first() is not None:
                return jsonify('USEREXISTS')
            user = User(email=user_form['email'], password=user_form['password'])
            db.session.add(user)
        db.session.commit()
        return 'SUCCESS'
    elif request.method == 'PUT':
        user = User.query.get(request.get_json()['id'])
        user.email = request.get_json()['email']
        user.password = request.get_json()['password']
        db.session.commit()
        return 'SUCCESS'
    elif request.method == 'DELETE':
        user = User.query.get(request.get_json()['id'])
        db.session.delete(user)
        db.session.commit()
        return 'SUCCESS'



@app.route('/users/<id>', methods=['GET'])
def route_user(id):
    if request.method == 'GET':
        user = User.query.get(id)
        return jsonify(user)

@app.route('/trainers', methods=['GET', 'POST', 'PUT', 'DELETE'])
def route_trainers():
    if request.method == 'GET':
        trainers = Trainer.query.all()
        trainers_data = [trainer.to_dict() for trainer in trainers]
        return jsonify(trainers_data)
    elif request.method == 'POST':
        trainer_data = request.get_json()
        for trainer_form in trainer_data:
            trainer = Trainer(email=trainer_form['email'], password=trainer_form['password'], calificacion=trainer_form['calificacion'])
            db.session.add(trainer)
        db.session.commit()
        return 'SUCCESS'
    elif request.method == 'PUT':
        trainer_data = request.get_json()
        for trainer_form in trainer_data:
            trainer = Trainer.query.get(trainer_form['id'])
            trainer.email = trainer_form['email']
            trainer.password = trainer_form['password']
            db.session.commit()
        return 'SUCCESS'
    elif request.method == 'DELETE':
        trainer_data = request.get_json()
        for trainer_form in trainer_data:
            trainer = Trainer.query.get(trainer_form['id'])
            db.session.delete(trainer)
        db.session.commit()
        return 'SUCCESS'


@app.route('/sessions', methods=['GET', 'POST', 'PUT', 'DELETE'])
def route_session():
    if request.method == 'GET':
        sessions = Session.query.all()
        sessions_data = [session.to_dict() for session in sessions]
        return jsonify(sessions_data)
    
    elif request.method == 'POST':
        try:
            session_data = request.get_json()
            # get all sessions and create an id by length of sessions
            sessions = Session.query.all()
            current_id = len(sessions) + 1
            for session_form in session_data:
                # convertir fecha a datetime
                session_form['fecha'] = datetime.strptime(session_form['fecha'], '%Y-%m-%d %H:%M:%S')
                session = Session(usuario_id=session_form['usuario_id'], fecha=session_form['fecha'], precio=session_form['precio'], id=current_id, entrenador_id=session_form['entrenador_id'])
                current_id += 1
                db.session.add(session)
            db.session.commit()
            return 'SUCCESS'
        except Exception as e:
            print(e)
            return f"ERROR: {e}"

    elif request.method == 'PUT':
        session_data = request.get_json()
        for session_form in session_data:
            session = Session.query.get(session_form['id'])
            session.entrenador_id = session_form['entrenador_id']
            session.usuario_id = session_form['usuario_id']
            session.precio = session_form['precio']
            db.session.commit()
        return 'SUCCESS'

    elif request.method == 'DELETE':
        session_data = request.get_json()
        for session_form in session_data:
            session = Session.query.get(session_form['id'])
            db.session.delete(session)
        db.session.commit()
        return 'SUCCESS'

@app.route('/sessions/<entrenador_id_in>/<date>', methods=['GET'])
def route_session_by_date(entrenador_id_in, date):
    if request.method == 'GET':
        sessions = Session.query.filter_by(entrenador_id=entrenador_id_in).all()
        sessions_data = [session.to_dict() for session in sessions]
        sessions_data = [session for session in sessions_data if session['fecha'].split(' ')[0] == date]
        return jsonify(sessions_data)


@app.route('/sessions/<entrenador_id_in>', methods=['GET'])
def route_session_by_entrenador(entrenador_id_in):
    if request.method == 'GET':
        sessions = Session.query.filter_by(entrenador_id=entrenador_id_in).all()
        sessions_data = [session.to_dict() for session in sessions]
        return jsonify(sessions_data)