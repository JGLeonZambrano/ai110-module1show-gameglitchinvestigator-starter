# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation
You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.
- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission
1. **Play the game.** Open the "Developer Debug Info" tab to see the secret number. Try to win.
2. **Find the bugs.** Note anything that behaves unexpectedly.
3. **Fix the Logic.** Repair the broken input validation and game state.
4. **Refactor & Test.** Run `pytest` to confirm your fixes hold.

## 📝 Document Your Experience
**Purpose:** A number guessing game where the player tries to guess a secret number 
between 1 and 100 within a limited number of attempts, with hints after each guess.

**Bugs found:**
- Out-of-range numbers (e.g. 0, negatives, above 100) were accepted as valid guesses
- Decimal inputs (e.g. 7.5) were silently truncated and accepted instead of rejected
- The New Game button failed to reset game status, leaving the game stuck in a 
  won/lost state and preventing new guesses

**Fixes applied:**
- `parse_guess()` now explicitly rejects decimals and validates the 1–100 range
- The `if new_game:` block now resets `st.session_state.status` to `"playing"`, 
  along with score, attempts, and history

## 📸 Demo Walkthrough
1. Run the app with `python -m streamlit run app.py` and open localhost:8501
2. Select difficulty from the sidebar (Easy/Normal/Hard changes range and attempt limit)
3. Enter a guess (e.g. 50) and click Submit Guess 🚀 — a hint appears ("Go HIGHER!" or "Go LOWER!")
4. Enter a decimal like 7.5 — the app now rejects it with "That's not a whole number"
5. Enter 0 — the app rejects it with "Number out of range"
6. Keep guessing until you win — balloons appear and your final score is shown
7. Click New Game 🔁 — the game fully resets and you can play again immediately

## 🧪 Test Results

```
#pytest tests/test_game_logic.py

============================= test session starts ==============================

collected 5 items
tests/test_game_logic.py .....                                           [100%]
============================== 5 passed in 0.42s ===============================
```

## 🚀 Stretch Features
- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here]
