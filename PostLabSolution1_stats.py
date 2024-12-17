def get_numbers():
    numbers = input("Enter a list of numbers separated by spaces: ")
    return list(map(float, numbers.split()))

def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def mode(numbers):
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1
    max_freq = max(frequency.values())
    modes = [key for key, value in frequency.items() if value == max_freq]
    return modes if len(modes) > 1 else modes[0]

if __name__ == "__main__":
    numbers = get_numbers()
    print(f"Mean: {mean(numbers)}")
    print(f"Median: {median(numbers)}")
    print(f"Mode: {mode(numbers)}")
