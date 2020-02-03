from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_uploads import UploadSet,IMAGES,configure_uploads,patch_request_class
db=SQLAlchemy()
login_manager=LoginManager()
migrate=Migrate(db=db)
mail=Mail()
photos=UploadSet('photos',IMAGES)
def config_extensions(app):
    db.init_app(app)
    migrate.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    configure_uploads(app, photos)
    patch_request_class(app, size=None)
