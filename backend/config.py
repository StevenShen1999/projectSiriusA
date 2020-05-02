class Configuration():
    ENV = "development"

    FLASK_DEBUG = True

    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # FIXME: Change this to get from environment variable upon deployment
    SQLALCHEMY_DATABASE_URI = f"postgresql://postgres:990928ss@localhost/siriusDB"
