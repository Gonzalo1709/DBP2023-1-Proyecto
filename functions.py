from gym import *

import PySimpleGUI as sg

def usable_ids(tablename):
    last_id = session.query(tablename).order_by(tablename.id.desc()).first()
    if last_id is None:
        return 1
    else:
        return last_id.id + 1

last_ids = {
    'user': usable_ids(User),
    'instructor': usable_ids(Instructores),
    'exercise': usable_ids(Ejercicio),
    'muscle_group': usable_ids(grupo_muscular),
    'implement': usable_ids(Implementos),
    'supplement': usable_ids(Suplementos)
}

def add_instructor():
    layout = [
        [sg.Text('Nombre del instructor: '), sg.InputText()],
        [sg.Text('Email del instructor: '), sg.InputText()],
        [sg.Text('Horario del instructor: '), sg.InputText()],
        [sg.Text('Nivel del instructor: '), sg.InputText()],
        [sg.Button('Ok'), sg.Button('Cancel')]
    ]

    window = sg.Window('Add Instructor', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == 'Ok':
            instructor_name = values[0]
            instructor_email = values[1]
            instructor_horario = values[2]
            instructor_nivel = values[3]

            instructor = Instructores(id = last_ids['instructor'], name = instructor_name, email = instructor_email, horario = instructor_horario, nivel = instructor_nivel)
            last_ids['instructor'] += 1
            session.add(instructor)
            session.commit()
            break

    window.close()

def add_excercise():
    layout = [
        [sg.Text('Nombre del ejercicio: '), sg.InputText()],
        [sg.Text('Repeticiones del ejercicio: '), sg.InputText()],
        [sg.Text('Series del ejercicio: '), sg.InputText()],
        [sg.Text('Calorias del ejercicio: '), sg.InputText()],
        [sg.Text('Implementos del ejercicio: '), sg.InputText()],
        [sg.Button('Ok'), sg.Button('Cancel')]
    ]

    window = sg.Window('Add Exercise', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == 'Ok':
            exercise_name = values[0]
            exercise_reps = values[1]
            exercise_series = values[2]
            exercise_calorias = values[3]
            exercise_implementos = values[4]

            exercise = Ejercicio(id = last_ids['exercise'] ,ejercicio = exercise_name, reps = exercise_reps, series = exercise_series, calorias = exercise_calorias, implementos = exercise_implementos)
            last_ids['exercise'] += 1
            session.add(exercise)
            session.commit()
            break

    window.close()

def add_muscle_group():
    layout = [
        [sg.Text('Nombre del grupo muscular: '), sg.InputText()],
        [sg.Text('Contenido del grupo muscular: '), sg.InputText()],
        [sg.Button('Ok'), sg.Button('Cancel')]
    ]

    window = sg.Window('Add Muscle Group', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == 'Ok':
            muscle_group_name = values[0]
            muscle_group_content = values[1]

            muscle_group = grupo_muscular(id = last_ids['muscle_group'], nombre = muscle_group_name, contenido = muscle_group_content)
            last_ids['muscle_group'] += 1
            session.add(muscle_group)
            session.commit()
            break

    window.close()

def add_implement():
    layout = [
        [sg.Text('Nombre del implemento: '), sg.InputText()],
        [sg.Text('Peso del implemento: '), sg.InputText()],
        [sg.Button('Ok'), sg.Button('Cancel')]
    ]

    window = sg.Window('Add Implement', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == 'Ok':
            implement_name = values[0]
            implement_weight = values[1]

            implement = Implementos(nombre = implement_name, pesos = implement_weight, id = last_ids['implement'])
            last_ids['implement'] += 1
            session.add(implement)
            session.commit()
            break

    window.close()


def add_supplement():
    layout = [
        [sg.Text('Nombre del suplemento: '), sg.InputText()],
        [sg.Text('Cantidad del suplemento: '), sg.InputText()],
        [sg.Text('Tipo del suplemento: '), sg.InputText()],
        [sg.Button('Ok'), sg.Button('Cancel')]
    ]

    window = sg.Window('Add Supplement', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == 'Ok':
            supplement_name = values[0]
            supplement_quantity = values[1]
            supplement_type = values[2]

            supplement = Suplementos(nombre = supplement_name, cantidad = supplement_quantity, tipo = supplement_type, id = last_ids['supplement'])
            last_ids['supplement'] += 1
            session.add(supplement)
            session.commit()
            break

    window.close()

def add_user():
    layout = [
        [sg.Text('Nombre del usuario: '), sg.InputText()],
        [sg.Text('Email del usuario: '), sg.InputText()],
        [sg.Text('Telefono del usuario: '), sg.InputText()],
        [sg.Text('Edad del usuario: '), sg.InputText()],
        [sg.Text('Altura del usuario: '), sg.InputText()],
        [sg.Text('Peso del usuario: '), sg.InputText()],
        [sg.Text('Usa suplementos: '), sg.InputText()],
        [sg.Text('Meta del usuario: '), sg.InputText()],
        [sg.Button('Ok'), sg.Button('Cancel')]
    ]

    window = sg.Window('Add User', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == 'Ok':
            user_name = values[0]
            user_email = values[1]
            user_phone = values[2]
            user_age = values[3]
            user_height = values[4]
            user_weight = values[5]
            boolean_value = values[6].lower() in ['true', '1', 't', 'y', 'yes']
            user_suplements = boolean_value
            user_goal = values[7]

            user = User(name = user_name, email = user_email, phone = user_phone, age = user_age, height = user_height, weight = user_weight,suplements = user_suplements, goal = user_goal, id = last_ids['user'])
            last_ids['user'] += 1
            session.add(user)
            session.commit()
            break

    window.close()

def get_users():
    layout = [
        [sg.Text('Usuarios: ')],
        [sg.Text('ID - Nombre - Email - Telefono - Edad - Altura - Peso - Suplementos - Meta')],
        [sg.Text('')],
    ]

    users = session.query(User).all()
    for user in users:
        layout.append([sg.Text(f'{user.id} - {user.name} - {user.email} - {user.phone} - {user.age} - {user.height} - {user.weight} - {user.suplements} - {user.goal}')])

    layout.append([sg.Button('Ok')])
    window = sg.Window('Usuarios', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Ok':
            break

    window.close()

def get_instructors():
    layout = [
        [sg.Text('Instructores: ')],
        [sg.Text('ID - Nombre - Email - Horario - Nivel')],
        [sg.Text('')],
    ]

    instructors = session.query(Instructores).all()
    for instructor in instructors:
        layout.append([sg.Text(f'{instructor.id} - {instructor.name} - {instructor.email} - {instructor.horario} - {instructor.nivel}')])

    layout.append([sg.Button('Ok')])
    window = sg.Window('Instructores', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Ok':
            break

    window.close()

def get_exercises():
    layout = [
        [sg.Text('Ejercicios: ')],
        [sg.Text('ID - Ejercicio - Repeticiones - Series - Calorias - Implementos')],
        [sg.Text('')],
    ]

    exercises = session.query(Ejercicio).all()
    for exercise in exercises:
        layout.append([sg.Text(f'{exercise.id} - {exercise.ejercicio} - {exercise.reps} - {exercise.series} - {exercise.calorias} - {exercise.implementos}')])

    layout.append([sg.Button('Ok')])
    window = sg.Window('Ejercicios', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Ok':
            break

    window.close()

def get_muscle_groups():
    layout = [
        [sg.Text('Grupos Musculares: ')],
        [sg.Text('ID - Nombre - Contenido')],
        [sg.Text('')],
    ]

    muscle_groups = session.query(grupo_muscular).all()
    for muscle_group in muscle_groups:
        layout.append([sg.Text(f'{muscle_group.id} - {muscle_group.nombre} - {muscle_group.contenido}')])

    layout.append([sg.Button('Ok')])
    window = sg.Window('Grupos Musculares', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Ok':
            break

    window.close()

def get_implements():
    layout = [
        [sg.Text('Implementos: ')],
        [sg.Text('ID - Nombre - Pesos')],
        [sg.Text('')],
    ]

    implements = session.query(Implementos).all()
    for implement in implements:
        layout.append([sg.Text(f'{implement.id} - {implement.nombre} - {implement.pesos}')])

    layout.append([sg.Button('Ok')])
    window = sg.Window('Implementos', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Ok':
            break

    window.close()

def get_supplements():
    layout = [
        [sg.Text('Suplementos: ')],
        [sg.Text('ID - Nombre - Cantidad - Tipo')],
        [sg.Text('')],
    ]

    supplements = session.query(Suplementos).all()
    for supplement in supplements:
        layout.append([sg.Text(f'{supplement.id} - {supplement.nombre} - {supplement.cantidad} - {supplement.tipo}')])

    layout.append([sg.Button('Ok')])
    window = sg.Window('Suplementos', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Ok':
            break

    window.close()

def get_user_by_id():
    id = sg.popup_get_text('Ingrese el ID del usuario: ')
    user = session.query(User).filter_by(id = id).first()
    layout = [
        [sg.Text('Usuario: ')],
        [sg.Text(f'{user.id} - {user.name} - {user.email} - {user.phone} - {user.age} - {user.height} - {user.weight} - {user.suplements} - {user.goal}')],
        [sg.Button('Ok')]
    ]

    window = sg.Window('Usuario', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Ok':
            break

    window.close()

def get_instructor_by_id():
    id = get_id()
    instructor = session.query(Instructores).filter_by(id = id).first()
    layout = [
        [sg.Text('Instructor: ')],
        [sg.Text(f'{instructor.id} - {instructor.name} - {instructor.email} - {instructor.horario} - {instructor.nivel}')],
        [sg.Button('Ok')]
    ]

    window = sg.Window('Instructor', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Ok':
            break

    window.close()

def get_exercise_by_id():
    id = get_id()
    exercise = session.query(Ejercicio).filter_by(id = id).first()
    layout = [
        [sg.Text('Ejercicio: ')],
        [sg.Text(f'{exercise.id} - {exercise.ejercicio} - {exercise.reps} - {exercise.series} - {exercise.calorias} - {exercise.implementos}')],
        [sg.Button('Ok')]
    ]

    window = sg.Window('Ejercicio', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Ok':
            break

    window.close()

def get_muscle_group_by_id():
    id = get_id()
    muscle_group = session.query(grupo_muscular).filter_by(id = id).first()
    layout = [
        [sg.Text('Grupo Muscular: ')],
        [sg.Text(f'{muscle_group.id} - {muscle_group.nombre} - {muscle_group.contenido}')],
        [sg.Button('Ok')]
    ]

    window = sg.Window('Grupo Muscular', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Ok':
            break

    window.close()

def get_implement_by_id():
    id = get_id()
    implement = session.query(Implementos).filter_by(id = id).first()
    layout = [
        [sg.Text('Implemento: ')],
        [sg.Text(f'{implement.id} - {implement.nombre} - {implement.pesos}')],
        [sg.Button('Ok')]
    ]

    window = sg.Window('Implemento', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Ok':
            break

    window.close()

def get_supplement_by_id():
    id = get_id()
    supplement = session.query(Suplementos).filter_by(id = id).first()
    layout = [
        [sg.Text('Suplemento: ')],
        [sg.Text(f'{supplement.id} - {supplement.nombre} - {supplement.cantidad} - {supplement.tipo}')],
        [sg.Button('Ok')]
    ]

    window = sg.Window('Suplemento', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Ok':
            break

    window.close()

def update_user():
    id = get_id()

    user = session.query(User).filter_by(id = id).first()
    layout = [
        [sg.Text('Ingrese los nuevos datos del usuario: ')],
        [sg.Text(f'{user.id} - {user.name} - {user.email} - {user.phone} - {user.age} - {user.height} - {user.weight} - {user.goal}')],
        [sg.Text('Nombre del usuario: '), sg.InputText()],
        [sg.Text('Email del usuario: '), sg.InputText()],
        [sg.Text('Telefono del usuario: '), sg.InputText()],
        [sg.Text('Edad del usuario: '), sg.InputText()],
        [sg.Text('Altura del usuario: '), sg.InputText()],
        [sg.Text('Peso del usuario: '), sg.InputText()],
        [sg.Text('Usa Suplementos: '), sg.InputText()],
        [sg.Text('Meta del usuario: '), sg.InputText()],
        [sg.Button('Ok')]
    ]

    window = sg.Window('Actualizar Usuario', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Ok':
            break
        else:
            user.name = values[0]
            user.email = values[1]
            user.phone = values[2]
            user.age = values[3]
            user.height = values[4]
            user.weight = values[5]
            user.suplements = values[6]
            user.goal = values[7]
            session.commit()
            break

    window.close()

def update_instructor():
    id = get_id()

    instructor = session.query(Instructores).filter_by(id = id).first()
    layout = [
        [sg.Text('Ingrese los nuevos datos del instructor: ')],
        [sg.Text(f'{instructor.id} - {instructor.name} - {instructor.email} - {instructor.horario} - {instructor.nivel}')],
        [sg.Text('Nombre del instructor: '), sg.InputText()],
        [sg.Text('Email del instructor: '), sg.InputText()],
        [sg.Text('Horario del instructor: '), sg.InputText()],
        [sg.Text('Nivel del instructor: '), sg.InputText()],
        [sg.Button('Ok')]
    ]

    window = sg.Window('Actualizar Instructor', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Ok':
            break
        else:
            instructor.name = values[0]
            instructor.email = values[1]
            instructor.horario = values[2]
            instructor.nivel = values[3]
            session.commit()
            break

    window.close()

def update_muscle_group():
    id = get_id()

    muscle_group = session.query(grupo_muscular).filter_by(id = id).first()
    layout = [
        [sg.Text('Ingrese los nuevos datos del grupo muscular: ')],
        [sg.Text(f'{muscle_group.id} - {muscle_group.nombre} - {muscle_group.contenido}')],
        [sg.Text('Nombre del grupo muscular: '), sg.InputText()],
        [sg.Text('Contenido del grupo muscular: '), sg.InputText()],
        [sg.Button('Ok')]
    ]

    window = sg.Window('Actualizar Grupo Muscular', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Ok':
            break
        else:
            muscle_group.nombre = values[0]
            muscle_group.contenido = values[1]
            session.commit()
            break

    window.close()

def update_exercise():
    id = get_id()

    exercise = session.query(Ejercicio).filter_by(id = id).first()
    layout = [
        [sg.Text('Ingrese los nuevos datos del ejercicio: ')],
        [sg.Text(f'{exercise.id} - {exercise.ejercicio} - {exercise.reps} - {exercise.series} - {exercise.calorias} - {exercise.implementos}')],
        [sg.Text('Nombre del ejercicio: '), sg.InputText()],
        [sg.Text('Repeticiones del ejercicio: '), sg.InputText()],
        [sg.Text('Series del ejercicio: '), sg.InputText()],
        [sg.Text('Calorias del ejercicio: '), sg.InputText()],
        [sg.Text('Implementos del ejercicio: '), sg.InputText()],
        [sg.Button('Ok')]
    ]

    window = sg.Window('Actualizar Ejercicio', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Ok':
            break
        else:
            exercise.ejercicio = values[0]
            exercise.reps = values[1]
            exercise.series = values[2]
            exercise.calorias = values[3]
            exercise.implementos = values[4]
            session.commit()
            break

    window.close()

def update_implement():
    id = get_id()

    implement = session.query(Implementos).filter_by(id = id).first()
    layout = [
        [sg.Text('Ingrese los nuevos datos del implemento: ')],
        [sg.Text(f'{implement.id} - {implement.nombre} - {implement.pesos}')],
        [sg.Text('Nombre del implemento: '), sg.InputText()],
        [sg.Text('Peso del implemento: '), sg.InputText()],
        [sg.Button('Ok')]
    ]

    window = sg.Window('Actualizar Implemento', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Ok':
            break
        else:
            implement.nombre = values[0]
            implement.pesos = values[1]
            session.commit()
            break

    window.close()

def update_supplement():
    id = get_id()

    supplement = session.query(Suplementos).filter_by(id = id).first()
    layout = [
        [sg.Text('Ingrese los nuevos datos del suplemento: ')],
        [sg.Text(f'{supplement.id} - {supplement.nombre} - {supplement.calorias}')],
        [sg.Text('Nombre del suplemento: '), sg.InputText()],
        [sg.Text('Calorias del suplemento: '), sg.InputText()],
        [sg.Button('Ok')]
    ]

    window = sg.Window('Actualizar Suplemento', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Ok':
            break
        else:
            supplement.nombre = values[0]
            supplement.calorias = values[1]
            session.commit()
            break

    window.close()

def delete_user():
    layout = [
        [sg.Text('Ingrese el ID del usuario a eliminar: ')],
        [sg.InputText()],
        [sg.Button('Ok')]
    ]

    window = sg.Window('Eliminar Usuario', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Ok':
            if values[0]:
                user = session.query(User).filter_by(id = values[0]).first()
                session.delete(user)
                session.commit()
                break
            else:
                break


    window.close()

def delete_instructor():
    layout = [
        [sg.Text('Ingrese el ID del instructor a eliminar: ')],
        [sg.InputText()],
        [sg.Button('Ok')]
    ]

    window = sg.Window('Eliminar Instructor', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Ok':
            if values[0]:
                instructor = session.query(Instructores).filter_by(id = values[0]).first()
                session.delete(instructor)
                session.commit()
                break
            else:
                break

    window.close()

def delete_exercise():
    layout = [
        [sg.Text('Ingrese el ID del ejercicio a eliminar: ')],
        [sg.InputText()],
        [sg.Button('Ok')]
    ]

    window = sg.Window('Eliminar Ejercicio', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Ok':
            if values[0]:
                exercise = session.query(Ejercicio).filter_by(id = values[0]).first()
                session.delete(exercise)
                session.commit()
                break
            else:
                break

    window.close()

def delete_implement():
    layout = [
        [sg.Text('Ingrese el ID del implemento a eliminar: ')],
        [sg.InputText()],
        [sg.Button('Ok')]
    ]

    window = sg.Window('Eliminar Implemento', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Ok':
            if values[0]:
                implement = session.query(Implementos).filter_by(id = values[0]).first()
                session.delete(implement)
                session.commit()
                break
            else:
                break

    window.close()

def delete_supplement():
    layout = [
        [sg.Text('Ingrese el ID del suplemento a eliminar: ')],
        [sg.InputText()],
        [sg.Button('Ok')]
    ]

    window = sg.Window('Eliminar Suplemento', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Ok':
            if values[0]:
                supplement = session.query(Suplementos).filter_by(id = values[0]).first()
                session.delete(supplement)
                session.commit()
                break
            else:
                break

    window.close()

def delete_muscle_group():
    layout = [
        [sg.Text('Ingrese el ID del grupo muscular a eliminar: ')],
        [sg.InputText()],
        [sg.Button('Ok')]
    ]

    window = sg.Window('Eliminar Grupo Muscular', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Ok':
            if values[0]:
                muscle_group = session.query(grupo_muscular).filter_by(id = values[0]).first()
                session.delete(muscle_group)
                session.commit()
                break
            else:
                break

    window.close()

def get_id():
    id = sg.popup_get_text('Ingrese el id del usuario: ')
    return id