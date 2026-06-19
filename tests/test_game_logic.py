import sys
import os

sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logic_utils import(
    check_guess,
    parse_guess,
    get_range_for_difficulty,
    update_score
)

class TestCheckGuess:
    """test suite for check_guess function"""

    def test_winning_guess(self):
        result = check_guess(50,50)
        assert result[0] == "Win"

    def test_guess_too_high(self):
        result = check_guess(60,50)
        assert result[0] == "Too High"

    def test_guess_too_low(self):
        result = check_guess(40,50)
        assert result[0] == "Too Low"

    def test_boundary_guess_high(self):
        result = check_guess(100,50)
        assert result[0] == "Too High"

    def test_boundary_guess_low(self):
        result = check_guess(0,50)
        assert result[0] == "Too Low"

class TestParseGuess:
    """test suite for parse_guess function with edge cases"""

    def test_valid_integer(self):
        ok, value, error = parse_guess("42")
        assert ok is True
        assert value == 42
        assert error is None

    def test_valid_float(self):
        ok, value, error = parse_guess("3.14")
        assert ok is True
        assert value == 3
        assert error is None

    def test_empty_string(self):
        ok, value, error = parse_guess("")
        assert ok is False
        assert value is None
        assert error == "no guess"

    def test_none_input(self):
        ok, value, error = parse_guess(None)
        assert ok is False
        assert value is None
        assert error == "none"

    def test_invalid_string(self):
        ok, value, error = parse_guess("abc")
        assert ok is False
        assert value is None
        assert error == "not a number"

    def test_special_characters(self):
        ok, value, error = parse_guess("@#$")
        assert ok is False
        assert value is None
        assert error == "not a number"

    def test_negative_number(self):
        ok, value, error = parse_guess("-50")
        assert ok is True
        assert value == -50
        assert error is None

    def test_negative_float(self):
        ok, value, error = parse_guess("-3.99")
        assert ok is True
        assert value == -3
        assert error is None

    def test_large_number(self):
        ok, value, error = parse_guess("999999")
        assert ok is True
        assert value == 999999
        assert error is None

    def test_zero(self):
        ok, value, error = parse_guess("0")
        assert ok is True
        assert value == 0
        assert error is None

class TestGetRangeForDifficulty:
    """test suite for get_range_for_difficulty function"""

    def test_easy_difficulty(self):
        low,high = get_range_for_difficulty("Easy")
        assert low == 0
        assert high == 30

    def test_normal_difficulty(self):
        low,high = get_range_for_difficulty("Normal")
        assert low == 30
        assert high == 60

    def test_hard_difficulty(self):
        low,high = get_range_for_difficulty("Hard")
        assert low == 60
        assert high == 100

    def test_unknown_difficulty(self):
        low,high = get_range_for_difficulty("Unknown")
        assert low == 30
        assert high == 60

    def test_empty_string(self):
        low,high = get_range_for_difficulty("")
        assert low == 30
        assert high == 60

class TestUpdateScore:
    """test suite for update_score function"""

    def test_win_on_first_attempt(self):
        score = update_score(
            current_score=100,
            outcome="Win",
            attempt_number=1,
            attempt_limit=10
        )

        assert score == 100

    def test_win_on_last_attempt(self):
        score = update_score(
            current_score=100,
            outcome="Win",
            attempt_number=10,
            attempt_limit=10
        )

        assert score == 10

    def test_win_on_middle_attempt(self):
        score = update_score(
            current_score=100,
            outcome="Win",
            attempt_number=5,
            attempt_limit=10
        )

        assert score == 60

    def test_non_win_guess(self):
        score = update_score(
            current_score=100,
            outcome="Too High",
            attempt_number=1,
            attempt_limit=10
        )

        assert score == 90

    def test_score_never_negative(self):
        score = update_score(
            current_score=5,
            outcome="Too Low",
            attempt_number=1,
            attempt_limit=10
        )

        assert score == 0

    def test_hard_difficulty_penalty(self):
        score = update_score(
            current_score=100,
            outcome="Too High",
            attempt_number=1,
            attempt_limit=5
        )

        assert score == 80
