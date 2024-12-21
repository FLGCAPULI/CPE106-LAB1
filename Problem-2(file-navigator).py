def main():
    try:
        filename = input("Enter the filename: ")

        with open(filename, 'r') as file:
            lines = file.readlines()

        while True:
            print(f"The file has {len(lines)} lines.")

            try:
                line_number = int(input("Enter a line number (0 to quit): "))

                if line_number == 0:
                    print("Exiting the program.")
                    break

                if 1 <= line_number <= len(lines):
                    print(f"Line {line_number}: {lines[line_number - 1].strip()}")
                else:
                    print("Invalid line number. Please try again.")

            except ValueError:
                print("Invalid input. Please enter a number.")

    except FileNotFoundError:
        print("The file does not exist. Please check the filename and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
