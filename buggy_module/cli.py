def main() -> None:

    # ruff tells me to be kinder to my future self
    df = None

    a: str = ""

    # flake8 should show some errors here
    d=a[2+3: 10   ] +"p"

    # mypy tells me that my type is wrong
    a = -1


if __name__ == "__main__":
    main()
