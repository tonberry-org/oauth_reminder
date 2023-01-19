import pythonlambdatemplate.lambda_function


def main(argv: list[str]) -> None:
    pythonlambdatemplate.lambda_function.lambda_handler({}, {})


if __name__ == "__main__":
    main(["hellow"])
