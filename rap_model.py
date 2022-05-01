from unittest.util import _MAX_LENGTH
import tokenizers
from transformers import GPT2Tokenizer, GPT2Model, pipeline, set_seed, TFGPT2Model, GPT2LMHeadModel         # Need to use Python 3.8.12 (anaconda `cs499` environment) as interpreter
import torch
from fetch_lyrics import *

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

"""
    Probe user for artist lyrics to generate.
"""
def user_select_artist():
    user_artist = None

    # Search .\lyrics\ for the file containing that artist's name, if it doesn't exist, prompt the user again.
    while user_artist == None:
        user_artist = input("Please type the full name (proper spelling and capitalization) of the rapper you wish to generate lyrics in the spirit of: ")
        if not os.path.exists('.\lyrics\\' + user_artist + '.txt'):
            print("CoZZy cannot find a rapper with name <%s> in his memory, please type a different rapper..." % user_artist, "\n\n")
            user_artist = None
        else:
            print("CoZZy will learn to rap like : <%s>" % user_artist)
            artist_lyric_file_path = '.\lyrics\\' + user_artist + '.txt'
            break
    return user_artist, artist_lyric_file_path


"""
    Initialize model and tokenizer.
"""
def initialize_model():
    print("Initializing model...\n")
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    model = GPT2LMHeadModel.from_pretrained('gpt2')

    return model, tokenizer


"""
    Create a tensor of the for the given artist selected by the user.
    I.e. Tokenize the input text - lyrics of 20 songs by artists
    This tensor will be used in model training.
"""
def create_lyric_tensor(artist_lyric_file_path, tokenizer):
    lyrics = []                                             # List of torch tensors containing encoded lyrics.
    with open(artist_lyric_file_path, 'r') as f:
        for line in f:
            lyrics.append(torch.tensor(tokenizer.encode()))
    return None
    #return torch.tensor(None)

"""
    Train GPT model on given artist.
    Model evaulation will be done in here too.

    TODO: Alternatively, create a vocabulary here of all songs from the .\lyrics\ and then use that to aid in training.
    NOTE: GPT2Tokenizer takes a vocabulary input: https://huggingface.co/docs/transformers/model_doc/gpt2 
"""
def train():

    # NOTE: Generate lyrics for rappers found in `list_rappers.txt`
    #       need to be only done once UNLESS new artists are added to .\data\list_rappers.txt
    #       AND/OR changes are made to code in `fetch_lyrics.py`.
    artists_list = list_all_rappers('.\data\list_rappers.txt', 76)
    create_lyrics(artists_list)
    
    user_artist, artist_lyric_file_path = user_select_artist()
    model, tokenizer = initialize_model()
    #lyric_tensor = create_lyric_tensor(artist_lyric_file_path, tokenizer)

    print("CoZZy is writing his lyrics...\n")

    # encoded_input = tokenizer(artist_lyric_file_path, return_tensors='pt')
    # --------------------------------------------------------------------
    # text = "Hello my name is Jeff."

    # encoded_input = tokenizer(text, return_tensors='pt')
    # outputs = model(**encoded_input, labels=encoded_input["input_ids"])
    # loss = outputs.loss
    # logits = outputs.logits

    # print(loss)
    # print(logits)
    # --------------------------------------------------------------------
    #generator = pipeline('text-generation', model = 'gpt2')
    #set_seed(42)
    #print(generator(artist_lyric_file_path, max_length=100, num_return_sequences=5))

    #output_tokens = model.generate(encoded_input, max_length = 200, do_sample = True)
    #lyrics = tokenizer.decode(output_tokens)
    #print(lyrics)

train()