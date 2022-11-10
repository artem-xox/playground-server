from typing import List
import random

import gensim

from app.games.config import model_name
from app.games.gaps.base import Equation, State, Status


class GapsGame:

    equations: List = [
        Equation(['woman', 'king', 'man'], 'queen')
    ]
    
    def __init__(self):
        self.state = State(
            guessed_equantion=self._generate_equation(),
            model_name=model_name,
            equations_count=len(self.equations)
        )

    def new(self) -> None:
        self.state = State(
            guessed_equantion=self._generate_equation(),
            model_name=model_name,
            equations_count=len(self.equations)
        )
    
    def step(self, word: str, model: gensim.models.keyedvectors.KeyedVectors) -> None:
        try:
            word = Word(word)
            word.check_word(model)
        
            if not word.is_known:
                self.state.status = Status.NOT_FOUND
                return
            
            if word.word.lower() == self.state.guessed_equantion.ans:
                self.state.status = Status.FINISH
            
        except Exception as error:
            self.state.status = Status.ERROR
        
    def _generate_equation(self) -> Equation:
        return random.choice(self.equations)
    
    @property
    def _state(self) -> dict:
        return self.state.__dict__
