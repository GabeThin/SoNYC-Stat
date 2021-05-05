from flask import render_template, flash, redirect, url_for, request, jsonify, g
from flask_login import current_user, login_user, logout_user, login_required
# from flask_babel import _, get_locale
from app import app, db, spotify
# from app.forms import LoginForm, RegistrationForm, EditProfileForm, EmptyForm, PostForm, ResetPasswordRequestForm, ResetPasswordForm
from app.forms import LoginForm, EditProfileForm, EmptyForm, PostForm
from app.models import User, Post
from werkzeug.urls import url_parse
from datetime import datetime

client_id = 'f5eb6f7b95d84bd48dea9a50c1cca18f'
client_secret = '37a907df23374db5b9ac602f4847c2b4'

@app.route('/callback/')
def callback():

    auth_token = request.args['code']
    auth_header = spotify.authorize(auth_token)
    session['auth_header'] = auth_header

    return profile()

# @app.before_request
# def before_request():
#     if current_user.is_authenticated:
#         current_user.last_seen = datetime.utcnow()
#         db.session.commit()
#     g.locale = str(get_locale())

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():

    return render_template('index.html', username='gabe')
# @app.route('/', methods=['GET', 'POST'])
# @app.route('/index', methods=['GET', 'POST'])
# @login_required
# def index():
#     form = PostForm()
#     if form.validate_on_submit():
#         language = guess_language(form.post.data)
#         if language == 'UNKNOWN' or len(language) > 5:
#             language = ''
#         post = Post(body=form.post.data, author=current_user, language=language)
#         db.session.add(post)
#         db.session.commit()
#         flash('Your post is now live!')
#         return redirect(url_for('index'))
#     page = request.args.get('page', 1, type=int)
#     posts = current_user.followed_posts().paginate(page, app.config['POSTS_PER_PAGE'], False)
#     next_url = url_for('index', page=posts.next_num) if posts.has_next else None
#     prev_url = url_for('index', page=posts.prev_num) if posts.has_prev else None
#     return render_template('index.html', title='Home', form=form, posts=posts.items, next_url=next_url, prev_url=prev_url, theme=theme_choice.url)

@app.route('/login', methods=['GET', 'POST'])
def login():
    auth_url = 'https://accounts.spotify.com/authorize/?'
    scope = 'user-read-private user-read-email playlist-modify-public playlist-modify-private user-read-recently-played user-top-read user-library-read'

    auth = {
        'response_type': 'code',
        'redirect_uri': 'http://localhost:5000',
        'scope': scope,
        'client_id': client_id
    }

    url = auth_url + '&' + 'response_type=' + auth['response_type'] + '&redirect_uri=' + auth['redirect_uri'] + '&scope=' + auth['scope'] + '&client_id=' + auth['client_id']
    return redirect(url)

# @app.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('index'))
