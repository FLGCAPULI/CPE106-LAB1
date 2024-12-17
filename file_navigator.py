def read_file_to_list(filename):
    """Read file content into a list where each line is an element."""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        return [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []

def navigate_lines(lines):
    """Navigate through the list of lines based on user input."""
    if not lines:
        print("The file is empty or not found.")
        return
    
    while True:
        print(f"\nTotal lines: {len(lines)}")
        try:
            line_number = int(input("Enter a line number (0 to quit): "))
            if line_number == 0:
                print("Exiting program.")
                break
            elif 1 <= line_number <= len(lines):
                print(f"Line {line_number}: {lines[line_number - 1]}")
            else:
                print("Invalid line number. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    # Prompt the user for a filename
    filename = input("Enter the filename: ")
    lines = read_file_to_list(filename)
    if lines:
        navigate_lines(lines)
