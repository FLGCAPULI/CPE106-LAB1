# stats.py

def mean(numbers):
    """
    Compute the mean (average) of a list of numbers.
    :param numbers: List of numbers
    :return: Mean of the numbers
    """
    if not numbers:
        raise ValueError("The list is empty.")
    return sum(numbers) / len(numbers)

def median(numbers):
    """
    Compute the median of a list of numbers.
    :param numbers: List of numbers
    :return: Median of the numbers
    """
    if not numbers:
        raise ValueError("The list is empty.")
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2

    if n % 2 == 0:
        # Even number of elements: average of the two middle numbers
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        # Odd number of elements: middle number
        return sorted_numbers[mid]

def mode(numbers):
    """
    Compute the mode of a list of numbers.
    :param numbers: List of numbers
    :return: Mode of the numbers
    """
    if not numbers:
        raise ValueError("The list is empty.")
    from collections import Counter
    
    counts = Counter(numbers)
    max_frequency = max(counts.values())
    modes = [key for key, value in counts.items() if value == max_frequency]

    if len(modes) == 1:
        return modes[0]  # Single mode
    else:
        return modes  # Multiple modes or no clear mode
