import random


def converter():
    """generates random 4 digits number of 0s and 1s
    and convert the generated number to base 10
    """

    # Generate a random 4-digit binary number
    random_binary = "".join(random.choice(["0", "1"]) for _ in range(4))

    # Convert binary to base 10
    decimal_number = int(random_binary, 2)

    # Display the results
    print(f"Generated Random Binary: {random_binary}")
    print(f"Equivalent Decimal: {decimal_number}")


if __name__ == "__main__":
    converter()
