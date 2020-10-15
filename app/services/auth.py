from flask import (
    Blueprint, request, jsonify, render_template, session, redirect, url_for
)
from app.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
@bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    
    email_address = request.form['email_address']
    password = request.form['password']

    if request.method == 'POST':
        
        email_address = request.form['email_address']
        password = request.form['password']

        """
        ADD POST LOGIN LOGIC HERE

        """


    else:
        error = "Incorrect login details"
        return render_template("login.html", error=error)


@bp.route('/logout', methods=['GET'])
def logout():
    session.pop('user')

    return redirect(url_for('auth.login'))


@bp.route('/update_password', methods=['GET', 'POST'])
def update_password():
    if request.method == 'GET':

        token = request.args.get('token')
        user_id = request.args.get('user_id')

        #Check if token is valid
        # if 

        return render_template('error_page.html', error=error)

        User.update()
    
    elif request.method == 'POST':
        
        """
        ADD PASSWORD RESET LOGIC HERE
        """
        
    return render_template('login.html', message=message)
