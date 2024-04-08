from flask import Blueprint, render_template, request
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from .proveedor_form import ProvvedorForm

proveedor_bp = Blueprint("proveedor", __name__, template_folder="templates")


@proveedor_bp.route("/proveedor", methods=['GET', 'POST'])

def proveedor():
    form_proveedor = ProvvedorForm(request.form)
    if request.method == "POST" and form_proveedor.validate():
      pass
    return render_template("proveedor.html", form = form_proveedor) 