from typing import List
import random

from app.games.config import model_name
from app.games.gaps.base import Equation, State, Status


class GapsGame:

    equations: List = [
        Equation(missed_word='a'), Equation(missed_word='b')
        ]
    
    def __init__(self, model):
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
    
    def step(self, word: str) -> None:
        try:
            pass
        except Exception as error:
            pass
        
    def _generate_equation(self) -> Equation:
        return random.choice(self.equations)
    
    @property
    def _state(self) -> dict:
        return self.state.__dict__
