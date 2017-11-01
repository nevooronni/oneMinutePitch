from app import create_app,db
from flask_script import Manager,Server
from app.models import Categories,User,Role
from flask_migrate import Migrate, MigrateCommand

#app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)#initializes migrate class and passes in app and db instance
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
	return dict(app = app, db = db, Categories = Categories,User = User,Role = Role)

if __name__ == '__main__':
	manager.run()