import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

#基础配置类
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')or '123456'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ONTEARDOWN = True
    # EAMIL CONFIG
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.163.com'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'huangkun2214@163.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'crazy123'
    MAIL_USE_SSL = True
    MAIL_SUPPRESS_SEND = False
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    # FILE UPLOAD SITE
    MAX_CONTENT_LENGTH = 8*1024*1024
    UPLOADED_PHOTOS_DEST = os.path.join(BASE_DIR,'static/uploads/')

    # SQLALCHEMY_DATABASE_URI='mysql://root:123456@localhost/python2'
    @staticmethod
    def init_app(app):
        pass

    #继承配置
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:1234561@localhost/python1'


# 测试环境配置
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost/python1'


# 生产环境
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost/python1'

config1={
    'DevelopmentConfig':DevelopmentConfig,
    'TestConfig':TestConfig,
    'default': DevelopmentConfig
}



