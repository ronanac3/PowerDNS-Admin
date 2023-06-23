import os

basedir = os.path.abspath(os.path.dirname(__file__))

BIND_ADDRESS = '0.0.0.0'
CAPTCHA_ENABLE = True
CAPTCHA_HEIGHT = 60
CAPTCHA_LENGTH = 6
CAPTCHA_SESSION_KEY = 'captcha_image'
CAPTCHA_WIDTH = 160
HSTS_ENABLED = False
PORT = 9191
SALT = '$2b$12$yLUMTIfl21FKJQpTkRQXCu'
SAML_ASSERTION_ENCRYPTED = True
SAML_ENABLED = False
SECRET_KEY = 'e951e5a1f4b94151b360f47edf596dd2'
SERVER_EXTERNAL_SSL = os.getenv('SERVER_EXTERNAL_SSL', True)

#CSRF Protection
WTF_CSRF_ENABLED = True
WTF_CSRF_CHECK_DEFAULT = True
WTF_CSRF_SECRET_KEY = SECRET_KEY
WTF_CSRF_METHODS = ['POST', 'PUT', 'PATCH', 'DELETE']
WTF_CSRF_FIELD_NAME = 'csrf_token'
WTF_CSRF_TIME_LIMIT = 3600
WTF_CSRF_SSL_STRICT = True


SESSION_COOKIE_SAMESITE = 'Lax'
SESSION_TYPE = 'sqlalchemy'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'pdns.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True
# SQLA_DB_USER = 'pda'
# SQLA_DB_PASSWORD = 'changeme'
# SQLA_DB_HOST = '127.0.0.1'
# SQLA_DB_NAME = 'pda'
# SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}/{}'.format(
#     urllib.parse.quote_plus(SQLA_DB_USER),
#     urllib.parse.quote_plus(SQLA_DB_PASSWORD),
#     SQLA_DB_HOST,
#     SQLA_DB_NAME
# )
