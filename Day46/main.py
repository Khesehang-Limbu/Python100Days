from pprint import pprint
import requests
import spotipy
from bs4 import BeautifulSoup

user_date = input("Enter the date you want to travel to (YYY-MM-DD) : ")
url = f"https://www.billboard.com/charts/hot-100/{user_date}/"
top_100_html = requests.get(url=url).text

top_100_soup = BeautifulSoup(top_100_html, "html.parser")
top_100_list = [song.getText().strip() for song in top_100_soup.select(selector="li #title-of-a-story")]

spotify_client_id = "id"
spotify_client_secret = "secret"
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

post_params = {
    "grant_type": "client_credentials",
    "client_id": spotify_client_id,
    "client_secret": spotify_client_secret,
}
scope = "playlist-modify-public"

access_token = spotipy.oauth2.SpotifyOAuth(client_id=spotify_client_id, client_secret=spotify_client_secret, redirect_uri="http://example.com", scope=scope)
client = spotipy.client.Spotify(oauth_manager=access_token)

current_user = client.current_user()
user_id = current_user["id"]

track_uri_list = []

playlists = client.current_user_playlists()["items"]
playlist_id = None
playlist = {}

exists = False
for item in playlists:
    if user_date == item["name"]:
        exists = True
        playlist_id = item["id"]
        playlist = item
        break

if not exists:
    user_playlist = client.user_playlist_create(user=user_id, name=f"{user_date}", public="true")
    playlist_id = user_playlist["id"]
    playlist_name = user_playlist["name"]

    for song in top_100_list:
        search_query = f"track:{song}"
        try:
            searched_song = client.search(q=search_query, type="track", limit="1")
            searched_song_uri = searched_song["tracks"]["items"][0]["uri"]
            track_uri_list.append(searched_song_uri)
        except:
            break
    try:
        res = client.playlist_add_items(playlist_id=playlist_id, items=track_uri_list)
        print(res)
    except:
        print("fail")
else:
    print("You already have the playlist of this date...")
    if playlist["tracks"]["total"] == 0:
        for song in top_100_list:
            search_query = f"track:{song}"
            try:
                searched_song = client.search(q=search_query, type="track", limit="1")
                searched_song_uri = searched_song["tracks"]["items"][0]["uri"]
                track_uri_list.append(searched_song_uri)
            except:
                break
        try:
            res = client.playlist_add_items(playlist_id=playlist_id, items=track_uri_list)
            print(res)
        except:
            print("fail")
