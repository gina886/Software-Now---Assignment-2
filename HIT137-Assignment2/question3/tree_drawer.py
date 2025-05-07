import turtle


def draw_tree(branch_length, angle_left, angle_right, reduction_factor, depth):
    """
    Recursively draws a tree based on the given parameters.
    """
    if depth == 0:
        return

    turtle.forward(branch_length)

    # Left branch
    turtle.left(angle_left)
    draw_tree(
        branch_length * reduction_factor,
        angle_left,
        angle_right,
        reduction_factor,
        depth - 1,
    )

    # Right branch
    turtle.right(angle_left + angle_right)
    draw_tree(
        branch_length * reduction_factor,
        angle_left,
        angle_right,
        reduction_factor,
        depth - 1,
    )

    # Restore original orientation and position
    turtle.left(angle_right)
    turtle.backward(branch_length)
