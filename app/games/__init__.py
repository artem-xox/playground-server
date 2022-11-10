import gensim.downloader as api

from app.games.config import model_name
from app.games.gaps.game import GapsGame
from app.games.guesser.game import GuesserGame


def download_gensim_model(model_name: str):
    return api.load(model_name)


model = download_gensim_model(model_name)

gaps_game = GapsGame(model)
guesser_game = GuesserGame(model)
