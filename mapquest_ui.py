import output_types


output_classes = {"STEPS": output_types.Steps, "TOTALDISTANCE": output_types.Totaldistance, "TOTALTIME": output_types.Totaltime,
                  "LATLONG": output_types.Latlong, "ELEVATION": output_types.Elevation}
locations = []
outputs = []


def read_num_minimum(min: int) -> int:
    """ Asks for input of a minimum value until valid and returns it """
    while True:
        try:
            num = int(input().strip())
            if num >= min:
                return num
            else:
                print("Number should be {} or greater".format(min))
        except ValueError:
            print("Not an integer")


def check_valid_output(output: str) -> bool:
    """ Checks if output is valid parameter """
    valid = ["STEPS", "TOTALDISTANCE", "TOTALTIME", "LATLONG", "ELEVATION"]
    return output in valid


def read_input() -> None:
    """ Reads input for locations and outputs """
    global locations
    global output

    num_locations = read_num_minimum(2)
    for num in range(num_locations):
        locations.append(str(input().strip()))

    num_outputs = read_num_minimum(1)
    for num in range(num_outputs):
        output = str(input().strip()).upper()
        if check_valid_output(output):
            outputs.append(output_classes[output](locations))
    print()


if __name__ == "__main__":
    read_input()
    for output in outputs:
        output.print_info()

    print("Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors")
