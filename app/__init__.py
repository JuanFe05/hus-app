from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import os

login_manager = LoginManager()
db = SQLAlchemy()
#migrate = Migrate()

def create_app():
    app = Flask(__name__)
    # Registro de los Blueprints
    from .inicio import inicio_blueprints
    app.register_blueprint(inicio_blueprints)

    from .autenticacion import autenticacion_blueprints
    app.register_blueprint(autenticacion_blueprints)

    from .administrador import administrador_blueprints
    app.register_blueprint(administrador_blueprints)

    from .usuarios import user_blueprints
    app.register_blueprint(user_blueprints)

    from .citas import appointment_blueprints
    app.register_blueprint(appointment_blueprints)

    from .rol import rol_blueprints
    app.register_blueprint(rol_blueprints)

    from .tipoDocumento import documentType_blueprints
    app.register_blueprint(documentType_blueprints)

    from .tipoCita import appointmentType_blueprints
    app.register_blueprint(appointmentType_blueprints)

    from .Comentario import comment_blueprints
    app.register_blueprint(comment_blueprints)

    app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
    PWD = os.path.abspath(os.curdir)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}/hospital.db'.format(PWD)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    login_manager.login_view = "autenticacion.iniciar_sesion"
    login_manager.init_app(app)
    
    db.init_app(app)
    #migrate.init_app(app, db)
      
    return app

def createSchema() :
    #db.drop_all()
    db.create_all()
    db.session.commit()
    from .autenticacion.models import loadData
    loadData()
    print('Se cargo la bd')