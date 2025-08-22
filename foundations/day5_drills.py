def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Dividing by zero causes an error! Try again!")
if __name__ == "__main__":
    safe_divide(3, 0)

    random_dict = {
        64: 1,
        451: 2,
        642: 3,
        96: 4,
        1: 5,
        49: 6,
        23: 7,
        0: 8,
        1114: 9,
        75: 10
    }

    def get_value(dict):
        user_input = int(input("Pick an arbitrary value...\n"))
        try:
            print(random_dict[user_input])
        except KeyError:
            print("Key not Found")

    get_value(random_dict)

    def read_file(filename):
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
                line_count = len(lines)
                print(f"{filename} has {line_count} lines")
        except FileNotFoundError:
            print("Are you sure that's a real file?")

    read_file("/home/jvinagray/projects/py-mastery/notes/week_1.txt")

class ConversionError(Exception):
    def __init__(self, from_unit, to_unit, message="Those two units are not convertible"):
        self.from_unit = from_unit
        self.to_unit = to_unit
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}. Got {self.from_unit} & {self.to_unit}"

