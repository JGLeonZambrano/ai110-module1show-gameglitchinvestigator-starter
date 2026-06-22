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
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
