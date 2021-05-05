from flask import Flask, flash, render_template, request, redirect, session


import CRUD
import model
import os

app = Flask(__name__)
app.secret_key = "SHHHHHHHHHHH SEEKRIT"


@app.route('/')
def homepage():
    """Show homepage."""

    return render_template('marketing.html')


@app.route('/show-registration-form', methods=['GET', 'POST'])
def show_registration_form():
    """ Show registration form."""

    return render_template("/register.html")


@app.route('/process-registration-form', methods=['GET', 'POST'])
def process_registration_form():
    """ Process registration form."""

    if "email" not in session:
        
        name = request.form.get('name')
        email = request.form.get('email')

        CRUD.create_user(name, email)
        
    
    flash("We will be reaching out to you soon!")
    return render_template("/register.html")


if __name__ == '__main__':
    app.debug = True
    model.connect_to_db(app)
    app.run(host='0.0.0.0')
