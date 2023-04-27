"""
create dataclass `Engine`
"""
from dataclasses import dataclass

# Добавление атрибутов volume и pistons
@dataclass
class Engine:
    volume: int
    pistons: int
