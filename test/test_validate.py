import pytest
from validate import validate_input, is_valid_email, is_valid_api

valid_apis = ["API1", "API2"]


def test_validate_input_success():
    args = ["script_name", "test@example.com", "API1"]
    email, api = validate_input(args, valid_apis)
    assert email == "test@example.com"
    assert api == "API1"


def test_validate_input_invalid_email():
    args = ["script_name", "invalid-email", "API1"]
    with pytest.raises(SystemExit):
        validate_input(args, valid_apis)


def test_validate_input_invalid_api():
    args = ["script_name", "test@example.com", "InvalidAPI"]
    with pytest.raises(SystemExit):
        validate_input(args, valid_apis)


def test_validate_input_wrong_argument_count():
    args = ["script_name", "test@example.com"]
    with pytest.raises(SystemExit):
        validate_input(args, valid_apis)


def test_is_valid_email_success():
    assert is_valid_email("test@example.com") == True


def test_is_valid_email_invalid_format():
    with pytest.raises(ValueError, match="Invalid email format"):
        is_valid_email("invalid-email")


def test_is_valid_api_success():
    assert is_valid_api("API1", valid_apis) == True


def test_is_valid_api_invalid_choice():
    with pytest.raises(
        ValueError, match="Invalid API choice. Please choose one of the following"
    ):
        is_valid_api("InvalidAPI", valid_apis)
