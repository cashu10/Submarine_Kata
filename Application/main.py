import argparse
from submarine import Submarine
from parse_inputs import parseInputs, parseLine

def plot_graph(horizontal_positions, depths):
    try:
        import matplotlib
        matplotlib.use("Qt5Agg")
        import matplotlib.pyplot as plt

        plt.plot(horizontal_positions, depths, marker="o")
        plt.xlabel("Horizontal Position")
        plt.ylabel("Depth")
        plt.title("Submarine Path")
        plt.gca().invert_yaxis()  # Depth increases downward
        plt.show()
    except ImportError:
        print("Matplotlib is not installed. Install it to enable graphing.")


def main(graph=False, aim=False):
    with open("input.txt", "r") as file:
        input_data = file.read()

    parsed_data = parseInputs(input_data)

    submarine = Submarine()

    horizontal_positions = [0]
    depths = [0]

    for command in parsed_data:
        if command["command"] == "forward":
            submarine.moveHorizontal(command["value"])
        elif command["command"] == "down":
            if aim:
                submarine.moveAim(command["value"])
            else:
                submarine.moveDepth(command["value"])
        elif command["command"] == "up":
            if aim:
                submarine.moveAim(-command["value"])
            else:
                submarine.moveDepth(-command["value"])

        horizontal_positions.append(submarine.horizontal)
        depths.append(submarine.depth)

    final_position = submarine.getPosition()
    print(f"Final Position: {final_position}")

    if graph:
        plot_graph(horizontal_positions, depths)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Submarine Navigation")
    parser.add_argument("--graph", action="store_true", help="Graph the submarine's path")
    parser.add_argument("--aim", action="store_true", help="Use aim the submarine's path")
    args = parser.parse_args()

    main(graph=args.graph, aim=args.aim)