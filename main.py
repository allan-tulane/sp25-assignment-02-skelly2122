"""
CMPS 2200 Homework Assignment 2.
Refer to homework-02.md for comprehensive instructions.
"""
from collections import defaultdict
import math


#### Iterative approach
def check_brackets_iterative(sequence):
    """
    Implement the iterative approach to validate matching brackets.
    This function uses `process_sequence` with the `bracket_validator` function.

    Parameters:
      sequence...a list of characters to check
    Returns:
      True if all brackets are properly matched, False otherwise

    Examples:
    >>> check_brackets_iterative(['(', 'x', ')'])
    True
    >>> check_brackets_iterative(['('])
    False
    """
    ### Implementation
    return iterate(bracket_validator, 0, sequence) == 0
    ###


def bracket_validator(accumulated_value, current_char):
    """
    This function will be passed to the `process_sequence` function to 
    validate bracket matching.

    As with all functions used by process_sequence, it accepts:
    accumulated_value....the running total so far (e.g., the running count when checking brackets)
    current_char........the next character in the sequence

    Returns:
      the updated accumulated_value
    """
    ### Implementation
    if accumulated_value == -math.inf:  # already in error state, propagate it
        return accumulated_value
    
    if current_char == ')':           # found closing bracket
        if accumulated_value <= 0:    # no matching open bracket available
            return -math.inf          # indicate error state
        else:                         # match found
            return accumulated_value - 1  # decrease open bracket count
    elif current_char == '(':         # found opening bracket
        return accumulated_value + 1  # increase open bracket count
    else:                             # character is not a bracket
        return accumulated_value      # no change to counter
    ###

def iterate(func, initial, data):
    """
    Process a sequence by applying a function to each element sequentially.
    
    Parameters:
        func: function that takes two arguments (accumulated value, current element)
        initial: starting value for accumulation
        data: list of elements to process
        
    Returns:
        The final accumulated value
    """
    if len(data) == 0:
        return initial
    else:
        return iterate(func, func(initial, data[0]), data[1:])


def fold(func, base_value, data):
    if len(data) == 0:
        return base_value
    elif len(data) == 1:
        return func(base_value, data[0])
    else:
        midpoint = len(data) // 2
        return func(fold(func, base_value, data[:midpoint]), 
                    fold(func, base_value, data[midpoint:]))



#### Parallel solution using scan
def add(a, b):
    """
    Simple addition function
    """
    return a + b
    
def check_brackets_scan(sequence):
    """
    Implement a solution to bracket matching using `parallel_scan`.
    This function makes one call each to `parallel_scan`, `transform`, and `fold`

    Parameters:
      sequence...a list of characters to check
    Returns:
      True if all brackets are properly matched, False otherwise

    Examples:
    >>> check_brackets_scan(['(', 'x', ')'])
    True
    >>> check_brackets_scan(['('])
    False
    """
    ### Implementation
    running_sums, final_sum = parallel_scan(add, 0, list(map(bracket_value, sequence)))
    return final_sum == 0 and fold(minimum, 0, running_sums) >= 0
    ###

def parallel_scan(func, base_value, data):
    """
    A simplified implementation of parallel scan
    to demonstrate the concept.
    A more efficient implementation would be used in practice.
    """
    return (
            [fold(func, base_value, data[:i+1]) for i in range(len(data))],
             fold(func, base_value, data)
           )

def bracket_value(char):
    """
    Converts brackets to numeric values for processing.
    Returns 1 for '(', -1 for ')', and 0 for any other character.

    Parameters:
       char....a character from the input sequence

    >>> bracket_value('(')
    1
    >>> bracket_value(')')
    -1
    >>> bracket_value('x')
    0
    """
    if char == '(':
        return 1
    elif char == ')':
        return -1
    else:
        return 0

def minimum(a, b):
    """
    Returns the smaller of a and b. Used in `check_brackets_scan`.
    """
    if a < b:
        return a
    return b



#### Divide and conquer approach

def check_brackets_dc(sequence):
    """
    Uses check_brackets_dc_worker. If the result is (0,0),
    there are no unmatched brackets, so the input is valid.

    Returns:
      True if check_brackets_dc_worker returns (0,0); otherwise False
    """
    # implementation
    unmatched_right, unmatched_left = check_brackets_dc_worker(sequence)
    return unmatched_right == 0 and unmatched_left == 0

def check_brackets_dc_worker(sequence):
    """
    Recursive divide and conquer solution for bracket matching.

    Returns:
      tuple (R, L), where R is the count of unmatched right brackets, and
      L is the count of unmatched left brackets. This result is used by 
      check_brackets_dc to determine the final validity
    """
    ### Implementation
    # Base cases
    if len(sequence) == 0:
        return (0, 0)
    elif len(sequence) == 1:
        if sequence[0] == '(':
            return (0, 1)  # one unpaired left bracket
        elif sequence[0] == ')':
            return (1, 0)  # one unpaired right bracket
        else:
            return (0, 0)  # non-bracket character

    # Recursive division
    midpoint = len(sequence) // 2
    right1, left1 = check_brackets_dc_worker(sequence[:midpoint])
    right2, left2 = check_brackets_dc_worker(sequence[midpoint:])

    # Combine results
    # Calculate net unmatched brackets from both halves
    if left1 > right2:
        return (right1, left2 + left1 - right2)
    else:
        return (right1 + right2 - left1, left2)
    ###

if __name__ == "__main__":
    def verify_implementations():
        test_inputs = [
            (['(', 'x', ')'], True),
            (['('], False),
            ([')', '('], False),
            (['(', '(', ')', ')'], True),
            (['(', ')', '(', ')', '('], False),
        ]

        print("Evaluating check_brackets_iterative:")
        for input_seq, expected_output in test_inputs:
            actual_output = check_brackets_iterative(input_seq)
            print(f"Input: {input_seq} | Expected: {expected_output} | Result: {actual_output} | {'SUCCESS' if actual_output == expected_output else 'FAILURE'}")

        print("\nEvaluating check_brackets_scan:")
        for input_seq, expected_output in test_inputs:
            actual_output = check_brackets_scan(input_seq)
            print(f"Input: {input_seq} | Expected: {expected_output} | Result: {actual_output} | {'SUCCESS' if actual_output == expected_output else 'FAILURE'}")

        print("\nEvaluating check_brackets_dc:")
        for input_seq, expected_output in test_inputs:
            actual_output = check_brackets_dc(input_seq)
            print(f"Input: {input_seq} | Expected: {expected_output} | Result: {actual_output} | {'SUCCESS' if actual_output == expected_output else 'FAILURE'}")

        print("\nAll verification complete.")

    verify_implementations()
