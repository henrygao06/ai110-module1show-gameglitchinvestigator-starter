def get_range_for_difficulty(difficulty:str) -> tuple[int,int]:
    """
    Get the secret number range for a given difficulty level.

    Args:
        difficulty(str): The difficulty level ("Easy", "Normal", or "Hard").
    Returns:
        tuple[int,int]: A tuple of (low,high) representing the inclusive
            range for the secret number. Defaults to (30,60) for unknown
            difficulty levels.
    """

    if difficulty == "Easy":
        return 0,30
    if difficulty == "Normal":
        return 30,60
    if difficulty == "Hard":
        return 60,100

    return 30,60

def parse_guess(raw:str) -> tuple[bool,int | None,str | None]:
    """
    Parse and validate user input as an integer guess.
    Converts string input (including floats like "3.14") to integers.
    Returns a status tuple indicating success, the parsed value, and
    any error message.

    Args:
        raw(str): The raw user input string to parse.
    Returns:
        tuple[bool,int | None,str | None]: A tuple of (ok,value,error)
            where ok is True if parsing succeeded, value is the parsed integer
            (or None on error), and error is a human-readable error message
            (or None on success).
    """

    if raw is None:
        return False,None,"none"
    if raw == "":
        return False,None,"no guess"

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False,None,"not a number"

    return True,value,None

def check_guess(guess:int,secret:int) -> tuple[str,str]:
    """
    Compare a guess against the secret number and return feedback.

    Args:
        guess(int): The player's guessed number.
        secret(int): The secret number to guess.
    Returns:
        tuple[str,str]: A tuple of (outcome, message) where outcome is one of
            "Win", "Too High", or "Too Low", and message is a user-friendly
            hint with emoji feedback.
    """

    if guess == secret:
        return "Win","Correct!"

    try:
        if guess > secret:
            return "Too High","📉 Go LOWER!"
        else:
            return "Too Low","📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win","Correct!"
        if g>secret:
            return "Too High","📉 Go LOWER!"

        return "Too Low","📈 Go HIGHER!"

def update_score(
    current_score:int,
    outcome:str,
    attempt_number:int,
    attempt_limit:int = 10
) -> int:
    """
    Calculate the player's score based on game outcome and attempts.
    On a win, score is calculated by subtracting a fixed penalty per attempt.
    On a non-win guess, a fixed penalty is subtracted from the current score.
    Score never goes below 0.

    Args:
        current_score(int): The player's current score before this guess.
        outcome(str): The result of the guess ("Win", "Too High", or "Too Low").
        attempt_number(int): The number of attempts made (1-indexed).
        attempt_limit(int,optional): The maximum allowed attempts for the
            difficulty level. Defaults to 10.
    Returns:
        int: The updated score, guaranteed to be >= 0.
    """

    if outcome == "Win":
        points_per_attempt = 100//attempt_limit
        points = 100-points_per_attempt*(attempt_number-1)
        return max(0,points)

    return max(0,current_score-(100//attempt_limit))

def calculate_temperature(guess:int,secret:int) -> str:
    """
    Calculate how close the guess is to the secret number.

    Args:
        guess(int): The player's guessed number.
        secret(int): The secret number to guess.
    Returns:
        str: Temperature descriptor ("Hot 🔥", "Warm 🌡️", or "Cold ❄️")
            based on proximity to the secret number.
    """

    distance = abs(guess-secret)
    if distance <= 5:
        return "Hot 🔥"
    elif distance <= 10:
        return "Warm 🌡️"
    else:
        return "Cold ❄️"
