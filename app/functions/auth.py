from functools import wraps
from flask import render_template, session
from werkzeug.security import check_password_hash, generate_password_hash


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user' in session:
            return f(*args, **kwargs)
        
        else:
            error="You need to be logged in."
            return render_template('login.html', error=error)
    
    return decorated

 
def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'admin' in session:
            return f(*args, **kwargs)
        
        else:
            error="You need to be logged in."
            return render_template('login.html', error=error)
    
    return decorated



def login(email, password):

    """
        Add user login/sign in logic here

    """
    
    if user:

        if check_password_hash(user.password, password):
            return True, user.id 
        
        error = "Incorrect username/password"
        return render_template('login.html', error=error)

    else:
        print("User: {} doesn't exist".format(email_address))
        error = "Invalid username/password"
        return None, error


def register(name, email, password):

    try:

        """
            Add user registration logic here
        """

        return True
    
    except Exception as e:
        return False