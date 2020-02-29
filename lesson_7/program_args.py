import argparse

def main():
    parser = argparse.ArgumentParser(description="Show contents of a file")
    parser.add_argument("file", help="The file which needs to be shown", type=str)
    parser.add_argument("-l", "--line_numbers", help="Show line numbers", action="store_true", default=False)
    parser_args = parser.parse_args()

    with open(parser_args.file, mode="r") as file:
        if parser_args.line_numbers:
            line_count = 1
            for line in file:
                print("{} {}".format(line_count, line))
                line_count = line_count + 1
        else:
            for line in file:
                print(line)

if __name__ == "__main__":
    main()