import gpt_2_simple as gpt2
from datetime import datetime
import tensorflow as tf
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
def initialize_model(model_downloaded):
    
    if(not model_downloaded):
        print("Initializing model...\n")
        model = gpt2.download_gpt2(model_name="124M")
        return model
    else:
        print("Model already downloaded!\n")
        return

"""
    Create a persistent TensorFlow session which stores the training configuration,
    and then run the training for the specified number of steps (to run indefinitely, step == -1).

    Model checkpoints are saved in \checkpoint\run1 by default and checkpoints are saved every 500 steps.
"""
def start_session():
    session = gpt2.start_tf_sess()
    tf.compat.v1.reset_default_graph()
    if not session:
        session = gpt2.start_tf_sess()
    else:
        session = gpt2.reset_session(session)
    return session

"""
    Train GPT model on given artist.
    Model evaulation will be done in here too.

    TODO: Alternatively, create a vocabulary here of all songs from the .\lyrics\ and then use that to aid in training.
    NOTE: GPT2Tokenizer takes a vocabulary input: https://huggingface.co/docs/transformers/model_doc/gpt2

    Other optional-but-helpful parameters for gpt2.finetune:
        (1) restore_from: Set to fresh to start training from the base GPT-2, or set to latest to restart training from an existing checkpoint.
        (2) sample_every: Number of steps to print example output
        (3) print_every: Number of steps to print training progress.
        (4) learning_rate: Learning rate for the training. (default 1e-4, can lower to 1e-5 if you have <1MB input data)
        (5) run_name: subfolder within checkpoint to save the model. This is useful if you want to work with multiple models (will also need to specify run_name when loading the model)
        (6) overwrite: Set to True if you want to continue finetuning an existing model (w/ restore_from='latest') without creating duplicate copies.
"""
def train():

    # NOTE: Generate lyrics for rappers found in `list_rappers.txt`
    #       need to be only done once UNLESS new artists are added to .\data\list_rappers.txt
    #       AND/OR changes are made to code in `fetch_lyrics.py`.
    # artists_list = list_all_rappers('.\data\list_rappers.txt', 76)
    # create_lyrics(artists_list)
    
    user_artist, artist_lyric_file_path = user_select_artist()
    model = initialize_model(model_downloaded=True)
    session = start_session()

    print("CoZZy is learning to write his lyrics...\n")

    gpt2.finetune(session,
                dataset = artist_lyric_file_path,
                model_name = '124M',
                steps = 1000,
                learning_rate = 0.0001,
                restore_from ='fresh',
                run_name ='run1',                # subfolder within checkpoint to save the model (useful when working with multiple models)
                print_every = 10,
                sample_every = 200,
                save_every = 500)

train()