# 💭 Reflection: Game Glitch Investigator
Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
- What did the game look like the first time you ran it?
  - Visually, the game actually looked pretty normal. It also kind of worked in that you were able to submit a guess. However, that was basically the only thing that worked correctly.

- List at least two concrete bugs you noticed at the start.
  (for example: "the hints were backwards").
  - Besides the hints, the new game button didn't work at all. It basically did nothing.
  - Most, if not all, of the numbers were inaccurate. For example: the scores, attempts, range, etc.

**Bug Reproduction Log**
> Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output/Error |
|-------|-------------------|-----------------|------------------------|
|Hints|If the guess is higher than the secret number, the hint should tell you to go lower. If the guess was lower than the secret number, the hint should tell you to go higher.|When the guess was higher than the secret number, the hint told you to go higher. When the guess was lower than the secret number, the hint told you to go lower.|This bug doesn't display an error message. It just doesn't work correctly.|
|New Game|When you click 'New Game,' a new game starts.|When you click 'New Game,' a new game does not start.|This bug doesn't display an error message. It just doesn't work correctly.|
|Scores|The score should be calculated correctly based on the outcome and attempt number. It should be displayed correctly at the end of the game and in the Developer Debug Info.|The score was not calculated correctly based on the outcome and attempt number. It was not displayed correctly at the end of the game and in the Developer Debug Info.|This bug doesn't display an error message. It just doesn't work correctly.|

---

## 2. How did you use AI as a teammate?
- Which AI tools did you use on this project (for example: ChatGPT,Gemini,Copilot)?
  - I mainly used Claude. It is set to Haiku 4.5, with thinking turned off. I also used Copilot, but only for the comparison stretch feature.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - The AI got the hints feature correct. It suggested to swap the hint messages around. I was able to verify this because when you run the game, giving a higher number always gave "Go Higher" as a hint, and vice versa. So, it was very likely that the messages were swapped.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - The AI got the color coding feature incorrect. It suggested a fix for the correct color so many times, but it was always wrong. I wanted the "Go Higher" message to be red, just like the "Hot" message, but it kept making it blue, and vice versa. 
---

## 3. Debugging and Testing Your Fixes
- How did you decide whether a bug was really fixed?
  - I mostly messed around with the guesses to test every possible case and outcome I could think of. Other bugs, like the color coding one, were straightforward. You can tell it is fixed just by looking at it.

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  - I manually ran a test on .markdown(). I didn't know how the formatting was suppose to work, so I had to test out what each formatting phrase did.

- Did AI help you design or understand any tests? How?
  - The AI definitely helped me design and understand the tests. I never knew what .markdown() was until doing this project with the AI. It showed me how formatting a background worked. I also never knew what pytest was, but the tests it generated gave me a better insight.
---

## 4. What did you learn about Streamlit and state?
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - Normally, when a script reaches the end, it finishes executing and terminates. However, when you want something that is constantly interactible, it needs to keep updating whatever the user is doing. Having .rerun() in the script is what allows this to happen.
  - If you also want something that feels permanent, you will have to have .session_state as well. Normally, when you rerun the same script, the data from the previous run does not stay. However, you can store that data as a session state that you can always have access to.
---

## 5. Looking Ahead: Your Developer Habits
- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - I want to break down my thought process more. At first, I was planning to focus on the application as a whole, and then move on to the documents. However, when I realized that I had to add a minimum of three commits throughout the project, I felt like I was being too general. I needed to break down my thought process more. So, I ended up focusing on just fixing the application's core logic first, then apply the stretch features on top of that, and lastly the document it in the .md files.

- This could be a testing habit, a prompting strategy, or a way you used Git.
  - I learned that the .git folder should be inside your project folder.

- What is one thing you would do differently next time you work with AI on a coding task?
  - I would change up the way I prompt the AI. I feel like I was asking for too much at once. I thought it would give the AI a better idea of what the application was like, when everything is together in one place, but when the fixes don't end up working, it just becomes one big problem.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - It is really impressive, however it is still not perfect.
