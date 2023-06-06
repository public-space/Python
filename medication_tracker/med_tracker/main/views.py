from flask import render_template, redirect, url_for, flash, request
from med_tracker.main.forms import MedicationForm
from med_tracker.main.models import Medication
from med_tracker.main.utils import record_dose
from med_tracker.main import bp

# Add other routes like login, register here

from flask_login import login_user, logout_user, login_required
from med_tracker import db
from med_tracker.main.forms import LoginForm, RegistrationForm
from med_tracker.main.models import User

@bp.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    form = MedicationForm()
    if form.validate_on_submit():
        record_dose(form.medication.data, form.dosage.data)
        flash('Dose recorded!', 'success')
        return redirect(url_for('main.dashboard'))
    doses = Medication.query.all() # or use Firebase queries here
    return render_template('dashboard.html', title='Dashboard', form=form, doses=doses)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.dashboard'))
    return render_template('login.html', form=form)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)


#? Each HTML file corresponds to a route in your views.py file and will be rendered when that route is visited.

#? The render_template() function takes the name of an HTML file in the templates folder as an argument. The HTML file in this case is dashboard.html. Flask will look for the templates folder in the app directory, so the location of the file is app/templates/dashboard.html. The render_template() function returns the contents of the HTML file to the browser, which is why the view function is called a view.