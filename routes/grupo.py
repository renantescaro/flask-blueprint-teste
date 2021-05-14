from flask import render_template, Blueprint

bp  = Blueprint(
    'grupo',
    __name__,
    template_folder='templates' )

@bp.route('/grupo')
def inicial():
    return render_template('grupo.html')