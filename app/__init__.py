import os
from flask import Flask, render_template
# from moment import momentjs
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_debugtoolbar import DebugToolbarExtension
from flask_restful import Api

# set file extension for upload
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])



application = Flask(__name__)

# , instance_path=os.path.join( os.path.dirname(os.path.dirname(__file__)),
#   'app/config'),instance_relative_config=True

# app.jinja_env.globals['momentjs'] = momentjs


application.config.from_pyfile('config/development.cfg')

#
db = SQLAlchemy(application)


# register for migrating
# db = MongoEngine(app)
migrate = Migrate(application, db)


from app.api.user_service import UserService, UserServiceList


# register for debugging
toolbar = DebugToolbarExtension(application)

# register script command
manager = Manager(application)
manager.add_command('db', MigrateCommand)

# wrap to api
api = Api(application)
api.add_resource(UserService, '/users')
api.add_resource(UserServiceList, '/user/<id>')


# app.register_blueprint(api)
