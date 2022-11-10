import gensim.downloader as api

from app.games.config import model_name
from app.games.gaps.game import GapsGame
from app.games.guesser.game import GuesserGame


def download_gensim_model(model_name: str):
    return api.load(model_name)


gensim_model = download_gensim_model(model_name)

gaps_game = GapsGame()
guesser_game = GuesserGame()
