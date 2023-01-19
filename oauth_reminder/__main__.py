import oauth_reminder.lambda_function


def main(argv: list[str]) -> None:
    oauth_reminder.lambda_function.lambda_handler({}, {})


if __name__ == "__main__":
    main(["hellow"])
