from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from enum import Enum

class Characters(Enum):
    btn_lowercase = ascii_lowercase
    btn_highercase = ascii_uppercase
    btn_nums = digits
    btn_specialsymbols = punctuation

CHARACTER_NUMBER = {
    'btn_lowercase': len(Characters.btn_lowercase.value),
    'btn_highercase': len(Characters.btn_highercase.value),
    'btn_nums': len(Characters.btn_nums.value),
    'btn_specialsymbols': len(Characters.btn_specialsymbols.value),
}

GENERATE_PASSWORD = (
    'btn_lowercase', 'btn_highercase', 'btn_nums', 'btn_specialsymbols', 'btn_refresh'
)
