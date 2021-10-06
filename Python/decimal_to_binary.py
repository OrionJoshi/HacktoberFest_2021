

def decimal_to_binary(decimal_number: int) -> str:
    """Function to convert a decimal number to a binary number."""
    binary = ""
    while decimal_number // 2 > 0:
        binary += str(decimal_number % 2)
        decimal_number = decimal_number // 2
    binary += str(decimal_number % 2)

    return binary[::-1]
