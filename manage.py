from app import create_app,db
from flask_migrate import Migrate,MigrateCommand
from app.models import User
from flask_script import Manager,Server



app = create_app ('production')
manager = Manager(app)
manager.add_command('server', Server)

#creating migration instance
 
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

#creating shell context
@manager.shell
def make_shell_context():
    return dict(app=app,db=db,User = User)

if __name__ == '__main__':
    manager.debug = True
    manager.run()
     
    


 
 