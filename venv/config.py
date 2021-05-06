import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMINS = ['your-email@example.com']
    POSTS_PER_PAGE = 25
    os.environ['SPOTIPY_CLIENT_ID'] = 'f5eb6f7b95d84bd48dea9a50c1cca18f'
    os.environ['SPOTIPY_CLIENT_SECRET'] = '37a907df23374db5b9ac602f4847c2b4'
