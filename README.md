# 🐍 Hangman (Mini) — Instructor-Ready Lesson

Lightweight, beginner-friendly **Python CLI Hangman**. Teach input handling, loops, conditionals, sets, functions, and simple state machines in **~90 minutes**. Includes step-by-step plan, quizzes, challenges, and a fully commented solution.

---

## 🧰 Tools & Setup

**You’ll Need**
- **Python 3.9+** (3.11 recommended). Check with:
  ```bash
  python --version
  ```
  or on some systems:
  ```bash
  python3 --version
  ```
- **Code editor:** VS Code (recommended) or any text editor
  - Optional VS Code extensions: *Python* (Microsoft), *Pylance*
- **Terminal** (Command Prompt, PowerShell, macOS Terminal, or VS Code Terminal)

**Project Structure**
```
hangman-mini/
├─ hangman.py          # game source (documented)
└─ README.md   # this file
```

**Run It**
```bash
python hangman.py
# or
python3 hangman.py
```

---

## 🎯 Learning Objectives

By the end, learners can:
1. Read and validate user input from the terminal
2. Use **loops** and **conditionals** to control game flow
3. Store and query unique items with **sets**
4. Split logic into **functions** (single responsibility)
5. Handle **errors & edge cases** (repeated guesses, invalid characters)
6. Improve UX with clear messages and formatted output

---

## Mini Quizzes

**Q1.** Why is a **set** a good structure for `guessed` letters?
**Q2.** What’s the difference between `break` and `return` in a function?
**Q3.** Why should we validate user input **before** mutating game state?
**Q4.** Write a boolean expression that detects a **win** state.

---

## Challenges

1) **Word Source Swap** — Load words from a text file (one per line) and skip short words.
2) **Hint System** — Add one free reveal per game (`hint` command).
3) **Difficulty Modes** — Easy/Normal/Hard adjust `MAX_TRIES` and word length.
4) **ASCII Art Hangman** — Draw a gallows that updates each miss.
5) **Scoreboard** — Track wins/losses in a local JSON file.
6) **Phrase Mode** — Support spaces and apostrophes in phrases.
7) **Tests** — Add simple unit tests for `render_mask` and validation logic.

---

## 🧯 Troubleshooting

| Symptom | Likely Fix |
|--------|------------|
| Repeated letter still consumes a try | Add a `if guess in guessed: continue` check early |
| Non-letters crash the game | Validate with `.isalpha()` and `len(guess) == 1` |
| Mask never reveals | Ensure you rebuild the mask each loop from current `guessed` |
| Win never triggers | Use `all(ch in guessed for ch in secret)` |
| Unicode errors on Windows | Save file as UTF-8, avoid emojis if terminal can’t display |
