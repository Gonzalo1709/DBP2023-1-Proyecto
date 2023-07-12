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


class Sesion(db.Model):
    __tablename__ = 'sesion'
    id = db.Column(db.Integer, primary_key=True)
    entrenador_id = db.Column(db.Integer, ForeignKey("trainer.id"), primary_key=True)
    usuario_id = db.Column(db.Integer, ForeignKey("user.id"), primary_key=True)
    fecha = db.Column(db.DateTime, nullable=False)
    precio = db.Column(db.Integer, nullable=False)

    entrenador = relationship("Trainer")
    usuario = relationship("User")

    def __repr__(self):
        return f'<Sesion {self.id}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'entrenador_id': self.entrenador_id,
            'usuario_id': self.usuario_id,
            'fecha' : self.fecha,
            'precio' : self.precio
        }

with app.app_context():
    db.create_all()


@app.route('/users', methods=['GET', 'POST', 'PUT', 'DELETE'])
def route_users():
    if request.method == 'GET':
        users = User.query.all()
        users_data = [user.to_dict() for user in users]
        return jsonify(users_data)
    elif request.method == 'POST':
        user_form = request.get_json()
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
        trainer = Trainer(email=request.get_json()['email'], password=request.get_json()['password'],calificacion = request.get_json()['calificacion'])
        db.session.add(trainer)
        db.session.commit()
        return 'SUCCESS'
    elif request.method == 'PUT':
        trainer = Trainer.query.get(request.get_json()['id'])
        trainer.email = request.get_json()['email']
        trainer.password = request.get_json()['password']
        db.session.commit()
        return 'SUCCESS'
    elif request.method == 'DELETE':
        trainer = Trainer.query.get(request.get_json()['id'])
        db.session.delete(trainer)
        db.session.commit()
        return 'SUCCESS'


@app.route('/sesions', methods=['GET', 'POST', 'PUT', 'DELETE'])
def route_sesion():
    if request.method == 'GET':
        sesions = User.query.all()
        sesions_data = [sesion.to_dict() for sesion in sesions]
        return jsonify(sesions_data)
    elif request.method == 'POST':
        sesion = Sesion(id=request.get_json()['id'], entrenador_id=request.get_json()['entrenador_id'],
                        usuario_id=request.get_json()['usuario_id'], fecha=request.get_json()['fecha'],
                        precio=request.get_json()['precio'])
        db.session.add(sesion)
        db.session.commit()
        return 'SUCCESS'
    elif request.method == 'PUT':
        sesion = Sesion.query.get(request.get_json()['id'])
        sesion.entrenador_id = request.get_json()['entrenador_id']
        sesion.usuario_id = request.get_json()['usuario_id']
        sesion.fecha = request.get_json()['fecha']
        sesion.precio = request.get_json()['precio']
        db.session.commit()
        return 'SUCCESS'
    elif request.method == 'DELETE':
        sesion = Sesion.query.get(request.get_json()['id'])
        db.session.delete(sesion)
        db.session.commit()
        return 'SUCCESS'
