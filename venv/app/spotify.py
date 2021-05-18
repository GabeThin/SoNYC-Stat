from flask import session, redirect, url_for
import base64
import json
import requests
import sys

# spotify endpoints
artists_url = 'https://api.spotify.com/v1/artists'
search_url = 'https://api.spotify.com/v1/search'
user_url = 'https://api.spotify.com/v1/me'
album_url = 'https://api.spotify.com/v1/albums'
tracks_url = 'https://api.spotify.com/v1/tracks'
playlist_url = user_url + '/playlists'
top_tracks_url = user_url + '/top/tracks?limit=5'
top_artists_url = user_url + '/top/artists?limit=5'
recents_url = user_url + '/player/recently-played'

client_id = 'f5eb6f7b95d84bd48dea9a50c1cca18f'
client_secret = '37a907df23374db5b9ac602f4847c2b4'


def refresh():
    code = {
        'grant_type': 'refresh_token',
        'refresh_token': session['refresh_token']
    }

    encoded = base64.b64encode((client_id + ':' + client_secret).encode())
    headers = {'Authorization': 'Basic ' + encoded.decode()}

    post_request = requests.post('https://accounts.spotify.com/api/token', data=code, headers=headers)

    response_data = json.loads(post_request.text)

    access_token = response_data['access_token']

    auth_header = {'Authorization': 'Bearer ' + access_token}
    session['auth_header'] = auth_header

def artist(artist_id):
    refresh()
    url = artists_url + '/' + artist_id
    resp = requests.get(url, headers=session['auth_header'])
    return resp.json()

def artist_albums(artist_id):
    refresh()
    url = artists_url + '/' + artist_id + '/albums'
    resp = requests.get(url)
    return resp.json()

def artist_top_tracks(artist_id, country='US'):
    refresh()
    url = artists_url + '/' + artist_id + '/top-tracks'
    myparams = {'country': country}
    resp = requests.get(url, params=myparams)
    return resp.json()

def related_artists(artist_id):
    refresh()
    url = artists_url + '/' + artist_id + '/related-artists'
    resp = requests.get(url)
    return resp.json()

def search(name):
    refresh()
    myparams = {'type': ['artist', 'album', 'track']}
    myparams['q'] = name
    resp = requests.get('https://api.spotify.com/v1/search', params=myparams, headers=session['auth_header'])
    return resp.json()

def users_profile():
    refresh()
    url = user_url
    resp = requests.get(url, headers=session['auth_header'])
    return resp.json()

def users_playlists():
    refresh()
    url = playlist_url
    resp = requests.get(url, headers=session['auth_header'])
    return resp.json()

def users_top_tracks():
    refresh()
    url = top_tracks_url
    resp = requests.get(url, headers=session['auth_header'])
    return resp.json()

def users_top_artists():
    refresh()
    url = top_artists_url
    resp = requests.get(url, headers=session['auth_header'])
    return resp.json()

def users_recently_played():
    refresh()
    url = recents_url
    resp = requests.get(url, headers=session['auth_header'])
    return resp.json()

def album(album_id):
    refresh()
    url = album_url + '/' + album_id
    resp = requests.get(url)
    return resp.json()

def albums_tracks(album_id):
    refresh()
    url = album_url + '/' + album_id + '/tracks'
    resp = requests.get(url)
    return resp.json()

def track(track_id):
    refresh()
    url = tracks_url + '/' + track_id
    resp = requests.get(url)
    return resp.json()

def several_tracks(list_of_ids):
    refresh()
    url = "{}/?ids={ids}".format(tracks_url, ids=','.join(list_of_ids))
    resp = requests.get(url)
    return resp.json()
