# Rap Lyric Generation for CS499 Final Project - Natural Language Processing

### Getting Started
- Be sure to use `pip` to install all packages required to use this model with the following command:
    - `pip install -r requirements.txt`
- Any other additional packages that need to be installed are done directly in the Google Colaboration Notebook available in this repository. The package(s) present in `requirements.txt` are used purely for data collection, which is now the only purpose of both `fetch_lyrics.py` and `rap_model.py`.

- Start by running `rap_model.py` to aggregate songs for all artists in `.\data\list_rappers.txt`, which executes two functions needed to generate the necessary lyric files in the `.\lyrics` directory.
    - Once this is done, please move to the next section entitled *Google Colab*!

### Google Colab
- Included in this repository is a Google Colab notebook (.ipynb file) that enables you to actually train a small GPT-2 model and generate text! If you navigate to the notebook, all cells have instructions on what do in each. Below I have made some special notes for cells that require extra attention more than just running them.

    - ***Cell 2:***
        - Please replace `GIT_USERNAME` and `GIT_TOKEN` with your Github username and your Github Personal Access Token, respectively.
        - Optionally, you can replace `MY_GOOGLE_DRIVE_PATH` with any path you desire other than the default I set.

    - ***Cell 6:***
        - After running the cell, you will be prompted to upload files to the Colab notebook. Upload all individual text files from the `.\lyrics` directory here so that lyric data files can be found in subsequent cells for later usage.

    - ***The second to last cell:***
        - In case you cloned to forked this repository and want to commit changes made to the repository, you can do so directly from the Google Colab notebook. In this cell, make sure you fill in the user email and username fields to make commits.

- A link to the Google Colab notebook is [here](https://colab.research.google.com/drive/1lxfRPhkAzKKpRzubyrswyCdK7f4DxKhw?usp=sharing)!

### Directories & Files
- `.\data\list_rappers.txt` :: file for list of popular American rappers (and some Pop artists) I've heard of or personally listen to parsed from [HipHopDatabase](https://hiphopdatabase.fandom.com/wiki/List_of_American_rappers).

- `.\lyrics\...` :: directory of aggregated artist lyrics by artist name.
    - Contains 76 artists, with lyrics from his/her top 20 most popular songs according to Genius.com

- `.\writeups\` :: directory containing semester project reports starting from semester week 8. The titles of each document is pretty self-explanatory so I don't think I need to elaborate :).
    - `research_sources.txt` was my own personal paper trail of sites and sources I referenced throughout the process in case anyone would like to do something similar to this, he/she has solid place to start!