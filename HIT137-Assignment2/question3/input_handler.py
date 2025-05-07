def get_validated_input(
    prompt, expected_type, condition=lambda x: True, error_msg="Invalid input."
):
    """Get validated user input with type and value checking."""
    while True:
        try:
            value = expected_type(input(prompt))
            if not condition(value):
                print(error_msg)
                continue
            return value
        except ValueError:
            print(f"Error: Please enter a valid {expected_type.__name__}.")
