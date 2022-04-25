from transformers import GPT2Tokenizer, TFGPT2Model         # Need to use Python 3.8.12 (anaconda `cs499` environment) as interpreter
from fetch_lyrics import *

## Single object test:
# young_sinatra = Lyric_Grabber('Logic')
# young_sinatra.create_song_list()

"""
    Iterate through list_rappers.txt & make list of artists.
    :param filename file containing list of artists
    :param num_rappers size of artists list - number of artists to pull from artist_names
    NOTE: list_rappers.txt contains 76 artist names.
"""
def list_all_rappers(filename, num_rappers):
    artists = []
    artist_names = open(filename).read().splitlines()
    for name in artist_names[:num_rappers]:
        artists.append(name)
    return artists

"""
    Create LyricGrabber objects for each artist in artists_list to create .txt file of a select number of his/her songs.
"""
def create_lyrics(artists_list):
    for name in artists_list:
        artist = Lyric_Grabber(name)
        artist.create_song_list()       # Will write file to `.\lyrics` of ARTIST_NAME.txt
        print("Lyrics for <%s> written to .\lyrics\ directory!\n" % name)
    print("\n\nDone writing lyrics to directory!\n\n")

# Generate lyrics for rappers found in `list_rappers.txt`
artists_list = list_all_rappers('.\data\list_rappers.txt', 76)
create_lyrics(artists_list)

# Ask the user what artist they would like to generate lyrics for - this will later be used in Lyric_Grabber objects.
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = TFGPT2Model.from_pretrained('gpt2')
text = "The Industrial Revolution has destroyed the foundations of American culture."
encoded_input = tokenizer(text, return_tensors='tf')
output = model(encoded_input)