from app import spotify
print("format")

class TopTracks:
    def __init__(self):
        self.names = []
        self.artists = []
        self.albums = []
    def format(self):
        data = spotify.users_top_tracks()
        for i in range(0, 5):
            print(data)
            # self.names.append(data['items'][i]['name'])
            # self.albums.append(data['items'][i]['album']['name'])
            # artists.append(top['items'][0]['name'])



