# AI Interactions Log
**Stretch Features Only**
> Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.
---
## Agent Workflow (SF8)
> Document your experience using an AI agent (e.g., Cursor Agent,Claude,Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**
- First, I asked the agent to fix the problems for me. I gave it the problems I found and asked it to look for problems that I might have missed.
- Then, I asked the agent to apply the stretch features for me. I gave it the specific stretch features I was looking for, like the High Score Chart, Game Summary, Guess History, etc.

**What did the agent do?**
- First, it always looked over the app.py and logic_utils.py files.
- Then, it made fixes for the problems it found.
- Next, it ran some tests to make sure they all passed.
- Finally, it summarized everything that it did.

**What did you have to verify or fix manually?**
- A lot of the stretch features required fixes. A lot of the fixes itself required fixes. I mainly verified to see if the fixes, it provided, fixed the problems that I found and prompted. If it didn't, I would, again, verify to see what the new problems are, and so on and so forth. If it keeps running into problems, I do end up trying to manually fix it, like with the .markdown() functions.
---
## Test Generation (SF7)
> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did it pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
|validFloat|"identify three potential edge case inputs and generate a suite of pytest cases that verify these inputs gracefully"|def test_valid_float(self):<br>&emsp;&ensp;ok,value,error = parse_guess("3.14")<br>&emsp;&ensp;assert ok is True<br>&emsp;&ensp;assert value == 3<br>&emsp;&ensp;assert error is None|Yes|a float can be within the given range, but it can also be really small, leading to many possible guesses, making the game feel unplayable|
|emptyString|"identify three potential edge case inputs and generate a suite of pytest cases that verify these inputs gracefully"|def test_empty_string(self):<br>&emsp;&ensp;ok,value,error = parse_guess("")<br>&emsp;&ensp;assert ok is False<br>&emsp;&ensp;assert value == None<br>&emsp;&ensp;assert error == "no guess"|Yes|the point of the game is to guess a number|
|invalidString|"identify three potential edge case inputs and generate a suite of pytest cases that verify these inputs gracefully"|def test_invalid_string(self):<br>&emsp;&ensp;ok,value,error = parse_guess("abc")<br>&emsp;&ensp;assert ok is False<br>&emsp;&ensp;assert value is None<br>&emsp;&ensp;assert error == "not a number"|Yes|the point of the game is to guess a number|
---
## Linting & Style (SF9)
> Document your use of AI for linting or code style improvements.

**Prompt Used:**

```
"add professional grade docstrings to every function in logic_utils.py, use the pep 8 style, change anything that isn't in this style"
```

**Linting Output Before:**

```
"Renamed all camelCase function names to snake_case: getRangeForDifficulty → get_range_for_difficulty, parseGuess → parse_guess, checkGuess → check_guess, updateScore → update_score"

"Renamed all camelCase variables to snake_case: rawGuess → raw_guess, intGuess → int_guess, onSubmit → on_submit, onNewGame → on_new_game, balloonsShown → balloons_shown, lastMessage → last_message, lastOutcome → last_outcome, lastTemperature → last_temperature, guessInput → guess_input, showHint → show_hint"
```

**Changes Applied:**
I left all the changes to the function and variable names.

---
## Model Comparison (SF11)
> Compare two AI models on the same task.

**Task Given to Both Models:**
| | Model A | Model B |
|-|---------|---------|
| **Model Name** |claudeCode;claudeHaiku4.5|copilot;claudeHaiku4.5|
| **Response Summary** |if new_game:<br>&emsp;&ensp;st.session_state.attempts = 0<br>&emsp;&ensp;st.session_state.score = 0<br>&emsp;&ensp;st.session_state.status = "playing"<br>&emsp;&ensp;st.session_state.history = []<br>&emsp;&ensp;st.session_state.secret = random.randint(1,100)<br>&emsp;&ensp;st.success("A new game has started.")<br>&emsp;&ensp;st.rerun()|if new_game:<br>&emsp;&ensp;st.session_state.attempts = 0<br>&emsp;&ensp;st.session_state.secret = random.randint(1,100)<br>&emsp;&ensp;st.session_state.guess_history = []<br>&emsp;&ensp;st.success("A new game has started.")<br>&emsp;&ensp;st.rerun()|
| **More Pythonic?** |Equal|Equal|
| **Clearer Explanation?** |Equal|Equal|

<br> **Which did you prefer and why?**
<br>&emsp;&ensp; Both models did basically the same thing. I'm not even sure if using claudeHaiku4.5 with a different AI makes a difference, but I was curious, so that's why I did this test. It does feel like claudeCode was a little bit more detailed, it's also the one that I used the most, so I think I prefer it more over Copilot.
