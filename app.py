from flask import Flask
from config import Config
from models import db
from flask_cors import CORS
from controllers.usuario_controller import usuario_bp
app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(usuario_bp)



@app.before_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)