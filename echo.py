# echo.py


def echo(text: str, repetitions: int = 3) -> str:
    last_repetitions_index = -abs(repetitions)
    for i in range(repetitions):
        print(text[last_repetitions_index:])
        last_repetitions_index += 1
    return "."


if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
