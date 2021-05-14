from flask import Flask
from routes.inicial import bp as bp_inicial
from routes.usuario import bp as bp_usuario
from routes.grupo   import bp as bp_grupo

app = Flask(
    __name__,
    static_url_path='/static',
    static_folder  ='static' )

app.register_blueprint(bp_inicial)
app.register_blueprint(bp_usuario)
app.register_blueprint(bp_grupo)

app.run(host='0.0.0.0', port=80, debug=True)