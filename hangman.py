#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random  # Used to choose a random secret word from our list
import sys     # Used for a graceful exit in some paths (optional)

# ----------------------------
# CONFIGURATION / CONSTANTS
# ----------------------------

# A small default word list to keep the first session simple. You can swap this out
# to load from a text file later (see Challenges in the README).
DEFAULT_WORDS = [
    # TODO Add in word/s
]

# Number of incorrect guesses allowed before losing the round.
MAX_TRIES = 6

# The hangman pics
HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===""",
]


# ----------------------------
# UTILITY FUNCTIONS
# ----------------------------

def pick_word(words):
    """
    Choose and return a random secret word from the provided list.
    """
    # random.choice selects one element uniformly at random
    # TODO Create the word randomizer to select


def render_mask(secret, guessed):
    """
    Return a masked version of the secret word, revealing only the letters that
    have been guessed. Un-guessed letters appear as underscores.

    Example:
      secret  = 'python'
      guessed = {'p', 'o'}
      result  = 'p _ _ _ o _'

    Parameters:
      secret  (str): the secret answer word
      guessed (set[str]): a set of guessed characters (lowercase)

    Returns:
      str: masked word with spaces between characters for readability
    """
    # Build a list of characters: real letter if guessed, '_' if not.
    display_chars = [ch if ch in guessed else '_' for ch in secret]
    # Join with spaces to make the mask easier to read on a terminal.
    return ' '.join(display_chars)


def is_win(secret, guessed):
    """
    Determine if the player has guessed all letters in 'secret'.

    Why this matters:
    - Keeps win logic in one place (Single Responsibility principle).
    - Easy to write a small test for this logic alone.
    """
    # A win occurs when every character in the secret is present in 'guessed'.
    return all(ch in guessed for ch in secret)


def prompt_letter():
    """
    Prompt the user for a single-letter alphabetic guess, normalized to lowercase.
    Re-prompts until a valid input is received.

    Why re-prompt?
    - Prevents invalid state transitions in the main game loop.
    - Keeps input validation encapsulated here (cleaner main loop).
    """
    # TODO Create the user prompt!


def ask_play_again():
    """
    Ask the user whether they want to play another round.

    Returns:
      bool: True if yes, False otherwise.
    """
    while True:
        ans = input("Play again? (y/n): ").strip().lower()
        if ans in {"y", "yes"}:
            return True
        if ans in {"n", "no"}:
            return False
        print("Please enter 'y' or 'n'.")


# ----------------------------
# CORE GAME LOOP (ONE ROUND)
# ----------------------------

def play_round(words=DEFAULT_WORDS, max_tries=MAX_TRIES, show_ascii=True):
    """
    Play a single round of Hangman.

    Parameters:
      words (list[str]): list to draw a secret word from
      max_tries (int): number of incorrect guesses allowed
      show_ascii (bool): whether to display gallows art

    Returns:
      bool: True if the player won the round, False if they lost
    """
    secret = pick_word(words)        # Choose a random answer
    guessed = set()                  # All unique letters the player has guessed
    misses = set()                   # Letters guessed that are NOT in the secret
    remaining = max_tries            # Tries left before losing

    print("\n=== New Game ===")
    print(f"Word has {len(secret)} letters.")
    print("Type 'quit' or 'exit' at any time to leave.\n")

    # Main guessing loop continues until win or out of tries.
    while True:
        # Optional: show ASCII gallows based on number of misses so far.
        if show_ascii:
            stage = len(misses)
            if 0 <= stage < len(HANGMAN_PICS):
                print(HANGMAN_PICS[stage])

        # Show the current mask, misses, and tries left.
        print("Word:     ", render_mask(secret, guessed))
        print("Misses:   ", ' '.join(sorted(misses)) if misses else "(none)")
        print(f"Tries left: {remaining}\n")

        # Get a (validated) guess from the user.
        guess = prompt_letter()

        # TODO Add in logic if it was already guessed :/

        # TODO Add in logic for good guess :)

        # TODO Add in logic for bad guess :(


# ----------------------------
# PROGRAM ENTRY POINT
# ----------------------------

def main():
    """
    Main entry point: plays one or more rounds until the player says 'no'.
    Keeping this separate from 'play_round' makes the code easier to test.
    """
    print("Welcome to Hangman (Mini)!")
    while True:
        _ = play_round()
        if not ask_play_again():
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    # Executes only when run as a script, not when imported as a module.
    main()
