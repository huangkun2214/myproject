from app import crate_app
import os
from flask_script import Manager
from flask_migrate import MigrateCommand
from app.model.users import User
from app.model.post import Post
config_name = os.environ.get('FLASK_CONFIG') or 'default'
app=crate_app(config_name=config_name)
manager=Manager(app)
manager.add_command('db',MigrateCommand)
if __name__=='__main__':
    manager.run()
