class Config:
    SECRET_KEY = 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://testing123:testing123@localhost:5432/testing123'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URL = "redis://:password@localhost:6379/0"