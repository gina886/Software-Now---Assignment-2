from input_handler import get_validated_input
from tree_drawer import draw_tree
from turtle_setup import setup_turtle
import turtle


def main():
    print("=== Recursive Turtle Tree Drawing Program ===")

    # Input
    angle_left = get_validated_input(
        "Left branch angle (0-90): ",
        float,
        lambda x: 0 <= x <= 90,
        "Must be between 0 and 90.",
    )
    angle_right = get_validated_input(
        "Right branch angle (0-90): ",
        float,
        lambda x: 0 <= x <= 90,
        "Must be between 0 and 90.",
    )
    start_length = get_validated_input(
        "Starting branch length (>0): ", float, lambda x: x > 0, "Must be > 0."
    )
    reduction = get_validated_input(
        "Reduction factor (0-1): ",
        float,
        lambda x: 0 < x < 1,
        "Must be between 0 and 1.",
    )
    depth = get_validated_input(
        "Recursion depth (>0): ", int, lambda x: x > 0, "Must be > 0."
    )

    # Setup and draw
    setup_turtle(start_length)
    draw_tree(start_length * reduction, angle_left, angle_right, reduction, depth - 1)

    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()
