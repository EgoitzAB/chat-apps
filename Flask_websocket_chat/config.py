class Config:
    SECRET_KEY = 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@db/mydatabase'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URL = "redis://:password@localhost:6379/0"