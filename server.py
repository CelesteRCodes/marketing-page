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
        

        
        email = request.form.get('email')
        name = request.form.get('name')

        CRUD.create_user(email, name)
    
    return redirect("/")