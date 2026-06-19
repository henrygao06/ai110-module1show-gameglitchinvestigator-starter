import random

import streamlit as st
import pandas as pd

from logic_utils import(
    get_range_for_difficulty,
    parse_guess,
    check_guess,
    update_score,
    calculate_temperature
)

st.set_page_config(page_title="notGlitchy Guesser",page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Nothing is off.")

st.sidebar.header("Settings")
if "difficulty" not in st.session_state:
    st.session_state.difficulty = "Normal"
if "high_scores" not in st.session_state:
    st.session_state.high_scores = {"Easy": 0,"Normal": 0,"Hard": 0}

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy","Normal","Hard"],
    index=["Easy","Normal","Hard"].index(st.session_state.difficulty)
)

if difficulty != st.session_state.difficulty:
    st.session_state.difficulty = difficulty
    st.session_state.attempts = 0
    st.session_state.score = 100
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.balloons_shown = False
    st.session_state.last_message = None
    st.session_state.last_outcome = None
    st.session_state.last_temperature = None
    low,high = get_range_for_difficulty(difficulty)
    st.session_state.secret = random.randint(low,high)
    st.session_state.guess_input = ""
    st.rerun()

attempt_limit_map = {
    "Easy": 15,
    "Normal": 10,
    "Hard": 5
}

attempt_limit = attempt_limit_map[difficulty]
low,high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts Allowed: {attempt_limit}")

st.sidebar.divider()
st.sidebar.subheader("🏆 High Scores")
for diff in ["Easy","Normal","Hard"]:
    score = st.session_state.high_scores[diff]
    st.sidebar.metric(f"{diff} Mode",score if score > 0 else "—")

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

if "last_temperature" not in st.session_state:
    st.session_state.last_temperature = None

if "debug_expanded" not in st.session_state:
    st.session_state.debug_expanded = False

st.subheader("Make a Guess")
st.markdown(
    f"<div style='background-color:#f0f0f0;padding:10px;border-radius:5px;'>"
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempt_limit-st.session_state.attempts}"
    f"</div>",
    unsafe_allow_html=True
)

st.markdown("<br>",unsafe_allow_html=True)

def on_submit():
    raw_guess = st.session_state.guess_input
    ok,int_guess,err = parse_guess(raw_guess)
    if not ok:
        st.session_state.history.append(err)
    else:
        st.session_state.attempts += 1
        st.session_state.history.append(int_guess)

        secret = st.session_state.secret
        outcome,message = check_guess(int_guess,secret)
        temperature = calculate_temperature(int_guess,secret)

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
            attempt_limit=attempt_limit_map[difficulty]
        )

        if outcome == "Win":
            st.session_state.status = "won"
            if st.session_state.score>st.session_state.high_scores[difficulty]:
                st.session_state.high_scores[difficulty] = st.session_state.score
        elif st.session_state.attempts >= attempt_limit_map[difficulty]:
            st.session_state.status = "lost"

        st.session_state.last_message = message
        st.session_state.last_outcome = outcome
        st.session_state.last_temperature = temperature

    st.session_state.guess_input = ""

def on_new_game():
    st.session_state.attempts = 0
    st.session_state.score = 100
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.balloons_shown = False
    st.session_state.last_message = None
    st.session_state.last_outcome = None
    st.session_state.last_temperature = None
    low,high = get_range_for_difficulty(difficulty)
    st.session_state.secret = random.randint(low,high)
    st.session_state.guess_input = ""

# old code:
# if new_game:
#     st.session_state.attempts = 0
#     st.session_state.secret = random.randint(1,100)
#     st.success("A new game has started.")
#     st.rerun()
#
# claudeCode first fix:
# if new_game:
#     st.session_state.attempts = 0
#     st.session_state.score = 0
#     st.session_state.status = "playing"
#     st.session_state.history = []
#     st.session_state.secret = random.randint(1,100)
#     st.success("A new game has started.")
#     st.rerun()
#
# copilot first fix:
# if new_game:
#     st.session_state.attempts = 0
#     st.session_state.secret = random.randint(1,100)
#     st.session_state.guess_history = []
#     st.success("A new game has started.")
#     st.rerun()

raw_guess = st.text_input(
    "Enter your guess:",
    key="guess_input"
)

col1,col2,col3 = st.columns(3)
with col1:
    st.button("Submit Guess 🚀",on_click=on_submit)
with col2:
    st.button("New Game 🔁",on_click=on_new_game)
with col3:
    show_hint = st.checkbox("Show Hint",value=True)

