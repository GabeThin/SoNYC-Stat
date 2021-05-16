from flask import session, redirect, url_for
import base64
import json
import requests
import sys

artists_url = 'https://api.spotify.com/v1/artists'
search_url = 'https://api.spotify.com/v1/search'
user_url = 'https://api.spotify.com/v1/me'
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


# def get_several_artists(list_of_ids):
#     url = "{}/?ids={ids}".format(GET_ARTIST_ENDPOINT, ids=','.join(list_of_ids))
#     resp = requests.get(url)
#     return resp.json()

def artist_albums(artist_id):
    url = artists_url + '/' + artist_id + '/albums'
    resp = requests.get(url)
    return resp.json()

def artist_top_tracks(artist_id, country='US'):
    url = artists_url + '/' + artist_id + '/top-tracks'
    myparams = {'country': country}
    resp = requests.get(url, params=myparams)
    return resp.json()

def related_artists(artist_id):
    url = artists_url + '/' + artist_id + '/related-artists'
    resp = requests.get(url)
    return resp.json()

def search(name):
    myparams = {'type': ['artist', 'album', 'track']}
    myparams['q'] = name
    resp = requests.get('https://api.spotify.com/v1/search', params=myparams, headers=session['auth_header'])
    return resp.json()


# spotify endpoints
USER_PLAYLISTS_ENDPOINT = "{}/{}".format(user_url, 'playlists')
USER_TOP_ARTISTS_AND_TRACKS_ENDPOINT = "{}/{}".format(
    user_url, 'top')  # /<type>
USER_RECENTLY_PLAYED_ENDPOINT = "{}/{}/{}".format(user_url,
                                                  'player', 'recently-played')
BROWSE_FEATURED_PLAYLISTS = "{}/{}/{}".format('https://api.spotify.com/v1', 'browse',
                                              'featured-playlists')


def get_users_profile():
    url = user_url
    resp = requests.get(url, headers=session['auth_header'])
    return resp.json()


def get_users_playlists(auth_header):
    url = USER_PLAYLISTS_ENDPOINT
    resp = requests.get(url, headers=session['auth_header'])
    return resp.json()


def get_users_top(auth_header, t):
    if t not in ['artists', 'tracks']:
        print('invalid type')
        return None
    url = "{}/{type}".format(USER_TOP_ARTISTS_AND_TRACKS_ENDPOINT, type=t)
    resp = requests.get(url, headers=auth_header)
    print(resp)


def get_users_recently_played(auth_header):
    url = USER_RECENTLY_PLAYED_ENDPOINT
    resp = requests.get(url, headers=auth_header)
    return resp.json()


def get_featured_playlists(auth_header):
    url = BROWSE_FEATURED_PLAYLISTS
    resp = requests.get(url, headers=auth_header)
    return resp.json()

GET_ALBUM_ENDPOINT = "{}/{}".format('https://api.spotify.com/v1', 'albums')  # /<id>

def get_album(album_id):
    url = "{}/{id}".format(GET_ALBUM_ENDPOINT, id=album_id)
    resp = requests.get(url)
    return resp.json()

def get_several_albums(list_of_ids):
    url = "{}/?ids={ids}".format(GET_ALBUM_ENDPOINT, ids=','.join(list_of_ids))
    resp = requests.get(url)
    return resp.json()

def get_albums_tracks(album_id):
    url = "{}/{id}/tracks".format(GET_ALBUM_ENDPOINT, id=album_id)
    resp = requests.get(url)
    return resp.json()

GET_USER_ENDPOINT = '{}/{}'.format('https://api.spotify.com/v1', 'users')

def get_user_profile(user_id):
    url = "{}/{id}".format(GET_USER_ENDPOINT, id=user_id)
    resp = requests.get(url)
    return resp.json()


GET_TRACK_ENDPOINT = "{}/{}".format('https://api.spotify.com/v1', 'tracks')  # /<id>

def get_track(track_id):
    url = "{}/{id}".format(GET_TRACK_ENDPOINT, id=track_id)
    resp = requests.get(url)
    return resp.json()

def get_several_tracks(list_of_ids):
    url = "{}/?ids={ids}".format(GET_TRACK_ENDPOINT, ids=','.join(list_of_ids))
    resp = requests.get(url)
    return resp.json()
