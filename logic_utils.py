def getRangeForDifficulty(difficulty:str):
    """return (low,high) inclusive range for a given difficulty"""

    if difficulty == "Easy":
        return 0,30
    if difficulty == "Normal":
        return 30,60
    if difficulty == "Hard":
        return 60,100

    return 30,60

def parseGuess(raw:str):
    """
    parse user input into an int guess
    returns: (ok:bool,guessInt:int | None,errorMessage:str | None)
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

def checkGuess(guess,secret):
    """
    compare guess to secret and return (outcome,message).
    outcome examples: "Win","Too High","Too Low"
    """

    if guess == secret:
        return "Win","Correct!"

    try:
        if guess>secret:
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

def updateScore(currentScore:int,outcome:str,attemptNumber:int,attemptLimit:int=10):
    """update score based on outcome and attemptNumber"""

    if outcome == "Win":
        pointsPerAttempt = 100//attemptLimit
        points = 100-pointsPerAttempt*(attemptNumber-1)
        return max(0,points)

    return max(0,currentScore-(100//attemptLimit))
