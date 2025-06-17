from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Employee
from app import db
from datetime import datetime 

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html')

@main_bp.route('/employees')
def employee_list():
    employees = Employee.query.all()
    return render_template('employees.html', employees=employees)

# Форма добавления нового сотрудника
@main_bp.route('/add-employee')
def add_employee_form():
    return render_template('add_employee.html')

# Сохранение нового сотрудника
@main_bp.route('/save-employee', methods=['POST'])
def save_employee():
    try:
        employee = Employee(
            full_name=request.form['full_name'],
            position=request.form['position'],
            department=request.form['department']
        )
        db.session.add(employee)
        db.session.commit()
        flash('Сотрудник успешно добавлен', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Ошибка: {str(e)}', 'danger')
    
    return redirect(url_for('main.employee_list'))

# Форма редактирования сотрудника
@main_bp.route('/edit/<int:id>')
def edit_employee(id):
    employee = Employee.query.get_or_404(id)
    return render_template('edit_employee.html', employee=employee)

# Обновление данных сотрудника
@main_bp.route('/update-employee/<int:id>', methods=['POST'])
def update_employee(id):
    employee = Employee.query.get_or_404(id)
    
    try:
        # Обновляем основные поля
        employee.full_name = request.form['full_name']
        employee.position = request.form['position']
        employee.department = request.form['department']
        
        
        # Обновляем метку времени
        employee.updated_at = datetime.utcnow()
        
        db.session.commit()
        flash('Данные сотрудника успешно обновлены', 'success')
    except ValueError:
        db.session.rollback()
        flash('Ошибка: некорректный формат данных', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Ошибка при обновлении: {str(e)}', 'danger')
    
    return redirect(url_for('main.employee_list'))

# Удаление сотрудника (заготовка)
@main_bp.route('/delete/<int:id>')
def delete_employee(id):
    try:
        employee = Employee.query.get_or_404(id)
        db.session.delete(employee)
        db.session.commit()
        flash('Сотрудник успешно удален', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Ошибка при удалении: {str(e)}', 'danger')
    
    return redirect(url_for('main.employee_list'))