if(
    "last_message"
    in st.session_state
    and show_hint
    and st.session_state.status == "playing"
):
    if st.session_state.last_outcome == "Win":
        st.success(f"🎉 {st.session_state.last_message}")
    elif st.session_state.last_outcome == "Too High":
        st.markdown(
            "<div style='background-color:#e3f2fd;padding:10px;border-radius:5px;'>"
            f"<span style='color:#1976d2;'>{st.session_state.last_message}</span>"
            "</div>",
            unsafe_allow_html=True
        )
    elif st.session_state.last_outcome == "Too Low":
        st.markdown(
            "<div style='background-color:#ffcccc;padding:10px;border-radius:5px;'>"
            f"<span style='color:#cc0000;'>{st.session_state.last_message}</span>"
            "</div>",
            unsafe_allow_html=True
        )

    if st.session_state.last_temperature:
        temp = st.session_state.last_temperature
        if "Hot" in temp:
            st.markdown(
                "<div style='background-color:#ffcccc;padding:10px;border-radius:5px;'>"
                f"<span style='color:#cc0000;'>{temp}</span>"
                "</div>",
                unsafe_allow_html=True
            )
        elif "Warm" in temp:
            st.markdown(
                "<div style='background-color:#ffffcc;padding:10px;border-radius:5px;'>"
                f"<span style='color:#cc8800;'>{temp}</span>"
                "</div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                "<div style='background-color:#e3f2fd;padding:10px;border-radius:5px;'>"
                f"<span style='color:#1976d2;'>{temp}</span>"
                "</div>",
                unsafe_allow_html=True
            )

st.markdown("<br>",unsafe_allow_html=True)

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        if not st.session_state.get("balloons_shown",False):
            st.balloons()
            st.session_state.balloons_shown = True

        st.markdown(
            "<div style='background-color:#c8e6c9;padding:10px;border-radius:5px;'>"
            f"<span style='color:#2e7d32;'>You won! The secret number was {st.session_state.secret}. Final Score: {st.session_state.score}</span>"
            "</div>",
            unsafe_allow_html=True
        )

        is_new_record = (
            st.session_state.score == st.session_state.high_scores[difficulty]
        )

        if is_new_record:
            st.markdown(
                "<div style='background-color:#ffffcc;padding:10px;border-radius:5px;'>"
                "<span style='color:#cc8800;'>🏆 New High Score!</span>"
                "</div>",
                unsafe_allow_html=True
            )
    else:
        st.markdown(
            "<div style='background-color:#ffcccc;padding:10px;border-radius:5px;'>"
            f"<span style='color:#cc0000;'>You are out of attempts! The secret number was {st.session_state.secret}. Final Score: {st.session_state.score}</span>"
            "</div>",
            unsafe_allow_html=True
        )

    st.markdown(
        "<div style='background-color:#e3f2fd;padding:10px;border-radius:5px;'>"
        "<span style='color:#1976d2;'>Click 'New Game' to play again.</span>"
        "</div>",
        unsafe_allow_html=True
    )

    st.divider()
    st.subheader("📈 Game Summary")
    numeric_guesses = [g for g in st.session_state.history if isinstance(g,int)]
    summary_data = {
        "Secret Number": [st.session_state.secret],
        "Total Attempts": [len(numeric_guesses)],
        "Final Score": [st.session_state.score]
    }

    summary_df = pd.DataFrame(summary_data)
    st.dataframe(summary_df,hide_index=True)

    st.subheader("📊 Guess History")
    if numeric_guesses:
        secret = st.session_state.secret
        history_data = []
        for i,guess in enumerate(numeric_guesses,1):
            distance = abs(guess-secret)
            outcome = "✓ Win" if guess == secret else f"{distance} away"
            history_data.append({"Attempt":i,"Guess":guess,"Status":outcome})

        history_df = pd.DataFrame(history_data)
        st.dataframe(
            history_df,
            hide_index=True,
            column_config={
                "Attempt": st.column_config.NumberColumn(alignment="left"),
                "Guess": st.column_config.NumberColumn(alignment="left"),
                "Status": st.column_config.TextColumn(alignment="left")
            }
        )

    with st.expander("Developer Debug Info",expanded=False):
        st.write("Secret:",st.session_state.secret)
        st.write("Attempts:",st.session_state.attempts)
        st.write("Score:",st.session_state.score)
        st.write("Difficulty:",difficulty)
        st.write("History:",st.session_state.history)

    st.stop()

if st.session_state.status == "playing":
    with st.expander("Developer Debug Info",expanded=st.session_state.get("debug_expanded", False)) as expander_state:
        st.write("Secret:",st.session_state.secret)
        st.write("Attempts:",st.session_state.attempts)
        st.write("Score:",st.session_state.score)
        st.write("Difficulty:",difficulty)
        st.write("History:",st.session_state.history)

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
