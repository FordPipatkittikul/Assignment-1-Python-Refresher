# echo.py


def echo(v: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo"""
    last_repetitions_index = -abs(repetitions)
    for _ in range(repetitions):
        print(v[last_repetitions_index:])
        last_repetitions_index += 1
    return "."


if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
