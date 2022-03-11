from app import create_app,db
from flask_migrate import Migrate
from app.models import User
from flask_migrate import Migrate



app = create_app ('production')

#creating migration instance
migrate = Migrate(db,app)

#creating shell context
@app.shell_context_processor
def make_shell_context():
    return dict(db=db,User = User)
    


 
 