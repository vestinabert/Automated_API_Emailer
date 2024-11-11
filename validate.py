import re
import sys


def validate_input(args, valid_apis):
    try:
        if len(args) != 3:
            raise ValueError(
                "Please provide exactly two arguments: an email address and an API choice."
            )

        email, api = args[1], args[2]

        is_valid_email(email)
        is_valid_api(api, valid_apis)

        return email, api

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


def is_valid_email(email):
    email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(email_regex, email):
        raise ValueError("Invalid email format. Please enter a valid email address.")
    return True


def is_valid_api(api, valid_apis):
    if api not in valid_apis:
        raise ValueError(
            f"Invalid API choice. Please choose one of the following: {', '.join(valid_apis)}"
        )
    return True
