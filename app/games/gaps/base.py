from dataclasses import dataclass, field
from typing import Dict, List


class Status:
    IN_PROGRESS: str = 'In progress'
    FINISH: str = 'Finish'
    NOT_FOUND: str = 'Not found'
    ERROR: str = 'Error'


@dataclass
class Equation:
    """
    words: woman + king - man
    answer: queen
    """
    words: List[str]
    answer: str
        
    first: str = ''
    second: str = ''
    third: str = ''
        
    answer: str = ''
    
    def __post_init__(self):
        self.first = self.words[0]
        self.second = self.words[1]
        self.third = self.words[2]


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
    guessed_equantion: Equation
    model_name: str
    equations_count: int

    status: Status = Status.IN_PROGRESS
    equations: List = field(default_factory=list)
