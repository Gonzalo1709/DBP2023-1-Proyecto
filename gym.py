from datetime import datetime
from sqlalchemy import Boolean, DateTime, Float, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String

engine = create_engine('mysql+mysqlconnector://sergioherrerajave:@localhost/test', echo = True)

Base = declarative_base()   

class User(Base):
    __tablename__ = 'Usuarios'
    
    id = Column(Integer(), primary_key = True)
    name = Column(String(50), unique = True)
    email = Column (String(50), unique = True)
    phone = Column (Integer() )
    age = Column (Integer()  )
    height = Column(Integer())
    weight = Column(Integer()  )
    suplements = Column(Boolean())
    goal = Column(String(50))
    ingreso = Column(DateTime(),default = datetime.now())

    def __str__(self):
        return self.name

class Instructores(Base):
    __tablename__ = 'Instructores'

    id = Column(Integer(), primary_key = True)
    name = Column(String(50) )
    email = Column (String(50), unique = True)
    horario = Column (String(100)  )
    nivel = Column (String(50)  )
    contrato = Column(DateTime(),default = datetime.now())

    def __str__(self):
        return self.name
    
class Ejercicio(Base):
    __tablename__ = 'Ejercicios'

    id = Column(Integer(), primary_key = True)
    ejercicio = Column(String(50) )
    reps = Column(Integer() )
    series = Column(Integer()  )
    calorias = Column(Integer()  )
    implementos = Column(String(50)  )

    def __str__(self):
        return self.ejercicio

class grupo_muscular(Base):
    __tablename__ = 'Grupos Musculares'

    id = Column(Integer(), primary_key = True)
    nombre = Column(String(50)  )
    contenido = Column(String(255) )

    def __str__(self):
        return self.nombre

class Implementos(Base):
    __tablename__ = 'Implementos'

    id = Column(Integer(), primary_key = True)
    nombre = Column(String(50)  )
    pesos = Column(String(50)  )

    def __str__(self):
        return self.nombre
    
class Suplementos(Base):
    __tablename__ = 'Suplementos'
    
    id = Column(Integer(), unique = True)
    nombre = Column(String(50), primary_key = True)
    cantidad = Column(Float()  )
    tipo = Column(String(50)  )
    

Session = sessionmaker(engine)
session = Session()

if __name__ == '__main__':
    
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    # user1 = User(id=1,username='Vasco', email='vasquito@tuutec.com',phone = 999777222, height = 183, weight = 74, suplementos= True)
    # user2 = User(id=2,username='Sergi',email= 'sergito@tuutec.com',phone = 111222333, talla = 171, peso = 51,  suplementos= False)
    # instructor1 = Instructores(id_p = 1, name = 'Gonzalo', email= 'gonzzalo@tugym.com',horario ='Jueves-Sábado' ,nivel = 'Intermedio')
    # instructor2 = Instructores(id_p = 2, name = 'Colfer', email= 'alejjjandro@tugym.com',horario ='Lúnes-Jueves' ,nivel = 'Básico')
    # ejercicio1 = Ejercicio(ejercicio = 'Bench Press',reps = 12,series= 4, calorias = 400, implementos = 'Banca, Barra, Pesos')
    # ejercicio2 = Ejercicio(ejercicio = 'Press Militar',reps = 10,series= 4, calorias = 250, implementos = 'Máquina de Press Militar')
    # grupo_muscular1 = grupo_muscular(nombre = 'Brazos', contenido = 'Bíceps braquial, Braquial, Coracobraquial, Tríceps braquial, Ancóneo')
    # grupo_muscular2 = grupo_muscular(nombre = 'Piernas', contenido = 'Cuádriceps, Isquiotibiales, Abductores, Gemelos, Glúteos')
    # implemento1 = Implementos(nombre = 'Mancuerna', pesos = '1kg - 45kg')
    # implemento2 = Implementos(nombre = 'Cuerda para Triceps', pesos = '0kg')
    # suplemento1 = Suplementos(id=1,nombre = 'Creatina', cantidad = 5, tipo = 'Ácido orgánico nitrogenado')
    # suplemento2 = Suplementos(id=2,nombre = 'Zinc', cantidad = 0.011, tipo = 'Vitamina')

    # session.add(user1)
    # session.add(user2)
    # session.add(instructor1)
    # session.add(instructor2)
    # session.add(ejercicio1)
    # session.add(ejercicio2)
    # session.add(grupo_muscular1)
    # session.add(grupo_muscular2)
    # session.add(implemento1)
    # session.add(implemento2)
    # session.add(suplemento1)
    # session.add(suplemento2)
    # session.commit()