from lyricsgenius import Genius
import os
from pathlib import Path

# INSERT API client ID & tokens here.
# TODO: REMOVE THESE BEFORE MAKING PUBLIC COMMITS.
client_id = 'YsrwCCloXJysedZMDINWA-LItizvvaWZ2IGtxMlHYQ98R9G3sorFRo_rRLQGirRq'
client_secret = 'zqIKs-k2QP2o5rYmkNA382TZKASnZGFooyu1whMw9q4b5a10MGnv61fHt7EwwHP8KCl3bzRr2gmQ84tgOXKv0g'
client_access_token = 'tIRriGV3s4ljmlrrVDoxBFuXaiU31g6thOQ-czBEiXXKnk1_1aUd7jt7huoGTa_X'

# LyricsGenius package use:
genius = Genius(client_access_token, response_format='plain,html',
                timeout=5, sleep_time=0.2, retries=3)


class Lyric_Grabber:
    """   
        Using Genius API, fetch the lyrics for songs for a given artist.
        :param artist_name: artist's name, duh
        :param song_list: list of songs by artist_name - for fetching lyrics by song name.
        My API clients can be accessed here: https://genius.com/api-clients
    """
    def __init__(self, artist_name):
        self.artist_name = artist_name

    """
        Look up artist, albums, songs on Genius and grab all lyrics for artist.
        Write songs of artist to a file.

        genius.search_artist(artist_name,
            max_songs=None, sort='popularity',
            per_page=20, get_full_info=True, 
            allow_name_change=True, artist_id=None,
            include_features=False)
    """
    def create_song_list(self):
        artist = genius.search_artist(self.artist_name, max_songs=20,
                                    sort='popularity', get_full_info=False)

        """
        # Save artist lyrics to [ARTIST_NAME].txt
        artist.save_lyrics(filename=self.artist_name, extension='txt',
                            overwrite=False, ensure_ascii=True,
                            sanitize=True, verbose=False)
        """ 

        # If artist lyric file doesn't already exist, open for writing (i.e. create file if it doesn't already exist).
        cwd = str(Path.cwd()) + '\\lyrics'
        file_name = os.path.join(cwd, self.artist_name)
        lyric_file = open(file_name + '.txt', 'w')

        # NOTE: Alternatively, you can use genius.save_artists(artists, filename='artist_lyrics', overwrite=False, ensure_ascii=True)
        #       to save lyrics of multiple artists all at once into a single file - saves as JSON. 
        # Write lyrics to file and close when done.
        for song in artist.songs:
            lyric_file.write(song.lyrics)
            lyric_file.write("\n\n")
            
        lyric_file.close()