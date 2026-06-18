import random
import streamlit as st

from logic_utils import getRangeForDifficulty,parseGuess,checkGuess,updateScore

st.set_page_config(page_title="notGlitchy Guesser",page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Nothing is off.")

st.sidebar.header("Settings")
if "difficulty" not in st.session_state:
    st.session_state.difficulty = "Normal"

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy","Normal","Hard"],
    index = ["Easy","Normal","Hard"].index(st.session_state.difficulty),
)

if difficulty != st.session_state.difficulty:
    st.session_state.difficulty = difficulty
    st.session_state.attempts = 0
    st.session_state.score = 100
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.balloonsShown = False
    st.session_state.lastMessage = None
    st.session_state.lastOutcome = None
    low, high = getRangeForDifficulty(difficulty)
    st.session_state.secret = random.randint(low,high)
    st.session_state.guessInput = ""

st.session_state.difficulty = difficulty
attempt_limit_map = {
    "Easy": 15,
    "Normal": 10,
    "Hard": 5,
}

attempt_limit = attempt_limit_map[difficulty]
low,high = getRangeForDifficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts Allowed: {attempt_limit}")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low,high)

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "score" not in st.session_state:
    st.session_state.score = 100

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

st.subheader("Make a Guess")
st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempt_limit-st.session_state.attempts}"
)

def onSubmit():
    rawGuess = st.session_state.guessInput
    ok,intGuess,err = parseGuess(rawGuess)
    if not ok:
        st.session_state.history.append(err)
    else:
        st.session_state.attempts += 1
        st.session_state.history.append(intGuess)

        secret = st.session_state.secret
        outcome,message = checkGuess(intGuess,secret)

        st.session_state.score = updateScore(
            currentScore=st.session_state.score,
            outcome=outcome,
            attemptNumber=st.session_state.attempts,
            attemptLimit=attempt_limit_map[difficulty],
        )

        if outcome == "Win":
            st.session_state.status = "won"
        elif st.session_state.attempts >= attempt_limit_map[difficulty]:
            st.session_state.status = "lost"

        st.session_state.lastMessage = message
        st.session_state.lastOutcome = outcome

    st.session_state.guessInput = ""

def onNewGame():
    st.session_state.attempts = 0
    st.session_state.score = 100
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.balloonsShown = False
    st.session_state.lastMessage = None
    st.session_state.lastOutcome = None
    low, high = getRangeForDifficulty(difficulty)
    st.session_state.secret = random.randint(low,high)
    st.session_state.guessInput = ""

rawGuess = st.text_input(
    "Enter your guess:",
    key = "guessInput"
)

col1, col2, col3 = st.columns(3)
with col1:
    st.button("Submit Guess 🚀",on_click=onSubmit)
with col2:
    st.button("New Game 🔁",on_click=onNewGame)
with col3:
    showHint = st.checkbox("Show Hint",value=True)

if "lastMessage" in st.session_state and showHint:
    if st.session_state.lastOutcome == "Win":
        st.success(f"🎉 {st.session_state.lastMessage}")
    else:
        st.warning(st.session_state.lastMessage)

if st.session_state.status == "won" and not st.session_state.get("balloonsShown",False):
    st.balloons()
    st.session_state.balloonsShown = True

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success(
            f"You won! The secret number was {st.session_state.secret}. "
            f"Final score: {st.session_state.score}"
        )

        st.info("Click 'New Game' to play again.")
    else:
        st.error(
            f"Out of attempts! "
            f"The secret number was {st.session_state.secret}. "
            f"Score: {st.session_state.score}"
        )

        st.info("Click 'New Game' to play again.")

    st.stop()

with st.expander("Developer Debug Info"):
    st.write("Secret:",st.session_state.secret)
    st.write("Attempts:",st.session_state.attempts)
    st.write("Score:",st.session_state.score)
    st.write("Difficulty:",difficulty)
    st.write("History:",st.session_state.history)

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
