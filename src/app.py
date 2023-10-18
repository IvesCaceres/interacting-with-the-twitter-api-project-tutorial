from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import datetime
import pandas as pd
load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

# con = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id = client_id,
#                                                               client_secret = client_secret))
# artist_id = ''

# response = con.artist_top_tracks(artist_id)                                                  

# for track in response['tracks'][:10]:
#     print('track    : ' + track['name'])
#     print('audio    : ' + track['preview_url'])
#     print('cover art: ' + track['album']['images'][0]['url'])
#     print()

lz_uri = 'spotify:artist:1Yox196W7bzVNZI7RBaPnf'

con = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret))
results = con.artist_top_tracks(lz_uri)
tracks = results['tracks']

for track in tracks:
    
    print('track    : ' + track['name'])
    print('duration_min    : ' + str(datetime.timedelta(milliseconds=track['duration_ms'])))
    print('popularity    : ' + str(track['popularity']))

    # if track['preview_url'] is not None:
    #     print('audio    : ' + track['preview_url'])
    # else:
    #     print('audio    : Preview URL not available')
    # print('cover art: ' + track['album']['images'][0]['url'])
    print()

tracks_df = pd.DataFrame.from_records(tracks)
tracks_df.sort_values(['popularity'],inplace=True)
print(tracks_df.head(3))


