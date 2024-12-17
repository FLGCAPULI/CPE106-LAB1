def main():
    filename = input("Please enter the filename: ")
    
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        while True:
            print(f"\nNumber of lines: {len(lines)}")
            line_number = int(input("Please enter a line number (0 to exit): "))
            
            if line_number == 0:
                print("Exiting the program.")
                break
            
            if 1 <= line_number <= len(lines):
                print(f"Line {line_number}: {lines[line_number - 1].strip()}")
            else:
                print("Invalid line number. Please try again.")
    
    except FileNotFoundError:
        print("File not found. Please try again.")
    except ValueError:
        print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()