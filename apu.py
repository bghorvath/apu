# %% 

import os
import json

import pandas as pd
import numpy as np

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# %%

def get_apu_ep_list(apu_id, spotify_api_keys):
    apu_id = apu_id
    client_id, client_secret = spotify_api_keys
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id = client_id, client_secret = client_secret))

    ep_list = []

    results = spotify.show_episodes(apu_id, market="HU", limit = 50)
    
    ep_count = 0

    while results:
        for ep in results["items"]:
            ep_list.append({"id": ep_count, "title": ep["name"], "url": ep["external_urls"]["spotify"]})
            ep_count += 1
        results = spotify.next(results)
    
    return ep_list

# %%

with open("spotify_keys.json","r") as f:
    spotify_keys = json.load(f)

ep_list = get_apu_ep_list(apu_id = '3Pv0slVPbeKGjssFDGaPhr', spotify_api_keys = (spotify_keys["client_id"], spotify_keys["client_secret"]))

# %%

for ep in ep_list:
    id = ep["id"]
    title = ep["title"]
    url = ep["url"]
    print(f"Started downloading episode '{title}'")
    os.system(f"youtube-dl --format 'bestaudio' {url} -o 'data/{id}.%(ext)s' --verbose")
    break

# %%
