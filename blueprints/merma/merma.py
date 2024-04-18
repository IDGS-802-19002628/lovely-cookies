from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from flask_login import login_user, logout_user, login_required, current_user

merma_bp = Blueprint("merma", __name__, template_folder="templates")

@merma_bp.route('/merma')
def merma():
    
    return
