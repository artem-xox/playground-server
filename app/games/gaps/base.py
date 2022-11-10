from dataclasses import dataclass, field
from typing import Dict, List


class Status:
    IN_PROGRESS: str = 'In progress'
    FINISH: str = 'Finish'
    NOT_FOUND: str = 'Not found'
    ERROR: str = 'Error'


@dataclass
class Equation:
    missed_word: str


@dataclass
class State:
    guessed_equantion: Equation
    model_name: str
    equations_count: int

    status: Status = Status.IN_PROGRESS
    equations: List = field(default_factory=list)
