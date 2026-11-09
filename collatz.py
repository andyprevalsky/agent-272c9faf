"""Print the Collatz sequence starting at 27 and the number of steps to reach 1."""


def collatz_sequence(n: int) -> list[int]:
    if n < 1:
        raise ValueError("n must be a positive integer")
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence


def main() -> None:
    sequence = collatz_sequence(27)
    for number in sequence:
        print(number)
    # Steps are transformations, so one fewer than the count of numbers.
    total_steps = len(sequence) - 1
    print(f"Total steps: {total_steps}")


if __name__ == "__main__":
    main()
