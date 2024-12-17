import statistics

def mean(numbers):
    """Compute the mean (average) of a list of numbers."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

def median(numbers):
    """Compute the median of a list of numbers."""
    if not numbers:
        return None
    return statistics.median(numbers)

def mode(numbers):
    """Compute the mode of a list of numbers."""
    if not numbers:
        return None
    try:
        return statistics.mode(numbers)
    except statistics.StatisticsError:
        return "No unique mode found"

# Test the functions
if __name__ == "__main__":
    # Sample test data
    numbers = [4, 1, 2, 2, 5, 6, 6, 7, 8]
    print("Numbers:", numbers)
    print("Mean:", mean(numbers))        # Expected: 4.5556
    print("Median:", median(numbers))    # Expected: 5
    print("Mode:", mode(numbers))        # Expected: 2 (first mode found)
