from flask import Flask, render_template, request,redirect, url_for, flash 
from flask_mysqldb import MySQL

app = Flask(__name__)

#MySQL connection 
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Damaylis2103'
app.config['MYSQL_DB'] = 'tickets'
mysql = MySQL(app)

#settings
app.secret_key = 'mysecretkey'

#inicio
@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tickets')
    data = cur.fetchall()
    return render_template('index.html', tickets = data)

#crear nota
@app.route('/create_note/<ticket>')
def get_note(ticket):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tickets WHERE ticket = %s', [ticket])
    data = cur.fetchall()
    print(data[0])
    return render_template('create_note.html', ticket = data[0])

    
#Agregar nota
@app.route('/add_note/<ticket>', methods = ['POST'])
def add_note(ticket):
    if request.method == 'POST':
        employeeEnvia = request.form['employeeEnvia']
        employeeResibe = request.form['employeeResibe']
        note = request.form['note']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO tickets (employeeEnvia, employeeResibe, note) VALUES (%s, %s, %s)',(employeeEnvia, employeeResibe, note))
        mysql.connection.commit()
        flash('note added successfully')
        return redirect(url_for('home'))

#visualizar tickets
@app.route('/view/<ticket>')
def view(ticket):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tickets WHERE ticket = %s', [ticket])
    data = cur.fetchall()
    print(data[0])
    return render_template('ticket.html', ticket = data[0])

#editar tickets
@app.route('/edit/<ticket>')
def get_ticket(ticket):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tickets WHERE ticket = %s', [ticket])
    data = cur.fetchall()
    return render_template('edit-tickets.html', ticket = data[0])

    
#actualizar tickets
@app.route('/update/<ticket>', methods = ['POST'])
def update_ticket(ticket):
    if request.method == 'POST':
        ticket = request.form['ticket']
        dateStart = request.form['dateStart']
        subject = request.form['subject']
        status = request.form['status']
        employee = request.form['employee']
        description = request.form['description']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE tickets
            SET ticket = %s,
                dateStart = %s,
                subject = %s,
                status = %s,
                employee = %s,
                description = %s
            WHERE ticket = %s""" , (ticket, dateStart, subject, status, employee, description, ticket))
        mysql.connection.commit()
        flash('Ticket Update successfully')
        return redirect(url_for('home'))

#borrar ticket
@app.route('/delete/<string:ticket>')
def delete(ticket):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM tickets WHERE ticket = {0}'.format(ticket))
    mysql.connection.commit()
    flash('Ticket removed successfully')
    return redirect(url_for('home'))

    
#ruta empleados
@app.route('/employees')
def about():
    return render_template('employees.html')

#crear ticket
@app.route('/create_ticket')
def create_ticket():
    return render_template('create.html')


#agrefar ticket
@app.route('/add_ticket', methods=['POST'])
def add_ticket():
    if request.method == 'POST':
        ticket = request.form['ticket']
        dateStart = request.form['dateStart']
        subject = request.form['subject']
        status = request.form['status']
        employee = request.form['employee']
        description = request.form['description']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO tickets (ticket, dateStart, subject, status, employee, description) VALUES (%s, %s, %s, %s, %s, %s)',(ticket, dateStart, subject, status, employee, description))
        mysql.connection.commit()

        flash('Ticket created successfully')

        return redirect(url_for('create_ticket'))

#realizar reporte
@app.route('/report')
def report():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tickets')
    data = cur.fetchall()
    return render_template('report.html', ticket = data)


@app.route('/add_report', methods=['POST'])
def add_report():
    if request.method == 'POST':
        dateStart = request.form['dateStart']
        dateEnd = request.form['dateEnd']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO tickets (dateStart, dateEnd) VALUES (%s, %s)',(dateStart, dateEnd))
        mysql.connection.commit()

        flash('report created successfully')

        return redirect(url_for('report'))

#datos de empleados
@app.route('/add_employee', methods= ['POST'])
def add_employee():
    if request.method == 'POST':
        employe = request.form['firstName']
        email = request.form['email']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO tickets (email, password) VALUES (%s, %s)',(email, password))
        mysql.connection.commit()
        flash('Employee created successfully')

        return redirect(url_for('add_employee'))


if __name__ =="__main__":
    app.run(debug=True)