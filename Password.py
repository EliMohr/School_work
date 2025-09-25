"""Password prompt that reveals hints after repeated failed attempts."""

# Import typing helpers so we can explain the shapes of values we pass around.
from typing import List, Optional, Callable


# Define a function that keeps asking for the password until the user gets it right or quits.
def prompt_for_password(
    valid_password: str,
    *,
    hints: Optional[List[str]] = None,
    attempts_before_first_hint: int = 3,
    hint_spacing: int = 2,
    input_func: Callable[[str], str] = input,
    output_func: Callable[[str], None] = print,
) -> bool:
    """Prompt the user until they enter ``valid_password`` or quit.

    Parameters
    ----------
    valid_password:
        The password users must enter.
    hints:
        A list of incremental hints that are shown after repeated failures.
    attempts_before_first_hint:
        Number of wrong attempts before the first hint is revealed.
    hint_spacing:
        Additional wrong attempts required between subsequent hints.
    input_func, output_func:
        Injected I/O functions, useful for testing.

    Returns
    -------
    bool
        ``True`` if access is granted, ``False`` otherwise.
    """

    # Use the provided hints, or fall back to these automatic ones if none were given.
    prepared_hints = hints or [
        f"Hint: The password is {len(valid_password)} characters long.",
        f"Hint: It starts with '{valid_password[:len(valid_password) // 2]}'.",
        f"Hint: It ends with '{valid_password[-3:]}'.",
    ]

    # Keep track of how many wrong tries the user has made.
    attempts = 0
    # Keep track of how many hints we have already shared.
    hints_shown = 0

    # Repeat the prompt until the function returns.
    while True:
        # Ask the user to type their password.
        user_input = input_func("Enter your password: ")

        # If the guess matches, tell them they can enter and finish the function.
        if user_input == valid_password:
            output_func("Access granted")
            return True

        # Let the user type "quit" or "exit" to give up and leave the loop.
        if user_input.lower() in {"quit", "exit"}:
            output_func("Access denied")
            return False

        # Count this as another failed attempt and ask them to try again.
        attempts += 1
        output_func("Incorrect password, try again.")

        # Only show a hint when we still have one left to share.
        if hints_shown < len(prepared_hints):
            # Figure out how many attempts the user must make before the next hint appears.
            hint_threshold = attempts_before_first_hint + (hints_shown * hint_spacing)
            # If the user has reached that many attempts, show the next hint and remember it was shown.
            if attempts >= hint_threshold:
                output_func(prepared_hints[hints_shown])
                hints_shown += 1


# Run this block only when the file is executed directly (not when it is imported).
if __name__ == "__main__":
    # This is the password the user must guess.
    VALID_PASSWORD = "PythonPass123"
    # These are the human-friendly hints we want to show after enough wrong tries.
    PASSWORD_HINTS = [
        "Hint: The password uses both letters and numbers.",
        "Hint: It begins with the word 'Python'.",
        "Hint: The final three characters are digits.",
    ]

    # Call the function with our password, hints, and hint timing settings.
    prompt_for_password(
        VALID_PASSWORD,
        hints=PASSWORD_HINTS,
        attempts_before_first_hint=3,
        hint_spacing=2,
    )