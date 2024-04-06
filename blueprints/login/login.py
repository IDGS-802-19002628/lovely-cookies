from flask import Blueprint, render_template, request
from .login_form import loginForm
login_bp = Blueprint("login", __name__, template_folder="templates")


@login_bp.route("/login", methods=['GET', 'POST'])
def auth():
    form_login = loginForm(request.form)
    if request.method == 'POST' and form_login.validate():
        email = form_login.email.data
        password = form_login.password.data
        print(email)
        print(password)
      
    return render_template("login.html", form = form_login)