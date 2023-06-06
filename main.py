from functions import *
import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [
    [sg.Text('Welcome to Gym Manager')],
    [sg.Button('Add User'), sg.Button('Add Instructor'), sg.Button('Add Exercise'), sg.Button('Add Muscle Group'), sg.Button('Add Implement'), sg.Button('Add Supplement')],
    [sg.Button('View Users'), sg.Button('View Instructors'), sg.Button('View Exercises'), sg.Button('View Muscle Groups'), sg.Button('View Implements'), sg.Button('View Supplements')],
    [sg.Button('View User by ID'), sg.Button('View Instructor by ID'), sg.Button('View Exercise by ID'), sg.Button('View Muscle Group by ID'), sg.Button('View Implement by ID'), sg.Button('View Supplement by ID')],
    [sg.Button('Update User'), sg.Button('Update Instructor'), sg.Button('Update Exercise'), sg.Button('Update Muscle Group'), sg.Button('Update Implement'), sg.Button('Update Supplement')],
    [sg.Button('Delete User'), sg.Button('Delete Instructor'), sg.Button('Delete Exercise'), sg.Button('Delete Muscle Group'), sg.Button('Delete Implement'), sg.Button('Delete Supplement')],
    [sg.Button('Exit')]
]

window = sg.Window('Gym Manager', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Add User':
        try:
            add_user()
        except Exception as e:
            exception = str(e)
            sg.popup(f'Error: {exception}')
    elif event == 'Add Instructor':
        try:
            add_instructor()
        except Exception as e:
            exception = str(e)
            sg.popup(f'Error: {exception}')
    elif event == 'Add Exercise':
        try:
            add_excercise()
        except Exception as e:
            exception = str(e)
            sg.popup(f'Error: {exception}')
    elif event == 'Add Muscle Group':
        try:
            add_muscle_group()
        except Exception as e:
            exception = str(e)
            sg.popup(f'Error: {exception}')
    elif event == 'Add Implement':
        try:
            add_implement()
        except Exception as e:
            exception = str(e)
            sg.popup(f'Error: {exception}')
    elif event == 'Add Supplement':
        try:
            add_supplement()
        except Exception as e:
            exception = str(e)
            sg.popup(f'Error: {exception}')
    elif event == 'View Users':
        try:
            get_users()
        except Exception as e:
            exception = str(e)
            sg.popup(f'Error: {exception}')
    elif event == 'View Instructors':
        try:
            get_instructors()
        except Exception as e:
            exception = str(e)
            sg.popup(f'Error: {exception}')
    elif event == 'View Exercises':
        try:
            get_exercises()
        except Exception as e:
            exception = str(e)
            sg.popup(f'Error: {exception}')
    elif event == 'View Muscle Groups':
        try:
            get_muscle_groups()
        except Exception as e:
            exception = str(e)
            sg.popup(f'Error: {exception}')
    elif event == 'View Implements':
        try:
            get_implements()
        except Exception as e:
            exception = str(e)
            sg.popup(f'Error: {exception}')
    elif event == 'View Supplements':
        try:
            get_supplements()
        except Exception as e:
            exception = str(e)
            sg.popup(f'Error: {exception}')
    elif event == 'View User by ID':
        try:
            get_user_by_id()
        except Exception as e:
            exception = str(e)
            sg.popup(f'Error: {exception}')
    elif event == 'View Instructor by ID':
        try:
            get_instructor_by_id()
        except Exception as e:
            exception = str(e)
            sg.popup(f'Error: {exception}')
    elif event == 'View Exercise by ID':
        try:
            get_exercise_by_id()
        except Exception as e:
            exception = str(e)
            sg.popup(f'Error: {exception}')
    elif event == 'View Muscle Group by ID':
        try:
            get_muscle_group_by_id()
        except Exception as e:
            exception = str(e)
            sg.popup(f'Error: {exception}')
    elif event == 'View Implement by ID':
        try:
            get_implement_by_id()
        except Exception as e:
            exception = str(e)
            sg.popup(f'Error: {exception}')
    elif event == 'View Supplement by ID':
        try:
            get_supplement_by_id()
        except Exception as e:
            exception = str(e)
            sg.popup(f'Error: {exception}')
    elif event == 'Update User':
        try:
            update_user()
        except Exception as e:
            exception = str(e)
            sg.popup(f'Error: {exception}')
    elif event == 'Update Instructor':
        try:
            update_instructor()
        except Exception as e:
            exception = str(e)
            sg.popup(f'Error: {exception}')
    elif event == 'Update Exercise':
        try:
            update_exercise()
        except Exception as e:
            exception = str(e)
            sg.popup(f'Error: {exception}')
    elif event == 'Update Muscle Group':
        try:
            update_muscle_group()
        except Exception as e:
            exception = str(e)
            sg.popup(f'Error: {exception}')
    elif event == 'Update Implement':
        try:
            update_implement()
        except Exception as e:
            exception = str(e)
            sg.popup(f'Error: {exception}')
    elif event == 'Update Supplement':
        try:
            update_supplement()
        except Exception as e:
            exception = str(e)
            sg.popup(f'Error: {exception}')
    elif event == 'Delete User':
        try:
            delete_user()
        except Exception as e:
            exception = str(e)
            sg.popup(f'Error: {exception}')
    elif event == 'Delete Instructor':
        try:
            delete_instructor()
        except Exception as e:
            exception = str(e)
            sg.popup(f'Error: {exception}')
    elif event == 'Delete Exercise':
        try:
            delete_exercise()
        except Exception as e:
            exception = str(e)
            sg.popup(f'Error: {exception}')
    elif event == 'Delete Muscle Group':
        try:
            delete_muscle_group()
        except Exception as e:
            exception = str(e)
            sg.popup(f'Error: {exception}')
    elif event == 'Delete Implement':
        try:
            delete_implement()
        except Exception as e:
            exception = str(e)
            sg.popup(f'Error: {exception}')
    elif event == 'Delete Supplement':
        try:
            delete_supplement()
        except Exception as e:
            exception = str(e)
            sg.popup(f'Error: {exception}')

        

window.close()