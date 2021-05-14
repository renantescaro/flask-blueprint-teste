from flask import render_template, Blueprint

bp  = Blueprint(
    'inicial',
    __name__,
    template_folder='templates' )

@bp.route('/')
def inicial():
    return render_template('inicial.html')