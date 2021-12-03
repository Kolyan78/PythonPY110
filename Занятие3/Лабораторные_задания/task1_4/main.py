INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE, "r") as input_file, open(OUTPUT_FILE, "w") as output_file:
        for upper_line in map(str.upper, input_file):
            output_file.write(upper_line)


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
