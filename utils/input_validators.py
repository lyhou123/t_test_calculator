"""
Input validation utilities for statistical analysis.
"""

def get_positive_int(prompt):
    """Get a positive integer from user input with validation."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer.")


def get_positive_float(prompt):
    """Get a positive float from user input with validation."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")


def get_float(prompt):
    """Get any float from user input with validation."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_test_type():
    """Get test type with validation."""
    while True:
        test_type = input("Choose test type ('one-tailed' or 'two-tailed'): ").strip().lower()
        if test_type in ['one-tailed', 'two-tailed']:
            return test_type
        print("Please enter 'one-tailed' or 'two-tailed'.")

def get_direction():
    """Get direction for one-tailed test with validation."""
    while True:
        direction = input("Choose direction ('greater' or 'less'): ").strip().lower()
        if direction in ['greater', 'less']:
            return direction
        print("Please enter 'greater' or 'less'.")

        
def get_alpha_level():
    """Get significance level with validation."""
    while True:
        try:
            alpha = float(input("Enter significance level (default 0.05): ") or "0.05")
            if 0 < alpha < 1:
                return alpha
            else:
                print("Please enter a value between 0 and 1.")
        except ValueError:
            print("Please enter a valid number.")
