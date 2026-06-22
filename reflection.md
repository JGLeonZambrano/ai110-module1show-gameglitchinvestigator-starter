# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
It was fine: an intuitive, direct UI with a nice button letting one see the attempts in place and the secret number only if opened for debugging.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
1.- Numbers out of range (0, negative numbers, anything above 100) are still counted as valid if incorrect attempts, not rejected. I expected a message telling me that they weren't allowed.
2.- Entering ndecimals is allowed, even though it shouldn't be. I expected a notification saying the input is invalid ("no decimals"), akin to the "That's not a number" notification when one enters an alphanumeric character.
3.- The New Game button is glitchy: Pressing may reset the secret number but one cannot enter a new guess: instead of it being recorded, the mesage displayed remains "You already won. Start a new game to play again." I expected instead to start a new game.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input       | Expected Behavior | Actual Behavior | Console Output / Error |
|-------------|-------------------|-----------------|------------------------|
|Guess of 0   |Error Message "Number out of range" |Attempt counted and hint provided (too low in this case, but varied) | None|
| Guess of 7.5|Error Message "Invalid input please enter a whole number" |Attempt counted and hint provided |None |
|New Game pressed |New game triggered, with new attempts allowed for a new number |"Game over. Start a new game to try again." or "You already won. Start a new game to play again." message displayed, depending on the previous result|None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude Code
- Give one example of an AI suggestion that was correct (including what 
the AI suggested and how you verified the result).
Claude correctly identified that the New Game bug was caused by the status 
field in session_state never being reset to "playing" when a new game started. It suggested adding `st.session_state.status = "playing"` to the new_game block. 
I verified this by playing a game to completion, clicking New Game, and confirming I could enter a new guess without hitting the "You already won" wall.
- Give one example of an AI suggestion that was incorrect or misleading.
Claude initially suggested placing the FIXME comments inside the try block, 
which was slightly misleading since the logic break happens before the try block executes. I moved them outside to better mark the actual problem location.

---

## 3. Debugging and testing your fixes

## 3. Debugging and testing your fixes
- How did you decide whether a bug was really fixed?
I used two methods:
First, manual testing in the live Streamlit app (entering  a decimal, an out-of-range number, and pressing New Game after winning) to confirm the correct error messages appeared and the game reset properly.
Second, running pytest to confirm the fixes held up programmatically with 5/5 tests passing.

- Describe at least one test you ran (manual or using pytest) and what it showed you.
I wrote test_decimal_input_rejected() and test_out_of_range_rejected() in 
tests/test_game_logic.py. Running PYTHONPATH=. pytest showed all 5 tests passing, confirming that parse_guess() now correctly rejects "7.5" and "0" instead of silently accepting them as valid guesses.

- Did AI help you design or understand any tests? How?
Yes. I specifically asked to first explain the exact nature of the tests and commands per se before even trying anything. 
Claude then suggested specifically the structure of the pytest tests and explained that check_guess() returns a tuple (outcome, message), which is why the original starter tests needed to be updated to unpack both values (without that the existing tests would have crashed).
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit is an open-source library for Python that will allow you to create something like a website locally; that is, it is a group of commands anyone can access, so that you can run the program from your computer quickly and without additional coding. To do this, it reads the entire code you wrote, top to bottom, when you run it, again and again (ie, it "reruns" it.)
If you make a change in one of these "sessions", like scoring some points or in this case running out of attempts, you can write down how things were at a particular moment of that session elsewhere, ie in the "session state"

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
Run tests manually, taking time to check and try breaking the code, and then honing in on the specific code-based solution when I am not familiar with the codebase overall

- What is one thing you would do differently next time you work with AI on a coding task?
I tend to first jot down, pen and pencil, ideas to see how things flow from one loop to another (akin to a loose or vague flowchart). Next time I would also provide the agent a version of that, to better explain my thinking.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
I am realizing that AI-generated code can be treated as a collaborative tool more than just a tester, particularly in edge cases or easily-overlooked bugs. I am still reluctant to give it access to any codebase more than it may be necesary, but its way of processing data can be taken as a specialized, supra-panoramic perspective that can be trained and refined.
