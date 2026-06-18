import sys
import os

sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from logic_utils import checkGuess

def test_winning_guess():
    result = checkGuess(50,50)
    assert result[0] == "Win"

def test_guess_too_high():
    result = checkGuess(60,50)
    assert result[0] == "Too High"

def test_guess_too_low():
    result = checkGuess(40,50)
    assert result[0] == "Too Low"
