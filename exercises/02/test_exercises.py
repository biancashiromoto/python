import pytest
from exercises import fizz_buzz, 


def test_fizz_buzz_should_return_list_of_numbers():
    assert fizz_buzz(5) == [1, 2, "Fizz", 4, "Buzz"]


def test_validate_email():
    with pytest.raises(ValueError):
        validate_email("email.com.br")
