def mean(numbers):
    """
    Calculate the mean (average) of a list of numbers.
    
    :param numbers: List of numbers.
    :return: Mean of the numbers.
    """
    if not numbers:
        raise ValueError("The list of numbers is empty.")
    return sum(numbers) / len(numbers)

def median(numbers):
    """
    Calculate the median of a list of numbers.
    
    :param numbers: List of numbers.
    :return: Median of the numbers.
    """
    if not numbers:
        raise ValueError("The list of numbers is empty.")
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    middle = n // 2

    if n % 2 == 0:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    else:
        return sorted_numbers[middle]

def mode(numbers):
    """
    Calculate the mode of a list of numbers.
    If there are multiple modes, returns the smallest one.
    
    :param numbers: List of numbers.
    :return: Mode of the numbers.
    """
    if not numbers:
        raise ValueError("The list of numbers is empty.")
    
    from collections import Counter
    frequency = Counter(numbers)
    max_count = max(frequency.values())

    modes = [num for num, count in frequency.items() if count == max_count]

    return min(modes)

if __name__ == "__main__":
    try:
        data = list(map(float, input("Enter a list of numbers separated by spaces: ").split()))
        print("Mean:", mean(data))
        print("Median:", median(data))
        print("Mode:", mode(data))
    except ValueError as e:
        print("Error:", e)
