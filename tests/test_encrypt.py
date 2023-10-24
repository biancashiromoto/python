import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    def test_non_int_key():
        with pytest.raises(TypeError, match="tipo inválido para key"):
            encrypt_message("message", "a")

    test_non_int_key()

    def test_non_string_message():
        with pytest.raises(TypeError, match="tipo inválido para message"):
            encrypt_message(2, 1)

    test_non_string_message()

    def test_non_positive_index():
        "If key < 0, the function should return the message reversed"
        message = "message"
        assert encrypt_message(message, -1) == message[::-1]

    test_non_positive_index()

    def test_odd_key():
        "If key % 2 == 0, the function should return the encrypted message"
        message = "message"
        result = "egass_em"
        assert encrypt_message(message, 2) == result

    test_odd_key()