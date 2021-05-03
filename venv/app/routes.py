from flask import render_template, flash, redirect, url_for, request, jsonify, g
from flask_login import current_user, login_user, logout_user, login_required
# from flask_babel import _, get_locale
from app import app, db, spotify
# from app.forms import LoginForm, RegistrationForm, EditProfileForm, EmptyForm, PostForm, ResetPasswordRequestForm, ResetPasswordForm
from app.forms import LoginForm, EditProfileForm, EmptyForm, PostForm
from app.models import User, Post
from werkzeug.urls import url_parse
from datetime import datetime


@app.route('/auth')
def auth():
    return redirect(spotify.AUTH_URL)


@app.route('/callback/')
def callback():

    auth_token = request.args['code']
    auth_header = spotify.authorize(auth_token)
    session['auth_header'] = auth_header

    return profile()

def valid_token(resp):
    return resp is not None and not 'error' in resp

# @app.before_request
# def before_request():
#     if current_user.is_authenticated:
#         current_user.last_seen = datetime.utcnow()
#         db.session.commit()
#     g.locale = str(get_locale())

# @app.route('/user/<username>')
# @login_required
# def user(username):
#     user = User.query.filter_by(username=username).first_or_404()
#     page = request.args.get('page', 1, type=int)
#     posts = user.posts.order_by(Post.timestamp.desc()).paginate(page, app.config['POSTS_PER_PAGE'], False)
#     next_url = url_for('user', username=user.username, page=posts.next_num) if posts.has_next else None
#     prev_url = url_for('user', username=user.username, page=posts.prev_num) if posts.has_prev else None
#     form = EmptyForm()
#     return render_template('user.html', user=user, posts=posts.items, next_url=next_url, prev_url=prev_url, form=form, theme=theme_choice.url)


@app.route('/index')
def index():
    return render_template('index.html')
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

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.username.data).first()
#         if user is None or not user.check_password(form.password.data):
#             flash('Invalid username or password')
#             return redirect(url_for('login'))
#         login_user(user, remember=form.remember_me.data)
#         next_page = request.args.get('next')
#         if not next_page or url_parse(next_page).netloc != '':
#             next_page = url_for('index')
#         return redirect(next_page)
#     return render_template('login.html', title='Sign In', form=form, theme=theme_choice.url)

# @app.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('index'))

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user = User(username=form.username.data, email=form.email.data)
#         user.set_password(form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         flash('Congratulations, you are now a registered user!')
#         return redirect(url_for('login'))
#     return render_template('register.html', title='Register', form=form)
