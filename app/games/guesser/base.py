from dataclasses import dataclass, field
from typing import Dict, List


class Status:
    IN_PROGRESS: str = 'In progress'
    FINISH: str = 'Finish'
    NOT_FOUND: str = 'Not found'
    ERROR: str = 'Error'


@dataclass
class Word:
    word: str
    is_known: bool = False
        
    def check_word(self, model):
        try:
            _ = model.get_vector(self.word)
            self.is_known = True
        except KeyError:
            self.is_known = False


@dataclass
class State:
    guessed_word: str
    model_name: str
    words_count: int

    status: Status = Status.IN_PROGRESS
    words: List = field(default_factory=list)
