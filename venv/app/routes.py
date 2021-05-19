from flask import render_template, flash, redirect, url_for, request, jsonify, g, session
from flask_login import current_user, login_user, logout_user, login_required
# from flask_babel import _, get_locale
from app import app, db, spotify
from app.forms import LoginForm, EditProfileForm, EmptyForm, PostForm
from app.format import TopTracks
from werkzeug.urls import url_parse
from datetime import datetime
import base64, json, requests, threading


client_id = 'f5eb6f7b95d84bd48dea9a50c1cca18f'
client_secret = '37a907df23374db5b9ac602f4847c2b4'

redirect_base = 'http://localhost:5000'

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    auth_url = 'https://accounts.spotify.com/authorize/?'
    scope = 'user-read-private user-read-email playlist-modify-public playlist-modify-private user-read-recently-played user-top-read user-library-read'

    auth = {
        'response_type': 'code',
        'redirect_uri': redirect_base + '/callback',
        'scope': scope,
        'client_id': client_id
    }

    url = auth_url + '&' + 'response_type=' + auth['response_type'] + '&redirect_uri=' + auth['redirect_uri'] + '&scope=' + auth['scope'] + '&client_id=' + auth['client_id']

    return redirect(url)

@app.route('/callback')
def callback():
    auth_token = request.args['code']

    code = {
        'grant_type': 'authorization_code',
        'code': str(auth_token),
        'redirect_uri': redirect_base + '/callback'
    }

    encoded = base64.b64encode((client_id + ':' + client_secret).encode())
    headers = {'Authorization': 'Basic ' + encoded.decode()}

    post_request = requests.post('https://accounts.spotify.com/api/token', data=code, headers=headers)

    response_data = json.loads(post_request.text)

    access_token = response_data['access_token']
    session['refresh_token'] = response_data['refresh_token']

    auth_header = {'Authorization': 'Bearer ' + access_token}
    session['auth_header'] = auth_header

    session['logged_in'] = True
    session['username'] = spotify.users_profile()['display_name']

    return redirect(url_for('home'))

@app.route('/home')
def home():
    if not session['logged_in']:
        flash('You are not logged in')
        return redirect(url_for('index'))

    data = TopTracks()
    data.format()

    return render_template('home.html', data=data)

@app.route('/artist/<artist_id>')
def artist(artist_id):
    return None
