
# INSERT API client ID & tokens here.
# TODO: REMOVE THESE BEFORE MAKING PUBLIC COMMITS.
client_id = 'YsrwCCloXJysedZMDINWA-LItizvvaWZ2IGtxMlHYQ98R9G3sorFRo_rRLQGirRq'
client_secret = 'zqIKs-k2QP2o5rYmkNA382TZKASnZGFooyu1whMw9q4b5a10MGnv61fHt7EwwHP8KCl3bzRr2gmQ84tgOXKv0g'
client_access_token = 'tIRriGV3s4ljmlrrVDoxBFuXaiU31g6thOQ-czBEiXXKnk1_1aUd7jt7huoGTa_X'


class Lyric_Grabber:
    """   
        Using Genius API, fetch the lyrics for songs for a given artist.
        :param artist_name: artist's name, duh
        :param song_list: list of songs by artist_name - for fetching lyrics by song name.
        My API clients can be accessed here: https://genius.com/api-clients
    """
    def __init__(self, artist_name, song_list):
        self.artist_name = artist_name
        self.song_tite_list = song_list


    # TODO: Create a function to look up artist, albums, songs on Genius and grab all lyrics.
    def create_song_list():
        return None     # TODO: Implement


    # TODO: Write song list from `create_song_list()` to a file for later lookup.
    def write_song_list():
        return None     # TODO: Implement