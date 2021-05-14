from flask import render_template, Blueprint

bp  = Blueprint(
    'usuario',
    __name__,
    template_folder='templates' )

@bp.route('/usuario')
def inicial():
    return render_template('usuario.html')