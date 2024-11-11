import sys
from validate import validate_input
from fetch import fetch_github_repositories, fetch_nasa_apod
from send import send_email
from format import format_github_data, format_nasa_data


def main():
    valid_apis = ["github", "nasa"]

    email, api = validate_input(sys.argv, valid_apis)

    combined_data = ""

    if api == "github":
        data = fetch_github_repositories()
        combined_data = format_github_data(data)

    elif api == "nasa":
        data = fetch_nasa_apod()
        combined_data = format_nasa_data(data)

    send_email(f"Letter about {api}", combined_data, email)


if __name__ == "__main__":
    main()