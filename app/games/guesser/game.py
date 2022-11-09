from typing import List
import random
from numpy import abs

from app.games.guesser import constants
from app.games.guesser.base import State, Status, Word


class GuesserGame:
    
    model_name: str = constants.model_name
    words: List[str] = constants.words
    
    def __init__(self, model):
        self.model = model
        self.state = State(
            guessed_word=self._generate_word(),
            model_name=self.model_name,
            words_count=len(self.words)
        )

    def new(self) -> None:
        self.state = State(
            guessed_word=self._generate_word(),
            model_name=self.model_name,
            words_count=len(self.words)
        )
    
    def step(self, word: str) -> None:
        try:
            word = Word(word)
            word.check_word(self.model)
        
            if not word.is_known:
                self.state.status = Status.NOT_FOUND
                return

            distance = self.model.distance(word.word, self.state.guessed_word)
            score = int((1 - abs(distance)) * 100)
            self.state.words.insert(0, {"word": word.word, "score": score})

            if word.word.lower() == self.state.guessed_word:
                self.state.status = Status.FINISH
            else:
                self.state.status = Status.IN_PROGRESS    

        except Exception as error:
            self.state.status = Status.ERROR
        
    def _generate_word(self) -> Word:
        return random.choice(self.words)
    
    @property
    def _state(self) -> dict:
        return self.state.__dict__
