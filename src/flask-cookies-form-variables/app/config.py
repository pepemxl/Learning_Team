# Place to put temporal files
UPLOAD_FOLDER = './TBD'
PROCESED_FOLDER = './TBD'
# Max size of files
MAX_CONTENT_LENGTH = 256 * 1024 * 1024
# Create dummy secrey key so we can use sessions
SECRET_KEY = 'millave'
# Create in-memory database
DATABASE_FILE = 'ejemplo_db.sqlite'
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_FILE
#SQLALCHEMY_DATABASE_URI = DATABASE_MSSQL
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Flask-Security config
SECURITY_URL_PREFIX = "/admin"
SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
SECURITY_PASSWORD_SALT = "ATGUOHAELKiubahiughaerGOJAEGj"

# Flask-Security URLs, overridden because they don't put a / at the end
SECURITY_LOGIN_URL = "/login/"
SECURITY_LOGOUT_URL = "/logout/"
SECURITY_REGISTER_URL = '/register/'
# Configure application to route to the Flask-Admin index view upon login
SECURITY_POST_LOGIN_VIEW = '/admin'
# Configure application to route to the Flask-Admin index view upon logout
SECURITY_POST_LOGOUT_VIEW = '/admin'
# Configure application to route to the Flask-Admin index view upon registering
SECURITY_POST_REGISTER_VIEW = '/admin/create_account'
# Configure application to not send an email upon registration
SECURITY_SEND_REGISTER_EMAIL = False
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Flask-Security features
SECURITY_REGISTERABLE = True
SECURITY_SEND_REGISTER_EMAIL = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Configure a specific Bootswatch theme
FLASK_ADMIN_SWATCH = 'united'


# Flask-Mail SMTP server settings
# MAIL_SERVER = 'smtp.gmail.com'
# MAIL_PORT = 465
# MAIL_USE_SSL = True
# MAIL_USE_TLS = False
# MAIL_USERNAME = 'email@example.com'
# MAIL_PASSWORD = 'password'
# MAIL_DEFAULT_SENDER = '"MyApp" <noreply@example.com>'
