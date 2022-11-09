from app.games.guesser.constants import model_name
from app.games.guesser.game import GuesserGame

import gensim.downloader as api


def download_gensim_model(model_name: str):
    return api.load(model_name)


guesser_model = download_gensim_model(model_name)
guesser_game = GuesserGame(guesser_model)
