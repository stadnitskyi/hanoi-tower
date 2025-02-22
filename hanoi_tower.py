def move_disk(from_pole, to_pole):
    print(f"Move disk from {from_pole} to {to_pole}")


def hanoi(n, from_pole, to_pole, aux_pole):
    if n == 1:
        move_disk(from_pole, to_pole)
    else:
        hanoi(n - 1, from_pole, aux_pole, to_pole)
        move_disk(from_pole, to_pole)
        hanoi(n - 1, aux_pole, to_pole, from_pole)


if __name__ == "__main__":
    n = 3
    hanoi(n, "A", "C", "B")
